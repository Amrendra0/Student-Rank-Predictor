# Student-Rank-Predictor

output link - https://drive.google.com/file/d/1J6hYapquG2CzkQDbSWoRCPyr2U3PJesF/view?usp=drive_link


video - https://drive.google.com/file/d/1cLYUAgZ0d4NtEXWsVd52Gyrip2QpJNvO/view?usp=drive_link


Project Overview:

The Student Rank Predictor for NEET Testline is a machine learning project aimed at predicting student ranks for the NEET exam based on their quiz performance data. The system analyzes student responses, generates insights from past NEET exam results, and predicts the rank a student may achieve in the NEET exam. Additionally, it predicts the most likely college a student could get into based on their rank.

Features:

Predicts the NEET exam rank based on quiz performance.
Generates insights from past performance data.
Bonus feature: Predicts the most likely college based on predicted rank.

Technologies Used:

Python: For data analysis and model training.
Pandas: For data manipulation and analysis.
Scikit-learn: For implementing machine learning models.
Matplotlib / Seaborn: For data visualization.

Approach-

Data Collection:

Gathered quiz performance data for students and NEET results.
The data is used to train a machine learning model for predicting the rank.

Data Preprocessing:

Cleaned and processed the data, handling missing values and outliers.
Converted categorical data to numerical format using encoding techniques.

Model Training:

Used regression models (e.g., Linear Regression, Random Forest) to predict the NEET rank.
Evaluated multiple models and selected the one with the best performance based on metrics like accuracy and RMSE (Root Mean Squared Error).

Prediction and Insights:

Developed a prediction function to estimate the rank based on quiz scores.
Analyzed trends to predict the most likely college based on predicted rank.

Visualization:

Used Matplotlib and Seaborn for visualizing the data and predictions.
