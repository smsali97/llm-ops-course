from mlflow import log_metric
from random import choice

def main():
    metric_names = ["cpu", "ram", "disk"]
    percentages = [i for i in range(0, 100)]

    for _ in range (40):
        log_metric(choice(metric_names), choice(percentages)) 


if __name__ == "__main__":
    mlflow.set_tracking_uri('http://127.0.0.1:5000')
    main()
