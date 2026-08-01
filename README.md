🚗 CarDekho Used Car Price Predictor

👩‍💻 Participant Name

Anusree M S

🆔 MUID

anusree-5@mulearn

📘 Project Overview

This project predicts the selling price of used cars using the CarDekho dataset.
A Random Forest Regressor model was trained on historical car data (year, fuel type, transmission, etc.) to estimate resale value.
The trained model was integrated into a Streamlit web application, allowing users to input car details and instantly view predicted prices.


🌐 Deployment Approach

Developed and tested in Google Colab.
Model saved as model.pkl using joblib.
Streamlit app built (app.py) and deployed publicly via Streamlit Community Cloud.
Alternative testing done using LocalTunnel in Colab for live preview.

🔍 Key Observations

Random Forest performed better than Linear Regression, achieving higher R² score.
Price strongly correlates with Year and Present Price.
Encoding categorical features consistently between training and deployment is crucial.

⚙️ Challenges Faced

Column name mismatches in dataset (Fuel_Type vs fueltype) caused preprocessing errors.
Handling categorical encoding during prediction required careful mapping.
Initial Streamlit deployment failed due to missing dependencies in requirements.txt.

🚀 Future Improvements

Add brand and mileage features for more accurate predictions.
Enhance UI with charts and visual insights.
Deploy on Render or Hugging Face Spaces for faster load times.
Integrate model retraining option for updated datasets.

Deployment link -- https://cardekho-used-car-price-predictor-c4n4n5pbbow4tmna68xzp4.streamlit.app/
