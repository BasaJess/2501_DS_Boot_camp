# Feature Engineering

This is a collection guided topup lessons as well as exercise notebooks 
on Feature Engineering. In supervised machine learning and statistical modeling, Feature Engineering is a preprocessing step which transforms raw data into
features that more precisely represent the underlying problem for a predictive model. This is often achieved by means of applying domain knowledge to data.

## Contents

### 1. lessons_feature_engineering
- Notebook ***1_intro_to_fe*** covers the basics of feature engineering, with hands-on example from a given dataset, explaining various techniques like
    + `Imputation`
    + `Categorical Encoding`
    + `Feature Scaling`
    + `Feature Expansion` 
- Notebook ***2_advanced_fe*** is dedicated to various advanced technologies used in a Machine Learning workflow, namely 
    + `make_column_transformer`
    + `make_pipeline`


### 2. _exercises_feature_engineering_
- Notebook ***3_intro_to_fe_continued*** suppliments and serves as a continuation of notebook *1_intro_to fe*. It covers some examples of
    + `Imputation`
    + `Categorical Encoding`
    + `Feature Scaling`
    + `Discretization`
- Notebook ***4_advanced_fe_continued*** continues with some even more advanced technologies in a Machine Learning workflow: 
    + `ColumnTransformer`
    + `Pipeline`
- Notebook ***5_bike_sharing*** is a semi-guided open-ended mini project on its own right, where the reader will recollect some of the already-introduced concepts. 

## Set up your Environment

The added [requirements file](requirements.txt) contains all libraries and dependencies we need to execute the notebooks.

### **`macOS`** type the following commands : 

- Install the virtual environment and the required packages by following commands:

    ```BASH
    pyenv local 3.11.3
    python -m venv .venv
    source .venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
    ```
### **`WindowsOS`** type the following commands :

- Install the virtual environment and the required packages by following commands.

   For `PowerShell` CLI :

    ```PowerShell
    pyenv local 3.11.3
    python -m venv .venv
    .venv\Scripts\Activate.ps1
    pip install --upgrade pip
    pip install -r requirements.txt
    ```

    For `Git-Bash` CLI :
    ```
    pyenv local 3.11.3
    python -m venv .venv
    source .venv/Scripts/activate
    pip install --upgrade pip
    pip install -r requirements.txt
    ```


*Note: If there are errors during environment setup, try removing the versions from the failing packages in the requirements file.*

