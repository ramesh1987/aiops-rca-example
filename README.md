# AIOps RCA with FAISS

---

## 📈 Project Summary

This project builds a real-time **AIOps Root Cause Analysis (RCA)** pipeline to detect anomalies in system metrics (like Load Balancer errors, Pod connection failures, DB availability) and predict the root cause automatically.

It uses:
- **MinMaxScaler** for data normalization
- **Isolation Forest** for anomaly detection
- **FAISS** for vector similarity search
- **Majority Voting** for Root Cause prediction

---

## 🧠 Key Components

| Component | Tool/Algorithm |
|-----------|----------------|
| Metrics Simulation | Python scripts |
| Data Normalization | MinMaxScaler (scikit-learn) |
| Vector Storage | FAISS (Facebook AI Similarity Search) |
| Anomaly Detection | Isolation Forest (scikit-learn) |
| Root Cause Analysis | Majority voting based on FAISS nearest neighbors |


---

## ⚙️ Architecture Flow

```
Telemetry Metrics (Load Balancer, App Pod, DB Node)
    ↓
Preprocessing (MinMaxScaler Normalization)
    ↓
Vector Storage (FAISS Vector DB)
    ↓
Anomaly Detection (Isolation Forest)
    ↓
Similar Incident Search (FAISS KNN)
    ↓
Root Cause Analysis (Majority Voting)
    ↓
RCA Report/Alert
```

---

## 🚀 Setup Instructions

1. Clone the repository
```bash
git clone <repo-url>
cd aiops_rca_faiss
```

2. Install Dependencies
```bash
pip install -r requirements.txt
```

3. Run the Application
```bash
python app/main.py
```

---

## 📦 Project Structure

```
├── app/
│   ├── data_collector.py     # Simulate load balancer, app pod, and DB node metrics
│   ├── vectorizer.py          # Normalize and vectorize metrics
│   ├── chromadb_store.py      # FAISS storage and similarity search
│   ├── rca_model.py           # Isolation Forest anomaly detection
│   └── main.py                # Full pipeline orchestration
├── requirements.txt
└── README.md
```

---

## 📚 Example Output

```plaintext
New metrics: { 'load_balancer_500_errors': 130, 'pod_db_conn_failure': 25, 'db_node_availability': 55 }

🚨 Anomaly Detected!

Top Similar Incidents: ['db_node_down', 'pod_failure']

🧠 Predicted Root Cause: db_node_down
```

✅ The system detects the anomaly and correctly predicts the root cause by matching historical incident patterns.

---

## 📢 Notes

- **FAISS** is highly efficient for handling large-scale numerical similarity search.
- **Isolation Forest** is an unsupervised ML model, perfect for real-world anomaly detection without labeled data.
- This project can be extended to use live Prometheus scraping and real observability pipelines.

---

## 🏆 Future Enhancements

- Integrate live Prometheus/Grafana telemetry feeds
- Extend RCA to multi-level correlation (Pod → Service → DB)
- Add REST API interface using FastAPI
- Implement Auto-Remediation actions post RCA

---

# Built for Intelligent AIOps 🚀

