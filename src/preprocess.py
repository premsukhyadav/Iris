import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def preprocess_data(input_path="../data/raw/iris.csv", output_path="../data/processed/iris_processed.csv"):
    df = pd.read_csv(input_path)

    X = df.drop(columns=["target"])
    y = df["target"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    df_scaled = pd.DataFrame(X_scaled, columns=X.columns)
    df_scaled["target"] = y

    df_scaled.to_csv(output_path, index=False)
    return df_scaled

if __name__ == "__main__":
    df_scaled = preprocess_data()
    print(f"Processed data saved at data/processed/iris_processed.csv, shape: {df_scaled.shape}")