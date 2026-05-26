import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load dataset
df = pd.read_csv("data.csv")
# Show first 5 rows
print(df.head())
# Check missing values
print(df.isnull().sum())
# Remove missing values
df = df.dropna()
# Remove duplicate rows
df = df.drop_duplicates()
# Show dataset information
print(df.info())
# Basic statistics
print(df.describe())
# Example Visualization
plt.figure(figsize=(8,5))
# Replace column names with your dataset columns
sns.countplot(x=df.iloc[:,0])
plt.title("Data Visualization")
plt.xticks(rotation=45)
plt.show()