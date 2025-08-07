# Exploratory Data Analysis (EDA)

## Numeric Variable Distributions

    # Univariate Analysis:
        - Age distribution is right-skewed, with a median around 28 and a few older passengers and most of the passenger count is between 20 to 30.
        - Fare varies widely, with several high-value outliers and most of the people in the ship used low cost fare to travel.
        - Family size (derived from sibsp and parch) is mostly small and the distribution is right skewed, with most passengers traveling alone or with 1-2 family members.

    # Bivariate Analysis:
        - Overall there are only less survived than the count of those who not survived
        - Mostly childrens are survived than adults especially below the age of 10 and mostly elders are not survived after age 50
        - Survival rate is very high in female than compare to male  
        - People from first class has more survival rate than other classes and people from third class have less survival rate.
        
    # Multivariate Analysis:
        - Survival is negatively correlated with being an adult male and with lower passenger class—indicative of real Titanic outcomes (first-class women and children prioritized for lifeboats).
        - Most other correlations are weak, showing that your features are not heavily redundant (good for modeling).
        - The less the family size the more fare they spend.
        


## Categorical Variables
- Majority of passengers were 3rd class.
- Most passengers embarked at Southampton.
- Female passengers had a higher survival rate compared to males.

## Observations
- Age and fare distributions show potential outliers.
- Survival appears to correlate strongly with sex and passenger class.
- Family size could be an important feature for later analysis.
- Survival rate is not depend on Family count or individual passengers.
