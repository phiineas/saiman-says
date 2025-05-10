# Saiman Says - YouTube Statistics Analysis and Prediction

This project analyzes a YouTube statistics dataset to predict video views. It involves data preprocessing, feature engineering, model training, and evaluation. The best performing model is a tuned Random Forest Regressor.

## Project Overview

The primary goal of this project is to build a machine learning model that can accurately predict the number of views a YouTube video might receive based on various features of the channel and video.

## Dataset

The project uses the `youtube-statistics.csv` dataset. This dataset contains various statistics about YouTube channels.

## Project Steps

The project follows these key steps, as implemented in the [`flask_app/saiman_says.ipynb`](flask_app\saiman_says.ipynb) notebook:

1.  **Data Loading and Exploration:** The dataset is loaded using pandas and initial exploratory data analysis is performed.
2.  **Handling Missing Values:** Missing numerical values are imputed using the median, and missing categorical values are imputed using the mode.
3.  **Feature Engineering:** A new feature, `views_per_upload`, is created by dividing `video views` by `uploads`.
4.  **Outlier Handling:** Outliers in numerical columns are handled using the IQR method.
5.  **Feature Selection:** A correlation matrix is used to identify features highly correlated with `video views`.
6.  **Encoding Non-Numeric Features:** Categorical features are encoded using `LabelEncoder`.
7.  **Data Preparation for Modeling:**
    *   The data is split into training and testing sets.
    *   Features are scaled using `StandardScaler`.
8.  **Model Building and Evaluation:** Several regression models are trained and evaluated:
    *   Linear Regression
    *   Lasso Regression
    *   Ridge Regression
    *   Decision Tree Regressor
    *   Random Forest Regressor
    The models are evaluated based on Mean Squared Error (MSE) and R2 Score.
9.  **Hyperparameter Tuning:** `GridSearchCV` is used to find the optimal hyperparameters for the Random Forest Regressor.
10. **Results Comparison:** The performance of all models, including the tuned Random Forest, is compared.
11. **Saving Artifacts:**
    *   The predictions from the best model are saved to `./model/predictions.json`.
    *   The trained `StandardScaler` is saved to `./model/scaler.pkl`.
    *   The best performing model (tuned Random Forest) is saved to `./model/best_rf.pkl`.

## Models Used

*   Linear Regression
*   Lasso Regression
*   Ridge Regression
*   Decision Tree Regressor
*   Random Forest Regressor (with hyperparameter tuning)

## How to Run

1.  Ensure you have Python installed.
2.  **Create and activate a virtual environment:**
    *   On Windows:
        ```bash
        python -m venv .venv
        .\.venv\Scripts\activate
        ```
    *   On macOS/Linux:
        ```bash
        python3 -m venv .venv
        source .venv/bin/activate
        ```
3.  Install the required libraries:
    ```bash
    pip install pandas numpy matplotlib seaborn scikit-learn jupyter
    ```
4.  Place the `youtube-statistics.csv` file in the same directory as the notebook or update the `file_path` variable in the notebook.
5.  Open and run the [`flask_app/saiman_says.ipynb`](flask_app\saiman_says.ipynb) notebook in a Jupyter environment.

## Saved Artifacts

The following files are generated and saved in the `./model/` directory:

*   `predictions.json`: Predictions made by the final tuned Random Forest model on the test set.
*   `best_rf.pkl`: The trained and tuned Random Forest Regressor model.
*   `scaler.pkl`: The `StandardScaler` object used for feature scaling.
