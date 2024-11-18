# Real-Time Stock Price Prediction

This project is a **Real-Time Stock Price Prediction** application that uses an LSTM (Long Short-Term Memory) model to predict stock prices. The backend is implemented using **Flask**, and it fetches recent stock data from Yahoo Finance to make predictions.

## Table of Contents

- [Project Overview](#project-overview)

- [Features](#features)

- [Installation](#installation)

- [Usage](#usage)

- [API Endpoints](#api-endpoints)

- [Folder Structure](#folder-structure)

- [Technologies Used](#technologies-used)

- [Future Improvements](#future-improvements)

- [Contributing](#contributing)


---

## Project Overview

The goal of this project is to predict the next day's closing stock price for a specified stock ticker using a machine learning model trained on past stock price data. The model is an LSTM neural network, suitable for time series forecasting. The application fetches the latest stock data from Yahoo Finance, scales it, and uses the trained model to make a prediction. The project is structured as a REST API with a Flask backend.

## Features

- Fetches real-time stock data using the Yahoo Finance API.

- Uses an LSTM model to predict the next day's stock price.

- Provides an API endpoint to get predictions for any specified stock ticker.

- Scalable and modular, making it easy to extend with other machine learning models or front-end applications.

---

## Installation

### Prerequisites

- Python 3.7 or higher

- [Git](https://git-scm.com/)

- A virtual environment setup (recommended)

- [Flask](https://flask.palletsprojects.com/)

- [TensorFlow](https://www.tensorflow.org/)

### Steps

1\. **Clone the repository**:

   ```bash

   git clone https://github.com/avirooppal/RealTimeStock-DSA.git

   cd your-repository-name

   ```

2\. **Create and activate a virtual environment**:

   ```bash

   python -m venv venv

   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

   ```

3\. **Install dependencies**:

   ```bash

   pip install -r requirements.txt

   ```

4\. **Place the trained model**:

   - Ensure the `stock_price_prediction_model.h5` model file is saved in the `model` directory.

   - If you don't have the model file, follow the steps in the [Training the Model](#training-the-model) section.

5\. **Run the Flask application**:

   ```bash

   cd backend

   python backend.py

   ```

6\. **Access the API**:

   The Flask app will run on `http://127.0.0.1:5000` by default.

---

## Usage

After starting the Flask server, you can make predictions using a `POST` request to the `/predict` endpoint.

### Example Request with cURL

```bash

curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{"ticker": "AAPL"}'

```

This will return a JSON response with the predicted stock price for the specified ticker.

---

## API Endpoints

### `POST /predict`

- **Description**: Predicts the next day's closing price for a given stock ticker.

- **Request Parameters**:

  - `ticker` (string): The stock ticker symbol (e.g., "AAPL" for Apple).

- **Response**:

  - `ticker` (string): The stock ticker symbol provided.

  - `predicted_price` (float): The predicted closing price for the next day.

#### Example Request Payload

```json

{

    "ticker": "AAPL"

}

```

#### Example Response Payload

```json

{

    "ticker": "AAPL",

    "predicted_price": 226.15

}

```

---

## Folder Structure

```plaintext

your-repository-name/

├── model/

│   └── stock_price_prediction_model.h5       # Trained LSTM model

├── backend/

│   └── backend.py                            # Flask backend code

├── README.md                                 # Project documentation

├── requirements.txt                          # Python dependencies

└── request.py                                # Sample script to test API

```

---

## Technologies Used

- **Python**: Programming language.

- **Flask**: Web framework for creating the REST API.

- **TensorFlow**: Deep learning library used to build the LSTM model.

- **Yahoo Finance API**: Used to fetch historical stock data.

- **scikit-learn**: Provides data scaling functionality.

---

## Training the Model

If you don't already have the `stock_price_prediction_model.h5` model file, you can train your own LSTM model with historical stock data.

1\. **Collect historical data**: Download historical stock data (e.g., using `yfinance`).

2\. **Preprocess the data**: Scale the stock prices and structure the data for LSTM input.

3\. **Train the model**: Build and train an LSTM model using `TensorFlow` or `Keras`.

4\. **Save the model**: Save the trained model as `stock_price_prediction_model.h5` in the `model` directory.

For detailed steps on training, refer to the [TensorFlow documentation](https://www.tensorflow.org/).

---

## Future Improvements

- **Add more stock indicators**: Incorporate additional features such as moving averages, RSI, and volume data.

- **Build a front-end**: Create a web or mobile front-end to display predictions.

- **Use more advanced models**: Experiment with other models like GRU, ARIMA, or Prophet.

- **Real-time updating**: Integrate real-time stock data for continuous predictions.

---

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request.

1\. Fork the project

2\. Create your feature branch (`git checkout -b feature/YourFeature`)

3\. Commit your changes (`git commit -m 'Add some feature'`)

4\. Push to the branch (`git push origin feature/YourFeature`)

5\. Open a pull request

---




### Additional Notes

- Update `https://github.com/avirooppal/RealTimeStock.git` with your actual GitHub repository URL.

- Update `"avirooppal42@gmail.com"` with your contact email if you want people to reach you.

