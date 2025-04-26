from sklearn.ensemble import IsolationForest
import numpy as np

class RCAIsolationForest:
    def __init__(self):
        self.model = IsolationForest(contamination=0.2)

    def train(self, X_train):
        self.model.fit(X_train)

    def detect_anomaly(self, X_test):
        prediction = self.model.predict([X_test])[0]
        return prediction == -1
