import numpy as np
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

def fit_scaler(metrics_data):
    X = np.array([[m['load_balancer_500_errors'], m['pod_db_conn_failure'], m['db_node_availability']] for m in metrics_data])
    scaler.fit(X)

def vectorize(metrics_record):
    X = np.array([[metrics_record['load_balancer_500_errors'], metrics_record['pod_db_conn_failure'], metrics_record['db_node_availability']]])
    return scaler.transform(X)[0]
