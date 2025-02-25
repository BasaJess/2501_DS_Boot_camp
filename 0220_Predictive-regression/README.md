[![Shipping files](https://github.com/neuefische/ds-predictive-regression/actions/workflows/workflow-02.yml/badge.svg?branch=main&event=workflow_dispatch)](https://github.com/neuefische/ds-predictive-regression/actions/workflows/workflow-02.yml)

# Predictive Regression

In this repo we will have a look at various topics related to working with data when training a model for prediction (vs just for exploration). When working with data we need to be aware that we never really have all the data, so we need our experiments to approximate as much as possible what the results would be if we had all the data. Our models will never be perfect, but we want them to achieve a good balance between bias and variance:
- In order to understand how the model would behave on new data, the minimum setup is doing a train/test splits before modeling. Later in the bootcamp we will learn about cross-validation. 
- When we see that our model is under-fitting (high bias), we could try to see if using various combinations of features could improve it. For this we look at polynomial feature generation.
- When we see that there is a large gap between the evaluation metric on train vs test datasets, we might experience over-fitting (high variance). I.e. our model would not generalize well on new data. One way to mitigate this is doing regularization. 
- Finally, the saying garbage in garbage out still stands, so we still want to make sure that our data is as correct as possible and adequate for the problem we are solving. For this we need to also look at outliers and investigate if they are wrong data (this needs to be fixed) or extreme values (this might a business decision if they are kept or dropped...e.g. one cannot usually afford dropping 15% of their dataset). 

In this repository we have 3 notebooks covering these topics. Although we use linear regression as an example model in these notebooks, this framework holds for any supervised modeling practice.


### The way to success:

Please work in pairs through all the notebooks in this particular order:

1. [Bias Variance Tradeoff & Polynomial Features](1_Bias_Variance_Tradeoff.ipynb)
2. [Regularizations](2_Regularization.ipynb)
3. [Detecting Outliers](3_Detecting_Outliers.ipynb)

Keep in mind, you succeed better as a team. There are NO stupid questions! If you already feel comfortable with the concepts, you might even learn more from teaching them!


## Set up your Environment

Please make sure you have forked the repo and set up a new virtual environment. For this purpose you can use the following commands:

The added [requirements file](requirements.txt) contains all libraries and dependencies we need to execute the Predictive Regression notebooks.

*Note: If there are errors during environment setup, try removing the versions from the failing packages in the requirements file. M1 shizzle.*

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
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    ```

    For `Git-Bash` CLI :
    ```
    pyenv local 3.11.3
    python -m venv .venv
    source .venv/Scripts/activate
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    ```

    **`Note:`**
    If you encounter an error when trying to run `pip install --upgrade pip`, try using the following command:
    ```Bash
    python.exe -m pip install --upgrade pip
    ```
  
