import random

def collect_metrics():
    metrics_data = [
        {'incident': 'normal', 'load_balancer_500_errors': 5, 'pod_db_conn_failure': 0, 'db_node_availability': 100},
        {'incident': 'normal', 'load_balancer_500_errors': 8, 'pod_db_conn_failure': 1, 'db_node_availability': 100},
        {'incident': 'normal', 'load_balancer_500_errors': 3, 'pod_db_conn_failure': 0, 'db_node_availability': 100},
        {'incident': 'db_node_down', 'load_balancer_500_errors': 120, 'pod_db_conn_failure': 20, 'db_node_availability': 60},
        {'incident': 'pod_failure', 'load_balancer_500_errors': 70, 'pod_db_conn_failure': 15, 'db_node_availability': 90},
    ]
    return metrics_data

def simulate_new_metrics():
    return {
        'load_balancer_500_errors': 130,
        'pod_db_conn_failure': 25,
        'db_node_availability': 55
    }
