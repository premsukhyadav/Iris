import os
import mlflow
import mlflow.sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from mlflow.models.signature import infer_signature
import pandas as pd

# Set experiment
mlflow.set_experiment("iris_classification")

# Load data
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.Series(iris.target)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define models and params
models = {
    "LogisticRegression_1": LogisticRegression(max_iter=200, solver="lbfgs"),  # No multi_class param
    "LogisticRegression_2": LogisticRegression(max_iter=300, solver="liblinear"),  # No multi_class param
    "RandomForest_1": RandomForestClassifier(n_estimators=50, max_depth=3, random_state=42),
    "RandomForest_2": RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42),
}

best_model = None
best_accuracy = 0
best_params = None

# Train and log each model
for model_name, model in models.items():
    with mlflow.start_run(run_name=model_name):
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)

        # Infer signature & input example
        signature = infer_signature(X_train, model.predict(X_train))
        input_example = X_train.iloc[:5]  # small sample for logging

        # Log params, metrics, model
        if hasattr(model, "get_params"):
            mlflow.log_params(model.get_params())

        mlflow.log_metric("accuracy", acc)

        # Save model using `name` instead of deprecated `artifact_path`
        mlflow.sklearn.log_model(
            sk_model=model,
            name=model_name,
            signature=signature,
            input_example=input_example
        )

        print(f"{model_name} → Accuracy: {acc:.4f}")

        # Track best model
        if acc > best_accuracy:
            best_accuracy = acc
            best_model = model_name
            best_params = model.get_params()

print(f"\nBest Model: {best_model} with params {best_params} → Accuracy: {best_accuracy:.4f}")
