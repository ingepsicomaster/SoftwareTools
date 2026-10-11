# Delivery delay prediction and automated Slack alert system
## MapleFreight Logistics - Assessment 1 (AML 3303)
### Project overview
In this project, I address a critical operational challenge faced by MapleFreight Logistics, where on-time shipping performance dropped from 94% to 88%. As a data science analyst, I built an end-to-end machine learning pipeline to identify high-risk shipments prone to delays (**delivered_late**=1) and trigger automated alerts to Slack dispatchers before the delays occur
### Key Technical Highlights
- **Data Leakage Prevention**: I explicitly identified and dropped the **actual_transit_hours** feature because it is recorded after shipment completion. Including it would create artificial performance during training that fails in live operations
- **Class Imbalance Management**: I analyzed the target variable **delivered_late** and found that only 21% of shipments are late while 79% are on time. I mitigated this imbalance using stratified splitting (**stratify**=y) and cost-sensitive learning (**class_weight=**balanced)
- **Domain-Specific Feature Engineering**: I engineered operational features from raw data, including **scheduled_speed_kmh** to measure schedule pressure, **is_severe_weather** to capture adverse conditions, **is_winter_peak** to mark high-risk Canadian winter months, and **has_pickup_delay** to track origin delays
- **Model Evaluation**: I evaluated both a baseline Logistic Regression model and an advanced Random Forest Classifier using business-centric metrics, including Precision, Recall, F1-Score, ROC-AUC, and Confusion Matrices
- **Automated Slack Integration**: I designed a notification workflow that posts real-time JSON alert payloads to Slack webhooks whenever a shipment's predicted delay probability exceeds the defined risk threshold
### Notebook Structure and Workflow
The analysis and model development are structured across 9 sequential blocks inside 'maplefreight_delivery_delay.ipynb':
1. Block 1: Business Context and Environment Setup
   - I defined the business problem, operational context, and imported essential libraries (pandas, numpy, scikit-learn, seaborn)
2. Block 2: Data Loading and Initial Exploration
   - I loaded 'dataset.csv' / 'maplefreight_delivery_delay_dataset.csv', verified dataset dimensions, inspected data types, and checked class distribution
3. Block 3: Data Quality Exploration and Data Leakage Detection
   - I ran diagnostic checks for duplicate rows and missing values, and demonstrated the mathematical proof of data leakage in **actual_transit_hours**
4. Block 4: Data Preprocessing and Cleaning
   - I removed duplicate records, imputed missing numerical values using medians, imputed categorical missing values using modes, and dropped **actual_transit_hours**
5. Block 5: Feature Engineering
   - I created new predictors (**scheduled_speed_kmh**, **is_severe_weather**, **is_winter_peak**, **has_pickup_delay**) without introducing future data leakage
6. Block 6: Data Preparation for Machine Learning
   - I separated predictor matrix 'X' and target 'y', applied stratified train-test splitting (80/20 ratio), and fitted StandardScaler and OneHotEncoder on training data only
7. Block 7: Predictive Modeling and Model Evaluation
   - I trained a baseline Logistic Regression and a class-weighted Random Forest Classifier, evaluating F1-Score, and Confusion Matrices
8. Block 8: Model Interpretability and Automated Slack Integration
   - I extracted feature importances to explain key delay drivers and constructed the automated Slack alert dispatching module
9. Block 9: Summary and Operations Recommendations
   - I summarized actionable operational recommendations for the NorthLine and MapleFreight dispatch teams and documented data quality fixes at the source
### How to Run This Project
1. Clone or Download the Repository
   Clone the repository to your local environment
2. Set Up Environment and Dependencies
   Ensure Python 3.9+ is installed along with required packages (pandas,numpy,scikit-learn,matplotlib,seaborn,python-dotenv,requests)
3. Configure Environment Variables
   Create a .env file containing your Slack Webhook URL
4. Execute the Jupyter Notebook
   Open and run all cells sequentially in 'maplefreight_delivery_delay.ipynb'
