# Updated app.py
from flask import Flask, render_template, request
import joblib
# Ensure route_optimizer.py is in the same directory as app.py
from route_optimizer import get_optimized_route 

app = Flask(__name__)

# Load the pre-trained machine learning model
model = joblib.load("traffic_model.pkl")

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    route_nodes = None
    
    if request.method == 'POST':
        # 1. Retrieve user inputs from the web form
        time = float(request.form['time'])
        weather = float(request.form['weather'])
        vehicle_count = float(request.form['vehicle_count'])
        
        # 2. Predict the traffic congestion level (e.g., "Low", "Medium", "High")
        # The model uses: [Time, Weather, Vehicle Density]
        prediction_result = model.predict([[time, weather, vehicle_count]])
        prediction = prediction_result[0] 
        
        # 3. Calculate the optimized route based on the prediction
        # The function returns a list of intersection/road nodes
        route_nodes = get_optimized_route(prediction)
        
    # Render the template and pass data to index.html
    return render_template('index.html', prediction=prediction, route=route_nodes)

if __name__ == '__main__':
    # Run the Flask development server
    app.run(debug=True)