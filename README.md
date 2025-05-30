# TBI Technical Test Project

A lightweight Flask-based machine learning service with Prometheus metrics, containerization, security scanning, and AWS ECR integration.

---

## 🔧 Tech Stack

- **Flask** – Python web framework for API development  
- **Prometheus** – Metrics collection and monitoring  
- **Docker** – Containerization of the app  
- **AWS ECR** – Hosting and deployment of Docker images  
- **Pytest** – Unit testing framework  
- **Pipenv** – Python dependency management

---

## 📋 Requirements

- [Python 3.13+](https://www.python.org/downloads/)
- [Pipenv](https://pipenv.pypa.io/en/latest/)
- [Docker](https://www.docker.com/)
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) (for ECR login & push)

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Babaseun/tbi-ml-project
cd tbi-ml-project
```

2. Build and start the API:

   ```
    python3 server.py

    The server will be listening on port 5000
   ```

3. To run test unit tests:

   ```
   pipenv run pytest tests/
   ```

### Endpoints

1.  Metrics endpoint:

    - URL: `GET /http://localhost:5000/metrics`
    - Description: Returns prometheus metrics endpoint.

2.  Get Accounts:

    - URL: `GET http://localhost:5000`
      Path: /completion
      Method: POST
      Request Body:
      ```json
      { "messages": [ {"role": "user", "content": "message"} ] }
      Success response:
      ```

    ```json
    {
      "status": "success",
      "response": [{ "role": "assistant", "message": "response" }]
    }
    ```

    Model deployment status endpoint
    Path: /status
    Method: GET

    Response:

    ```json
    { "status": "NOT_DEPLOYED" | "PENDING" | "DEPLOYING" | "RUNNING" }
    ```

    Model information endpoint

    Path: /model
    Method: GET

    Response:

    ```json
    { "model_id": "model name" }
    ```

    Model deployment action endpoint

    Path: /model
    Method: POST

    Success response:

    ```json
    { "status": "success", "model_id": "model name"} ] }
    ```

    Error response:

    ```json
    { "status": "error", "message": "error message" }
    ```

### Improvements

- Add ArgoCD in the EKS cluster to pull changes from github and deploy automatically
- # Fetch a fresh ECR auth token and create a k8s secret in namespace “default”

  kubectl create secret docker-registry ecr-registry \
   --docker-server=${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com \
   --docker-username=AWS \
   --docker-password="$(aws ecr get-login-password --region ${AWS_REGION})" \
   --docker-email=you@example.com

- Reference the image in ECR in the kubernetes cluster
- Display the metrics on grafana dashboard
