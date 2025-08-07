import pandas as pd
import seaborn as sns

# Load cleaned Titanic data
df = sns.load_dataset('titanic')

# Data Preprocessing
df['age'] = df['age'].fillna(df['age'].median())
df['embarked'] = df['embarked'].fillna(df['embarked'].mode()[0])
df['embark_town'] = df['embark_town'].fillna(df['embark_town'].mode()[0])
df = df.drop('deck', axis=1)
df = df.drop_duplicates()
df['family_size'] = df['sibsp'] + df['parch'] + 1

df.info()


# Exploratory Data Analysis

import matplotlib.pyplot as plt


# UNIVARIATE ANALYSIS

# Distribution of Age
sns.histplot(df['age'], bins = 15 , kde = True )
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

# Distribution of Fare
sns.histplot(df["fare"], bins = 15 , kde = True)
plt.title("Fare Distribution")
plt.xlabel("Fare")
plt.ylabel("Count")
plt.show()

# Distribution of Family Size
sns.histplot(df['family_size'],bins = 10, kde = True)
plt.title("Family Size Distribution")
plt.xlabel("Family Size")
plt.ylabel("Count")
plt.show()

# Age Distribution by Survival using Hue
sns.histplot(
    data=df, x='age', hue='survived',
    bins=30, kde=True, multiple='dodge'
)
plt.title('Age Distribution by Survival (Side-by-Side)')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()


# Survival rate based on Gender
sns.countplot( data = df, x = "sex", hue = "survived")
plt.title("Survival rate based on Gender")
plt.xlabel('Gender')
plt.ylabel("Number of Passengers")
plt.show()

# SUrvival rate of Passengers based on Class
sns.countplot(data=df, x='pclass', hue='survived')
plt.title("Survival Count by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Number of Passengers")
plt.legend(title="Survived", labels=["No", "Yes"])
plt.show()
              

print(df.groupby('family_size')['survived'].mean())


# Survival rate based on fare
sns.boxplot(data=df, x='survived', y='fare')
plt.title("Fare by Survival Status")
plt.xlabel("Survived")
plt.ylabel("Fare")
plt.show()


# Correlation Healtmap between numeric features

corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot= True, cmap = 'coolwarm')
plt.title('Numerical Features Correlation')
plt.show()

# Pairwise relatiion plot between age,fare and family size based on survival rate
sns.pairplot(df, vars=['age', 'fare', 'family_size'], hue='survived')
plt.suptitle('Pairwise Relationships Colored by Survival', y=1.02)
plt.show()

