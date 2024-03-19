# Fish Weight Prediction

This project aims to predict the weight of a fish based on its physical characteristics such as length1, length2, length3, height, and width. The prediction is made using a machine learning model trained on the Fish Market dataset.

## Problem Statement

The goal of this project is to develop a machine learning model that can accurately predict the weight of a fish given its physical measurements. This can be framed as a regression problem, where the target variable is the weight of the fish, and the features are the physical characteristics of the fish.

## Dataset

The dataset used for training the model is the Fish Market dataset, which contains observations of various fish species along with their weight and physical measurements. The dataset can be found at [Fish Market Dataset](https://www.kaggle.com/aungpyaeap/fish-market).

## Model Building

The model is built using Python and scikit-learn library. Various regression algorithms such as Linear Regression, Random Forest Regressor, etc., are experimented with, and the best-performing model is selected based on evaluation metrics such as Mean Absolute Error, Mean Squared Error, and R-squared score.

## Files Included

1. `app.py`: Flask application file containing routes for serving the web application.
2. `fish_weight_predictor.pkl`: Serialized machine learning model saved using joblib.
3. `index.html`: HTML template for the input form.
4. `results.html`: HTML template for displaying prediction results.
5. `requirements.txt`: File containing required Python packages for running the Flask application.
6. `Fish.csv`: Dataset file containing fish market data.
7. `Procfile`: File specifying the commands to run the Flask application on Heroku.

