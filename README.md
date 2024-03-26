---
# Portuguese Bank Marketing Campaign Analysis using Machine Learning 
---
![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white) ![Jupyter Notebook](https://img.shields.io/badge/-Jupyter%20Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white) ![Pandas](https://img.shields.io/badge/-Pandas-150458?style=flat-square&logo=pandas&logoColor=white) ![Seaborn](https://img.shields.io/badge/-Seaborn-339933?style=flat-square&logo=seaborn&logoColor=white) ![Matplotlib](https://img.shields.io/badge/-Matplotlib-339933?style=flat-square&logo=matplotlib&logoColor=white) ![Scikit-learn](https://img.shields.io/badge/-Scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white) ![NumPy](https://img.shields.io/badge/-NumPy-013243?style=flat-square&logo=numpy&logoColor=white) ![Power BI](https://img.shields.io/badge/-Power%20BI-F2C811?style=flat-square&logo=powerbi&logoColor=black) ![PowerPoint](https://img.shields.io/badge/-PowerPoint-B7472A?style=flat-square&logo=microsoft-powerpoint&logoColor=white)

![image](https://github.com/hassankhan2608/PORTUGUESE-BANK-MARKETING-ANALYSIS/assets/149296407/f944911f-d6e0-475f-965d-39c787a5a874)

## Introduction

Welcome to our predictive analysis project tailored for the Banking, Financial Services, and Insurance (BFSI) sector. Our goal is to enhance customer outreach strategies by predicting responses to marketing campaigns. In the dynamic world of BFSI, understanding customer behavior is crucial. We'll explore how data-driven insights can help us optimize marketing efforts and reach out more effectively to potential clients.

Our mission is to uncover strategies that will strengthen long-term deposits and drive significant revenue growth for a Portuguese bank. We leverage a dataset named 'Bank Data Analysis' that encompasses direct marketing campaigns involving phone calls, with the aim of predicting whether a client will subscribe to a term deposit. This prediction is crucial for the bank to efficiently allocate resources and tailor its approach to potential customers.

## Understanding the Data

The dataset contains information on 32,950 existing customers contacted by a Portuguese banking institution for a term deposit campaign. It includes 16 columns, each representing different aspects of the customer and the marketing campaign.

- **Basic Statistics**: Rows: 32,950, Columns: 16
- **Key Input Variables**: Age, Job, Marital, Education, Default, Housing, Loan
- **Campaign Details**: Contact, Month, Day_of_week, Duration
- **Previous Campaign Information**: Campaign, Pdays, Previous, Poutcome
- **Outcome Variable**: 'response' (Binary variable indicating term deposit subscription: "yes" or "no")

## Ensuring Data Quality

To ensure data quality, we handled missing values, filtered the dataset to keep only rows where the 'duration' is greater than or equal to 5 seconds, renamed the 'y' column to 'response' for better clarity, and performed feature engineering tasks like changing the unit of 'duration' from seconds to minutes and creating an 'age_group' column.

## Exploratory Data Analysis

<img src="https://github.com/hassankhan2608/PORTUGUESE-BANK-MARKETING-ANALYSIS/assets/149296407/d6672bad-0a2f-46c0-86b9-089a7b407d73" alt="Response Distribution" width="500">

- The target variable ('response') distribution is highly imbalanced, with only 11% of customers subscribing to the term deposit.

---

<img src="https://github.com/hassankhan2608/PORTUGUESE-BANK-MARKETING-ANALYSIS/assets/149296407/6c677b32-d30c-41d0-a5c4-a69c000b4327" alt="Age vs Response" width="500">

- Customers aged 60+ and 20 have relatively higher positive responses compared to other age groups.
---
<img src="https://github.com/hassankhan2608/PORTUGUESE-BANK-MARKETING-ANALYSIS/assets/149296407/c1fa101f-161d-47db-8dc4-71b84f5c3f82" alt="Marital Status vs Response" width="500">

- Single customers have a higher proportion of positive responses than married or divorced customers.

---
<img src="https://github.com/hassankhan2608/PORTUGUESE-BANK-MARKETING-ANALYSIS/assets/149296407/16b97a63-8ddf-4d34-aea5-7e7f0977f0a7" alt="Job vs Response" width="500">

- Retired and student customers seem more interested in the campaign.

---
<img src="https://github.com/hassankhan2608/PORTUGUESE-BANK-MARKETING-ANALYSIS/assets/149296407/b47159e6-a4c8-4219-a584-ebed52c417a8" alt="Education vs Response" width="500">

- University degree holders had the highest number of contacts and the highest proportion of positive responses.

---
<img src="https://github.com/hassankhan2608/PORTUGUESE-BANK-MARKETING-ANALYSIS/assets/149296407/ae4fd287-9547-489a-8f4d-4982f4b46fd3" alt="Contact Type vs Response" width="500">

- Cellular contacts led to more conversions than telephonic contacts.

---
<img src="https://github.com/hassankhan2608/PORTUGUESE-BANK-MARKETING-ANALYSIS/assets/149296407/1f9bccbc-b4f9-4940-93b9-2a931c0cd69d" alt="Previous Outcome vs Response" width="500">

- Previous successful campaign outcomes resulted in higher subscription rates.

---
<img src="https://github.com/hassankhan2608/PORTUGUESE-BANK-MARKETING-ANALYSIS/assets/149296407/c7bab383-e939-476a-9688-8d59de7b6fe6" alt="Month vs Response" width="500">

- Higher subscription rates were observed in March, September, October, and December.

---
<img src="https://github.com/hassankhan2608/PORTUGUESE-BANK-MARKETING-ANALYSIS/assets/149296407/2a79904b-985d-49de-8548-63eaceff3d03" alt="Response vs Duration" width="500">

- There is a moderate positive correlation between 'response' and the duration of calls.

---
<img src="https://github.com/hassankhan2608/PORTUGUESE-BANK-MARKETING-ANALYSIS/assets/149296407/2efd5a8e-4dc8-4f95-a42d-cdfe67385fa2" alt="Duration Distribution" width="500">

* The range of duration for contacts who responded with 'yes' was larger than for contacts who responded with 'no'. This means that the contacts who said yes had more variation in their conversation length than the contacts who said no.
* The outliers in the graph indicate that there were some contacts who had very long or very short conversations, regardless of their response. These outliers may have some special characteristics or circumstances that affected their duration.

---

## Optimizing Features for Model Training

We applied label encoding to convert categorical variables into numerical values, removed the 'age_group' column, and dropped the 'duration' feature to prevent data leakage and biased predictions.

## Preparing for Model Training

We divided the dataset into independent variables (X) and the dependent variable (y), split the data into training and testing sets (80% for training, 20% for testing), and applied the SMOTE technique to address class imbalance in the training set.

## Choosing the Right Model
![image](https://github.com/hassankhan2608/PORTUGUESE-BANK-MARKETING-ANALYSIS/assets/149296407/4cfdf5d2-4944-41e8-befc-5f28193f95a4)
After evaluating various models, including Logistic Regression, Decision Tree Classifier, Random Forest Classifier, and XGBoost Classifier, the Random Forest Classifier emerged as the top-performing algorithm for our Term Deposit Prediction. It achieved the highest accuracy, precision, recall, and F1-score, demonstrating its robustness and effectiveness in handling the complexities of our dataset.

## Deeper Insights into Random Forest Model

The Random Forest model showcased exceptional predictive power, with a precision of 92% for Class 0 (identifying clients who decline the term deposit) and a recall of 88% for Class 0 (accurately predicting clients who actually say "no" out of all clients who declined the offer).

## Conclusion

Our analysis provided valuable insights into customer behavior and preferences, including the impact of factors like education level, marital status, loan status, previous campaign outcomes, and contact channels on subscription rates. The Random Forest model proved well-suited for predicting customer responses to the term deposit campaign, providing a reliable tool for optimizing marketing efforts and targeting the most responsive clients.

## Recommendations

Based on the analysis, we recommend:

1. Target marketing efforts on specific customer segments with a higher likelihood of subscribing (e.g., university degree holders, single individuals, those without existing housing or personal loans).
2. Optimize contact strategy based on the success of previous campaigns, potentially re-engaging clients with successful outcomes.
3. Adjust the timing of the telemarketing campaign to coincide with periods when subscription rates tend to be higher.
4. Leverage the Random Forest classification model to predict customer responses before initiating the campaign.
5. Prioritize cellular communication over telephonic channels, as cellular contacts showed higher conversion rates.
6. Continuously monitor and update the predictive model to adapt to changing customer behaviors and preferences.

By incorporating these recommendations, the company can optimize its marketing strategy, increase the efficiency of its telemarketing campaigns, and ultimately enhance the success rate of term deposit subscriptions.

## Acknowledgments
This project was developed by Mohd Hassan Khan. Feel free to collaborate and provide feedback.

