document.getElementById('predictionForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const ticker = document.getElementById('tickerInput').value.trim();
    const resultDiv = document.getElementById('result');

    if (ticker) {
        // Display loading text
        resultDiv.textContent = "Predicting...";

        // Send POST request to Flask backend
        fetch('http://127.0.0.1:5000/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ ticker: ticker })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error("Network response was not ok");
            }
            return response.json();
        })
        .then(data => {
            // Display the predicted price
            if (data.predicted_price) {
                resultDiv.textContent = `Predicted Price for ${ticker}: $${data.predicted_price.toFixed(2)}`;
            } else {
                resultDiv.textContent = "Prediction error: " + (data.error || "Unknown error");
            }
        })
        .catch(error => {
            resultDiv.textContent = "An error occurred: " + error.message;
        });
    }
});
