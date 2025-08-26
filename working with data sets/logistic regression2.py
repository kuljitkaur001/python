# Step 1: Import Required Libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Step 2: Load the Dataset
ed = pd.read_csv("C:\\Users\\hp\\OneDrive\\python\\python\\working with data sets\\fifa_eda.csv")

# Step 3: Drop rows with missing values in important columns
ed = ed.dropna(subset=['Value', 'Age', 'Overall', 'Potential', 'Wage', 'Skill Moves', 'International Reputation'])

# Step 4: Create a binary target column (1 = High Value, 0 = Not High Value)
ed['HighValue'] = ed['Value'].apply(lambda x: 1 if x > 100000 else 0)

# Step 5: Select Features and Target
X = ed[['Age', 'Overall', 'Potential', 'Wage', 'Skill Moves', 'International Reputation']]
y = ed['HighValue']

# Step 6: Split the Data into Train and Test Sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 7: Create and Train the Logistic Regression Model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Step 8: Make Predictions on the Test Set
y_pred = model.predict(X_test)

# Step 9: Evaluate the Model
print(" Accuracy:", accuracy_score(y_test, y_pred))
print("\n Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
