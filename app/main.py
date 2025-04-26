import sys
import os
from collections import Counter

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import data_collector, vectorizer, chromadb_store, rca_model
import numpy as np

# Step 1: Collect Initial Metrics
data = data_collector.collect_metrics()

# Step 2: Fit Scaler and Vectorize Initial Metrics
vectorizer.fit_scaler(data)
X_train = np.array([vectorizer.vectorize({
    'load_balancer_500_errors': d['load_balancer_500_errors'],
    'pod_db_conn_failure': d['pod_db_conn_failure'],
    'db_node_availability': d['db_node_availability']
}) for d in data])

# Step 3: Add Vectors to FAISS
for idx, vec in enumerate(X_train):
    chromadb_store.add_vector(vec, {"incident": data[idx]['incident']}, f"vec_{idx}")

# Step 4: Train Isolation Forest RCA Model
model = rca_model.RCAIsolationForest()
model.train(X_train)

# Step 5: Simulate New Metrics
new_metrics = data_collector.simulate_new_metrics()

# Extract only the relevant numerical fields for vectorization
new_vector = vectorizer.vectorize({
    'load_balancer_500_errors': new_metrics['load_balancer_500_errors'],
    'pod_db_conn_failure': new_metrics['pod_db_conn_failure'],
    'db_node_availability': new_metrics['db_node_availability']
})

# Step 6: Detect Anomaly
is_anomaly = model.detect_anomaly(new_vector)

print(f"New metrics: {new_metrics}")

if is_anomaly:
    print("\n🚨 Anomaly Detected!")
    similar = chromadb_store.search_similar(new_vector)
    similar_incidents = [meta.get('incident', 'unknown') for meta in similar]

    print(f"\nTop Similar Incidents: {similar_incidents}")

    # Perform majority voting to predict Root Cause
    incident_counter = Counter(similar_incidents)
    likely_root_cause = incident_counter.most_common(1)[0][0]

    print(f"\n🧠 Predicted Root Cause: {likely_root_cause}")
else:
    print("\n✅ No anomaly detected.")
