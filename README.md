# Bank Marketing Analysis

## Aim
The primary objective of this project is to employ predictive analysis for optimizing marketing efforts at a Portuguese banking institution. The focus is on predicting whether a client will subscribe to a term deposit, providing valuable insights for crafting targeted marketing strategies.

## Insights

### Dataset Overview
- **Rows:** 32,950
- **Columns:** 16
- **No missing values**
- Class imbalance in the target variable (89:11)

### Exploratory Data Analysis (EDA)
- Conducted an in-depth exploration of customer statistics to identify key factors influencing responses.
- Leveraged various visualizations to analyze correlations between different variables.
- Uncovered patterns related to campaign calls, duration, and their impact on subscription rates.

### Preprocessing
- Addressed missing values through strategic imputation techniques.
- Employed Label Encoding for categorical features and dropped unnecessary columns.
- Tackled class imbalance using Synthetic Minority Over-sampling Technique (SMOTE) for enhanced model performance.

### Machine Learning: Classification Models
1. **Logistic Regression**
   - Accuracy: 58.17%
   - Precision: 15.76%
   - Recall: 62.40%
   - F1 Score: 25.16%

2. **Decision Tree Classifier**
   - Accuracy: 77.70%
   - Precision: 21.28%
   - Recall: 36.25%
   - F1 Score: 26.82%

3. **Random Forest Classifier**
   - Accuracy: 82.37%
   - Precision: 29.88%
   - Recall: 41.91%
   - F1 Score: 34.89%

4. **XGBOOST Classifier**
   - Accuracy: 78.30%
   - Precision: 25.72%
   - Recall: 49.06%
   - F1 Score: 33.75%

## Conclusion
The analysis provides valuable insights into customer behavior, with actionable recommendations for crafting targeted marketing strategies. Key factors influencing subscription rates include the number of campaign calls, duration, and specific customer characteristics.

### Recommendations
1. **Optimize Campaign Calls**
   - Limit calls to avoid customer dissatisfaction.
   - Positive response likelihood declines after 3 calls.

2. **Focus on High-Duration Calls**
   - Longer calls correlate with higher positive response rates.
   - Consider tailoring marketing strategies for such calls.

3. **Utilize Machine Learning Insights**
   - Leverage machine learning models for predictive insights.
   - Implement strategies to enhance subscription rates based on model recommendations.

## How to Use
1. **Clone the Repository**
   - Clone this repository to your local machine using `git clone https://github.com/your-username/bank-marketing-analysis.git`

2. **Install Dependencies**
   - Install the required dependencies using `pip install -r requirements.txt`

3. **Execute the Code**
   - Execute the Jupyter Notebook `Bank_Marketing_Analysis.ipynb` or use the provided Python scripts for model training and prediction.

## Acknowledgments
This project was developed by [Your Name]. Feel free to collaborate and provide feedback.

