# Commands

```
python3 -m virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt

```

# Sample Request

```
curl -X POST  -H "Content-Type: application/JSON" \
  --data '["Containers are more or less interesting"]' \
  http://0.0.0.0:5000/predict

{
  "positive": false
}

$ curl -X POST  -H "Content-Type: application/json" \
  --data '["MLOps is critical for robustness"]' \
  http://0.0.0.0:5000/predict

{
  "positive": true
}
```

# How to build

```
docker build -t sualeh-class/roberta .
docker run -it -p 5000:5000 --rm sualeh-class/roberta
```

# ONNX Models

https://github.com/onnx/models


# Sample Request

```

$ curl -X POST  -H "Content-Type: application/JSON" \
  --data '["Containers are more or less interesting"]' \
  http://0.0.0.0:5000/predict

{
  "positive": false
}

$ curl -X POST  -H "Content-Type: application/json" \
  --data '["MLOps is critical for robustness"]' \
  http://0.0.0.0:5000/predict

{
  "positive": true
}
```

# For setting up with Azure Credentials

https://learn.microsoft.com/en-us/azure/developer/github/connect-from-azure-openid-connect