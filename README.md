# YouTube---Content-Monetization-Modeler

Content Monetization Modeler
Project Overview
To create the Content Monetization Modeler, we received basic input data including:
video_id, date,views, likes, comments, watch_time_minutes, video_length_minutes,
subscribers, category, device, country, ad_revenue_usd and ad_revenue_usd is our target column
Since we have both input and output data, this is a supervised machine learning problem. And because our target is a numeric value, it falls under regression type modeling.
Data Preparation
There were some duplicate rows and missing values in columns like likes, comments, and watch_time_minutes. These needed to be cleaned. We also added useful features such as engagement_rate, watch_per_view..
These help make the prediction more informative and detailed.
It was also important to check for outliers, as they can mislead the model during training. We need to handle outliers using statistical methods and if needed some simple rules in streamlit calculation.
Since machine learning models work with numeric data, we need to consider encoding techniques to convert categorical columns like category, device, and country into numeric format.
Model Training
We need to train several regression models:
Linear Regression, Ridge Regression, Decision Tree Regressor, Random Forest Regressor, XGBoost Regressor
To evaluate model performance, we used:
R square Score - how well the model fits the data
RMSE - Root Mean Squared Error (average prediction error)
MAE- Mean Absolute Error (average absolute difference between predicted and actual values)
Based on these results, we can select the best-performing model for deployment.
Streamlit Web App
The web page needs to be  designed as beginner-friendly, allowing users to enter the inputs that were used during model training. Any internal calculations (like derived features) are to be handled behind the scenes, so users only need to provide the basic inputs.
The saved model expects the same number and format of inputs as used during training, ensuring consistent and accurate predictions.
Future Scope
We can plan to expand the prediction logic to support other content platforms such as Instagram Reels, Telegram Channels, Facebook Video
Nowadays, video views and monetization happen across multiple platforms — not just YouTube. This extension will help creators estimate revenue across different ecosystems.


