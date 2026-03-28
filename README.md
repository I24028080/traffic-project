# Traffic Prediction & Route Optimization System

## 📌 Project Overview
This project is an AI-powered solution for urban traffic management. It combines **Machine Learning** to predict congestion levels and **Graph Theory** to find the most efficient travel route. 

It was developed as part of the **INT4203E Artificial Intelligence** individual assignment.

---

## 🚀 Key Features
* **Traffic Level Prediction**: Uses a **Random Forest Classifier** to predict traffic congestion (Low, Medium, High) based on time, weather, and vehicle density.
* **Dynamic Pathfinding**: Implements **Dijkstra’s Algorithm** that automatically adjusts road "weights" based on real-time AI predictions.
* **Web Interface**: A user-friendly dashboard built with **Flask** for real-time interaction.

---

## 🛠️ System Architecture
The system operates through a seamless pipeline:
1.  **Data Collection**: Historical traffic patterns stored in `traffic_dataset.csv`.
2.  **ML Engine**: `train_model.py` processes features and exports `traffic_model.pkl`.
3.  **Optimization Logic**: `route_optimizer.py` builds a weighted graph of the city.
4.  **Deployment**: `app.py` serves the prediction and routing results to the frontend.

---

## 💻 Installation & Setup
1.  **Clone the Repository**:
    git clone https://github.com/I24028080/traffic-project.git
    cd traffic_project

2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Train the Model**:
    ```bash
    python train_model.py
    ```

4.  **Run the Application**:
    ```bash
    python app.py
    ```

---

## 📊 Evaluation Results
The Random Forest model achieved an accuracy of **87%** on the test set. 

---

## 📂 File Structure
* `app.py`: Flask application core.
* `train_model.py`: Machine learning training script.
* `route_optimizer.py`: Dijkstra's algorithm implementation.
* `traffic_dataset.csv`: Dataset for model training.
* `traffic_model.pkl`: Serialized pre-trained model.
* `templates/`: HTML user interface files.