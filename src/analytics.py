import pandas as pd

def get_audit_summary(file_path="data/prediction_audit.csv"):
    df = pd.read_csv(file_path)
    
    # Using functional-style chaining (very advanced/clean)
    summary = {
        "total_requests": len(df),
        "avg_co2": df['co2'].mean(),
        "occupancy_rate": (df['prediction'] == 1).mean() * 100
    }
    
    return summary

if __name__ == "__main__":
    print(f"📊 Audit Summary: {get_audit_summary()}")