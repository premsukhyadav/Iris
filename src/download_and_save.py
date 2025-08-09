import pandas as pd
from sklearn.datasets import load_iris
from pathlib import Path

def download_and_save(save_path="../data/raw/iris.csv"):
    save_path = Path(save_path)
    save_path.parent.mkdir(parents=True, exist_ok=True)  # ensure directories exist

    iris = load_iris(as_frame=True)
    df = iris.frame  # includes features + target
    df.to_csv(save_path, index=False)

    print(f"Iris dataset downloaded and saved to {save_path}, shape={df.shape}")
    return df

if __name__ == "__main__":
    download_and_save()
