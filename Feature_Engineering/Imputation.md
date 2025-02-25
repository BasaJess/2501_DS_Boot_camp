FEATURE ENGINEERING

02 IMPUTATION
(Generationg Data and filling in missing Data)


1. Why do we need imputation?

1.1 Maintain Dataset Integrity

    Imputation helps restore the dataset’s completeness by providing estimates or replacements for missing values.
    Missing data reduces the amount of usable information in your dataset.
    

1.1.1. Enable Machine Learning Algorithms

    Most machine learning models (e.g., linear regression, etc) do not handle missing values and will fail to train or predict.

1.1.2. Avoid Biased Analysis

    Dropping rows or columns with missing data (listwise deletion) can introduce bias if the missingness is not random.
    Imputation minimizes data loss while retaining patterns and relationships in the data.

1.1.3. Improve Model Performance

    Missing data may disrupt model performance by making patterns and correlations harder to detect.


2. The imputation Strategy.

        If “mean”, then replace missing values using the mean along each column. Can only be used with numeric data.

        If “median”, then replace missing values using the median along each column. Can only be used with numeric data.

        If “most_frequent”, then replace missing using the most frequent value along each column. (this is the one we used in the notebook)

        If “constant”, then replace missing values with fill_value.

        If an instance of Callable (Customizing the imputation)

3. What did we do? / What was our process?

3.1. Check Missing value in sex column
   describe() / unique() / .isna().sum()

3.2. Impute a categorical column
    
    3.2.1. Calculate percentage ratio
         to get familiar with the data (not actually using this)
  
    3.2.2. Do the imputation:
         imputer = SimpleImputer(strategy='most_frequent')
   
    3.2.3. "Fitting" the imputer transformer
           Training on the column with the missing data 
           Code: imputer.fit(columns)
      
    3.2.4. Fill in the missing data based on the most frequent 
           Code: imputer.transform(columns)
    3.2.5. Change from an array to df
    3.2.6. Add the completed column back to the main df
           Code: pd_conc = df
                 pd_conc['sex'] = cols_imputed


