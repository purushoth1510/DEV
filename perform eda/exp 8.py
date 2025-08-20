import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic wine data
data = {
    'fixed acidity': np.random.uniform(5, 15, 100),
    'volatile acidity': np.random.uniform(0.1, 1.5, 100),
    'citric acid': np.random.uniform(0, 1, 100),
    'residual sugar': np.random.uniform(0, 10, 100),
    'alcohol': np.random.uniform(8, 15, 100),
    'quality': np.random.randint(1, 11, 100)
}

# Create DataFrame
wine_df = pd.DataFrame(data)

# Save to CSV
wine_df.to_csv('wine_quality_dataset.csv', index=False)

# Load the dataset
wine_df = pd.read_csv('wine_quality_dataset.csv')

# Basic data info
print(wine_df.info())
print(wine_df.describe())
print(wine_df.isnull().sum())

# Countplot for wine quality
sns.countplot(x='quality', data=wine_df)
plt.title('Distribution of Wine Quality')
plt.xlabel('Quality')
plt.ylabel('Count')
plt.show()

# Correlation heatmap
correlation_matrix = wine_df.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.show()

# Pairplot of selected features
selected_features = ['alcohol', 'volatile acidity', 'citric acid', 'residual sugar', 'quality']
sns.pairplot(wine_df[selected_features], hue='quality', palette='Set2')
plt.suptitle('Pairplot of Selected Features', y=1.02)
plt.show()

# Boxplot of alcohol by quality
plt.figure(figsize=(10, 6))
sns.boxplot(x='quality', y='alcohol', data=wine_df)
plt.title('Boxplot of Alcohol Content by Wine Quality')
plt.xlabel('Quality')
plt.ylabel('Alcohol')
plt.show()
