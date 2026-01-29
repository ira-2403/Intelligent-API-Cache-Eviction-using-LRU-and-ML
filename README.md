# 🧠 Intelligent API Cache Eviction System
A real-world backend project that implemets an **intelligent API caching system** using **LRU (DSA)** and **Machine Learning** to optimize cache eviction decisions. The system caches real API responses and uses an ML model to predict whether a cached request will be reused soon.

## Tech Stack
- Python
- FastAPI
- Streamlit
- Scikit-learn
- Requests 
- Pandas

## Project Structure
- backend/
- main.py
- cache/
- lru_cache.py
- ml/
- model.py
- predictor.py
- model.pkl
- utils/
- logger.py
- data/
- logs.csv
- frontend/
- app.py
- requirements.txt

## Unique Selling Point
- Real-time intelligent cache eviction using ML predictions
- LRU cache implementation using core DSA concepts
- Works with **any public API URL**
- ML model trained on real request logs, not simulated data
- End-to-end system: frontend->backend->cache->ML
- Beginner-friendly yet production-style backend architecture

## Features
- Accepts any public API request
- LRU-based caching with hit/miss tracking
- Machine learning-guided cache eviction
- Request logging for dataset creation
- Interactive Streamlit frontend
- Displays cache status and ML decision

## How It Works
1. User enters a public API URL in the streamlit app
2. Request is sent to FastAPI backend
3. Backend checks the LRU cache 
4. Cache HIT or MISS is recorded
5. ML model predicts whether the request will be reused
6. Cache eviction decision is made
7. Response and metadata are returned to the user

## How To Run
- pip install -r requirements.txt
- unicorn backend.main:app --reload
- streamlit run frontend/app.py

## Output Shown To User
- API response data
- Cache HIT/MISS
- ML decision (KEEP/EVICT)
- Response time

## Future Improvement
- Support for multiple eviction strategies (LFU,ARC)
- Online learning for ML model
- Redis integration
- Deployment using Docker