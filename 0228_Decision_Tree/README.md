[![Shipping files](https://github.com/neuefische/ds-decision-tree/actions/workflows/workflow-02.yml/badge.svg?branch=main&event=workflow_dispatch)](https://github.com/neuefische/ds-decision-tree/actions/workflows/workflow-02.yml)

# Decision Trees

In this repository we learn about the Machine Learning Algorithm
 called Decision Tree in Python. 

## The way to success:

Please work together as **Pair-Programmers** through all the notebooks
in this particular order:

1. [Decision Trees Regression](1_Decision_Trees_Visualization.ipynb)
2. [Decision Trees Classification](2_Decision_Trees_Classification.ipynb)
3. [Decision Trees Recap](3_Decision_Trees_Recap.ipynb)

The first notebook will show you how to implement
Decision Trees on a regression problem with scikit-learn. 
In the second notebook, you will use the algorithm on a classification problem.
In the third notebook you can recap everything you have learnt so far about Decision Trees and get a deeper insight into a decision tree algorithm implemented in Python with the help of a blog post.

## Objectives

At the end of the notebooks you should:

- know how to implement Decision Trees (both classifier and regressor Trees) with scikit-learn.
- know how to plot Decision Trees.
- know about the different splitting criterions for Decision Trees (Gini and Entropy) and how splitting decisions are made while growing the tree.
- be able to shortly explain the Decision Tree Algorithm to a colleague.
- know of the Advantages and Disadvantages of Decision Trees.
- be able to understand typical Terminology (node, stump, leaf, threshold).
- have gotten a small recap on how to write and document functions (regarding length and using doc strings)
- have gotten a recap on the different steps during a ML project.

## Set up your Environment

Please make sure you have forked the repo and set up a new virtual environment. For this purpose you can use the following commands:

The added [requirements file](requirements.txt) contains all libraries and dependencies we need to execute the Decision Trees notebooks.

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
  
    ```BASH
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

## Data

The dataset for the notebook is stored in the `data.zip` folder. To unzip the data folder directly in the terminal run

```sh
unzip data.zip
```
