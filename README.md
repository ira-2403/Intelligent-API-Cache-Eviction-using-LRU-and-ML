🧠 Intelligent LRU Cache with Machine Learning (DSA + ML Project)
A real-world system design project that combines Data Structures (LRU Cache) with Machine Learning to build an intelligent caching mechanism that predicts future data reuse and makes smarter eviction decisions that traditional LRU.

## Tech Stack
- Python
- Data Structures (HashMap, Doubly Linked List)
- Pandas
- Numpy
- Scikil-learn
- Matplotlib
- Streamlit

## Project Structure
- data/
- access_logs.csv
- src/
- lru_cache.py
- logger.py
- feature_engineering.py
- train_model.py
- predictor.py
- app.py
- models/
- reuse_predictor.pkl
- requirements.txt
- result.csv
- README.md

## Unique Selling Point (USP)
- Combines **core DSA concepts** with **Machine Learning**
- Moves beyond rule-based caching to **prediction-driven eviction**
- Simulates **real-world cache behavior** using access logs
- Demonstrates **system design thinking**, not just algorithms
- Shows how **ML** can optimize **low-performance system**

## Features
- Traditional LRU Cache implementation (O(1)
operations)
- Real-world cache access simulation
- Logging of cache access platforms
- Feature engineering from access logs
- Machine Learning-based eviction strategy
- Comparision between normal LRU and intelligent LRU
- Performance visualization

## Real-World Use Case
- API response caching
- E-commerce product caching
- Streaming content buffering
- Social media feed optimization
- Database query caching

## How It Works
- Cache stores frequently accessed items using LRU
- Access patterns are logged (frequency, recency, time gaps)
- ML model predicts probability of future reuse
- Cache evicts the item **lowest predicted reuse**, not just least recent

## How To Run
- pip install -r requirements.txt
- python src/logger.py
- python src/train_model.py
- streamlit run src/app.py

## Future Improvements
- Deep Learning-based reuse prediction
- Distributed cache support
- Real-time streaming logs
- Support for multiple eviction policies
- Cloud deployment

