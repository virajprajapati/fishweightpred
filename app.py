from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

# Load the model
model = joblib.load('fish_weight_predictor.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [float(x) for x in request.form.values()]
    final_features = [features]
    prediction = model.predict(final_features)
    
    output = round(prediction[0], 2)
    
    return render_template('results.html', prediction=output)

if __name__ == "__main__":
    app.run(debug=True)
