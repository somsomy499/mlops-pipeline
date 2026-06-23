import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def train_model():
    mlflow.set_experiment('mlops-pipeline')
    
    with mlflow.start_run():
        # Load data
        import pandas as pd
        df = pd.read_csv('data/train.csv')
        X_train, X_test, y_train, y_test = train_test_split(
            df.drop('target', axis=1), df['target'], test_size=0.2
        )
        
        # Train
        model = RandomForestClassifier(n_estimators=100, max_depth=10)
        model.fit(X_train, y_train)
        
        # Evaluate
        accuracy = accuracy_score(y_test, model.predict(X_test))
        mlflow.log_metric('accuracy', accuracy)
        mlflow.sklearn.log_model(model, 'model')
        print(f"Accuracy: {accuracy:.4f}")

if __name__ == '__main__':
    train_model()
