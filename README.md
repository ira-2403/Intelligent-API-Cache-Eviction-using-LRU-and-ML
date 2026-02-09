# 🚀 Intelligent API Cache Eviction using LRU + Machine Learning

A high-performance intelligent caching system that enhances traditional LRU (Least Recently Used) eviction using Machine Learning-based reuse prediction and hybrid scoring. The project compares standard LRU cache behaviour with an AI-driven intelligent eviction strategy through a real-time monitoring dashboard.

---

## 📌 Overview

Traditional caching strategies like LRU rely only on recency, which may not always reflect real usage patterns. This project introduces an **Intelligent LRU Cache** that combines:

* Frequency-based scoring
* Metadata analysis
* Machine learning predictions
* Hybrid eviction logic

The system allows real-time comparison between normal LRU and intelligent cache strategies via a professional monitoring dashboard.

---

## ✨ Features

### 🟦 Normal LRU Cache

* Classic least-recently-used eviction
* Doubly linked list implementation
* Hit/miss tracking
* Eviction logging

### 🧠 Intelligent ML-Based Cache

* Hybrid LFU + LRU behaviour
* Machine learning reuse prediction
* Metadata-driven eviction scoring
* Dynamic eviction candidate selection

### 📊 Interactive Dashboard

* Built using Streamlit
* Real-time cache monitoring
* HIT/MISS indicators
* Eviction tracking
* Side-by-side comparison view

---

## 🏗️ Architecture

Frontend (Streamlit Dashboard)
⬇
FastAPI Backend (API Gateway)
⬇
Caching Layer

* Normal LRU Cache
* Intelligent ML Cache

⬇
External APIs (Data Source)

---

## 🛠️ Tech Stack

### Backend

* Python
* FastAPI
* Requests
* Pydantic

### Machine Learning

* Scikit-learn
* Logistic Regression
* Joblib

### Data Structures

* Custom LRU Cache (Doubly Linked List + Hash Map)

### Frontend

* Streamlit

---

## 📂 Project Structure

```
backend/
│
├── cache/
│   ├── lru_cache.py
│   └── intelligent_lru.py
│
├── ml/
│   ├── predictor.py
│   └── cache_reuse_model.pkl
│
frontend/
│   └── app.py
│
main.py
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```
git clone <repo-url>
cd Intelligent-API-Cache-Eviction
```

### 2️⃣ Create Virtual Environment

```
python -m venv .venv
```

Activate:

Windows:

```
.venv\Scripts\activate
```

Mac/Linux:

```
source .venv/bin/activate
```

### 3️⃣ Install Dependencies

```
pip install fastapi uvicorn streamlit requests scikit-learn joblib pandas
```

---

## ▶️ Running the Project

### Start Backend

```
uvicorn main:app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```

---

### Start Dashboard

Open another terminal:

```
streamlit run frontend/app.py
```

---

## 🔬 API Endpoints

### Normal Cache Request

```
POST /request-normal
```

### Intelligent Cache Request

```
POST /request-smart
```

### Comparison

```
GET /comparison
```

### Eviction Logs

```
GET /normal-evictions
GET /intelligent-evictions
```

---

## 🧠 Intelligent Eviction Strategy

Eviction decisions are based on:

* URL request frequency
* Cache hit count
* Response time
* Data size
* Time difference between accesses
* ML reuse prediction

Hybrid score:

```
Final Score =
Frequency Score +
Metadata Score +
ML Prediction Score
```

Lower score → higher eviction probability.

---

## 📊 Example Workflow

1. Send API requests via dashboard
2. Requests pass through FastAPI
3. Cache lookup performed
4. Intelligent cache evaluates reuse probability
5. Eviction decision logged
6. Dashboard updates stats and comparison

---

## 🚀 Future Improvements

* Real-time charts
* Auto-refresh metrics
* Redis integration
* Reinforcement learning eviction
* Distributed cache simulation
* Visualization of cache timeline

---

## 👩‍💻 Author

Samriddhi Shaw

---

## 📜 License

MIT License
