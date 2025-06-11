---

#  Insurance Premium Prediction API

This is a FastAPI-based backend application that predicts the **insurance premium category** based on user input. It provides endpoints to check the health of the API and get predictions using a trained ML model.

---

## 📦 Features

* ✅ RESTful API built with FastAPI
* 🔍 Predicts insurance premium category based on user attributes
* 🩺 Health check endpoint
* 🧠 ML model version tracking
* 📤 Clear JSON response format

---

## 🐳 Docker Image

You can directly pull the latest Docker image:

```bash
docker pull kaverapp/insurance_api:latest
```

> Read the full blog post on optimizing Python Docker images:
> 👉 [Optimizing Python Docker Images: A Deep Dive into uv vs pip for Size Reduction](https://timeflag.hashnode.dev/optimizing-python-docker-images-a-deep-dive-into-uv-vs-pip-for-size-reduction)

---

## 🛠️ Tech Stack

* **Python 3.12+**
* **FastAPI**
* **pydantic**
* **Uvicorn**

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/insurance-ml-api.git
cd insurance-ml-api
```

### 2. Install Dependencies

```bash
python -m venv env
source env/bin/activate   # or `env\Scripts\activate` on Windows

pip install -r requirements.txt
```

### 3. Run the Server

```bash
uvicorn app:app --reload
```

---

## 📡 API Endpoints

### `GET /`

Returns a welcome message.

### `GET /health`

Returns the API status, model version, and health info.

### `POST /predict`

Accepts a JSON payload and returns the predicted insurance premium category.

#### Example Input:

```json
{
  "age": 27,
  "income": 12.5,
  "occupation": "Unemployed",
  "smoker": "No",
  "weight":40,
  "height":1.3,
  "city":"Bangalore"
  
}
```

#### Example Output:

```json
{
  "predicted_category": "low"
}
```

---

## 📁 Project Structure

```
.
├── app.py
├── schema/
│   ├── user_input.py
│   └── prediction_response.py
├── model/
│   └── predict.py
├── requirements.txt
```

---

## 📄 License

This project is licensed under the MIT License.

---

## ✍️ Author

**Kirthan C.K.**
📖 [Read My Blog on Hashnode](https://timeflag.hashnode.dev/optimizing-python-docker-images-a-deep-dive-into-uv-vs-pip-for-size-reduction)

---

