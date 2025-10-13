# Installation 

```
!pip install mlflow
```


```
mlflow experiments create --experiment-name produce-metrics
MLFLOW_EXPERIMENT_ID=<YOUR_ID_HERE> python track_metrics.py
```
 


```

https://github.com/alfredodeza/mlflow-demo
# Running an actual mlflow project
conda activate exploratory
mlflow run . -P filename=carriage.csv
```


```
github.com/mlflow  mlflow-example
https://github.com/mlflow/mlflow-example.git
mlflow run git@github.com:mlflow/mlflow-example.git -P alpha=0.7
```

# Stuff to explore on your own
- Read the MLflow documentation to learn about advanced features like model registry and deployment.
- Learn how to register a model in the MLflow Model Registry and manage model versions.
- Try promoting a model to "Staging" or "Production" using the MLflow UI or CLI.
- Explore MLflow's model serving capabilities to deploy a trained model as a REST API.
- Experiment with MLflow's integration with cloud storage or remote tracking servers.
- Investigate how to use MLflow Projects for reproducible runs with different environments.
- Set up MLflow tracking with a remote backend database (e.g., PostgreSQL or MySQL).
- Explore MLflow's autologging features for popular ML libraries like scikit-learn, TensorFlow, or PyTorch.
