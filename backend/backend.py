from flask import Flask, request, jsonify, render_template
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import yfinance as yf
import os

app = Flask(_name_, static_folder='../frontend/static', template_folder='../frontend')

# Load model and scaler setup as before
model_path = os.path.join("..", "model", "stock_price_prediction_model.h5")
model = load_model(model_path)
scaler = MinMaxScaler(feature_range=(0, 1))

@app.route('/')
def home():
    return render_template('index.html')

# Function to fetch recent stock data and preprocess it
def fetch_recent_data(ticker, window_size=60):
    """
    Fetches the recent stock data for a given ticker symbol from Yahoo Finance.
    This function gets the last 3 months of data to ensure we have enough data points.
    It also checks if enough data points are available and scales the data for model compatibility.

    Args:
        ticker (str): The stock ticker symbol (e.g., 'AAPL').
        window_size (int): The number of past days used as input for prediction.

    Returns:
        tuple: A tuple containing:
            - scaled_data (np.array): Scaled stock prices for model input.
            - stock_data (np.array): Original (unscaled) stock prices for reference.
    """
    # Download the stock data for the last 3 months
    stock_data = yf.download(ticker, period="3mo", interval="1d")
    
    # Raise an error if no data is found for the ticker
    if stock_data.empty:
        raise ValueError(f"No data found for ticker symbol: {ticker}")

    # Extract the 'Close' price and keep the last window_size days
    stock_data = stock_data[['Close']].dropna().values[-window_size:]
    
    # Check if there are enough data points for prediction
    if stock_data.shape[0] < window_size:
        raise ValueError(f"Not enough data to make predictions for {ticker}. Need at least {window_size} data points.")
    
    # Scale the data to the range (0, 1) to match model requirements
    scaled_data = scaler.fit_transform(stock_data)
    return scaled_data, stock_data  # Return both scaled and original prices

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    """
    Predicts the next day's stock price based on the last 60 days of stock data.
    Expects a JSON POST request with the 'ticker' key specifying the stock symbol.
    Returns the predicted price in JSON format.

    Example request payload:
    {
        "ticker": "AAPL"
    }

    Example response payload:
    {
        "ticker": "AAPL",
        "predicted_price": 123.45
    }
    """
    # Check if the Content-Type header is set to JSON
    if request.content_type != 'application/json':
        return jsonify({"error": "Content-Type must be application/json"}), 415
    
    try:
        # Parse the JSON request body to get the ticker symbol
        data = request.json
        ticker = data.get("ticker", "AAPL")  # Default to AAPL if ticker not provided

        # Fetch and preprocess the recent stock data for the ticker
        recent_data_scaled, recent_data_unscaled = fetch_recent_data(ticker)

        # Reshape the data to match the model's expected input shape (1, window_size, 1)
        X_recent = np.reshape(recent_data_scaled, (1, recent_data_scaled.shape[0], 1))

        # Use the model to predict the next day's scaled price
        predicted_price_scaled = model.predict(X_recent)

        # Inverse transform the predicted price to get it back to the original scale
        predicted_price = scaler.inverse_transform(predicted_price_scaled)[0, 0]  # Extract the scalar value

        # Prepare the JSON response with the predicted price
        response = {
            "ticker": ticker,
            "predicted_price": float(predicted_price)  # Convert to standard float for JSON serialization
        }
        return jsonify(response)
    
    except ValueError as e:
        # Handle errors related to fetching and processing stock data
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

# Run the app
if _name_ == '_main_':
    # Start the Flask development server
    app.run(debug=True)