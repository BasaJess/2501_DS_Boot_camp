[![Shipping files](https://github.com/neuefische/ds-evaluation-metrics/actions/workflows/workflow-02.yml/badge.svg?branch=main&event=workflow_dispatch)](https://github.com/neuefische/ds-evaluation-metrics/actions/workflows/workflow-02.yml)

# Evaluation Metrics for Regression and Classification


In this tutorial, we practice evaluation metrics using Python's scikit-learn. But also, you will gain a deep understanding of them by implementing some of them by yourself.

## Task

Please work together as **Pair-Programmers** through all the notebooks in this particular order:

1. [Confusion Matrix](1_Confusion_Matrix.ipynb)
2. [Classification Metrics](2_Classification_Metrics.ipynb)
3. [Regression Metrics](3_Regression_Metrics.ipynb)

## Objectives

At the end of the notebooks you should:
* know how to use scikit-learns confusion matrix, classification report and accuracy score.
* have a better understanding of different classification metrics (precision, recall, f1-score,...).
* have a better understanding of different regression metrics (MAE, MSE, R-squared).

## Set up your Environment

Please make sure you have forked the repo and set up a new virtual environment. For this purpose you can use the following commands:

The added [requirements file](requirements.txt) contains all libraries and dependencies we need to execute the Gradient Descent notebooks.

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

The data used in this notebook is saved in a `.zip` file. To unzip it, copy the block below into your terminal:

```Bash
unzip data.zip
```

*Note: If there are errors during environment setup, try removing the versions from the failing packages in the requirements file.*
