[![Shipping files](https://github.com/neuefische/ds-visualisation/actions/workflows/workflow-03.yml/badge.svg?branch=main&event=workflow_dispatch)](https://github.com/neuefische/ds-visualisation/actions/workflows/workflow-03.yml)
# Visualisations with Python

In this repository we will have a look at visualisations with Python.

## Data

The dataset used for this exercise comes from the 2020 Kaggle survey. We will only use a subset of the data. If you need further information about the survey or the data you will find two PDF files in this repo that may help you.

We created a SQL Database that contains the data. In the [first notebook (Fetching_the_data)](1_Fetching_the_data.ipynb) you will see how to fetch the data and save it in a csv file.

## Task

Your task for today is to create specific plots which meet the requirements of your stakeholder. You will find a extensive description of the task in the [Visualisation_Exercise](2_Visualisation_Exercise.ipynb) notebook.

Create the visualizations with 3 libraries, at least one plot with each:

- matplotlib
- seaborn
- plotly

## Set up your Environment
This repo contains a requirements.txt file with a list of all the packages and dependencies you will need. Before you install the virtual environment. Before you can start with plotly in Jupyter Lab you have to install node.js (if you haven't done it before).
- Check **Node version**  by run the following commands:
    ```sh
    node -v
    ```
    If you haven't installed it yet, begin at `step_1`. Otherwise, proceed to `step_2`.


### **`macOS`** type the following commands : 

- `Step_1:` Update Homebrew and install Node by following commands:
    ```sh
    brew update
    brew install node
    ```

- `Step_2:` Install the virtual environment and the required packages by following commands:

    ```BASH
    pyenv local 3.11.3
    python -m venv .venv
    source .venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
    ```
### **`WindowsOS`** type the following commands :

- `Step_1:` Update Chocolatey and install Node by following commands:
    ```sh
    choco upgrade chocolatey
    choco install nodejs
    ```

- `Step_2:` Install the virtual environment and the required packages by following commands.

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

At the end of this exercise you should:

- be more familiar with the basic usage of different plotting libraries
- be able to create plots which convey certain information
