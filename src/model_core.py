from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
from src.utils import log_step

class OccupancyTrainer:
    def __init__(self, model_type="RF"):
        if model_type == "RF":
            self.model = RandomForestClassifier(n_estimators=100)
        self.is_trained = False

    @log_step
    def train(self, X, y):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        self.model.fit(X_train, y_train)
        
        # Quick validation
        preds = self.model.predict(X_test)
        acc = accuracy_score(y_test, preds)
        print(f"Model Accuracy: {acc * 100:.2f}%")
        
        self.is_trained = True
        return acc

    def save_model(self, file_path: str):
        if self.is_trained:
            joblib.dump(self.model, file_path)
            print(f"Model saved to {file_path}")