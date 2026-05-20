from src.data_pipeline import load_data, clean_data, split_features_target
from src.model_core import OccupancyTrainer

def run_training_pipeline():
    # 1. Pipeline
    raw_df = load_data("data/datatraining.txt")
    cleaned_df = clean_data(raw_df)
    X, y = split_features_target(cleaned_df)

    # 2. OOP Trainer
    trainer = OccupancyTrainer(model_type="RF")
    trainer.train(X, y)
    trainer.save_model("models/occupancy_v1.pkl")

if __name__ == "__main__":
    run_training_pipeline()