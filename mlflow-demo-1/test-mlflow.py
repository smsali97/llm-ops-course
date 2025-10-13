from mlflow import log_metric, log_param, log_artifact
import mlflow
def main():
    log_param("threshold", 3)
    log_param("accuracy", 0.95)

    log_metric("timestamp", 1234567890)
    log_metric("TTC", 42)

    log_artifact("produced_data.csv")




if __name__ == "__main__":
    mlflow.set_tracking_uri('http://127.0.0.1:5000')
    main()