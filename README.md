# House Price Prediction

This project predicts house prices based on various features such as location, size, number of bathrooms, and BHK. The model is trained using scikit-learn, and the prediction interface is built using Streamlit.

## Features

- Train a machine learning model to predict house prices.
- Save the trained model as a pickle file.
- Build a Streamlit app to interactively predict house prices.

## Dataset

### Initial Dataset Features

The original dataset contains the following features:

- `area_type`: Type of the area (e.g., Super Built-up Area, Plot Area, etc.)
- `availability`: Availability status of the property (e.g., Ready To Move, Immediate Possession, etc.)
- `location`: The location of the house.
- `size`: Size of the house (e.g., 2 BHK, 4 Bedroom, etc.)
- `society`: Name of the society.
- `total_sqft`: Total area in square feet.
- `bath`: Number of bathrooms.
- `balcony`: Number of balconies.
- `price`: Price of the house.

### Processed Dataset Features

After data cleaning and feature engineering, the dataset is refined to the following essential features for predicting house prices:

- `location`: The location of the house.
- `size`: The size of the house in square feet.
- `bath`: The number of bathrooms.
- `bhk`: The number of balconies.

#### For downloding dataset:
- https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data/data

## Model

### Linear Regression

The model used for predicting house prices is a Linear Regression model. Linear Regression is a simple and interpretable model that assumes a linear relationship between the input features and the target variable (house price). It works well for this problem as it allows us to understand the influence of each feature on the house price.

### Pipeline

A machine learning pipeline is used to streamline the workflow of preprocessing the data and training the model. The pipeline includes:

1. **Column Transformer**:
   - **OneHotEncoder**: Encodes categorical features (`location`) into a format that can be provided to the model.
   - **Passthrough**: Numeric features (`size`, `bath`, `bhk`) are passed through without changes.

2. **StandardScaler**: Standardizes the numeric features by removing the mean and scaling to unit variance, ensuring that the features are on a similar scale.

3. **Linear Regression**: The final step in the pipeline is the Linear Regression model, which is trained on the processed data.

The use of a pipeline ensures that all steps are executed in the correct order and makes it easy to reuse the entire workflow on new data.

## Requirements

- Python 3.6+
- pandas
- scikit-learn
- streamlit

You can install the required packages using the following command:

```bash
pip install pandas scikit-learn streamlit

```


## Screenshots

![App Screenshot]([https://via.placeholder.com/468x300?text=App+Screenshot+Here](https://github.com/jeetml/PRODIGY_ML_01/blob/main/houseprice.png))



## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jeet-patel-30757b2a2/)

[![Github](https://img.shields.io/badge/github-0A66C2?style=for-the-badge&logo=github&logoColor=white)](https://github.com/jeetml)





