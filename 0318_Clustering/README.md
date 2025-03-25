[![Shipping files](https://github.com/neuefische/ds-clustering/actions/workflows/workflow-07.yml/badge.svg?branch=main&event=workflow_dispatch)](https://github.com/neuefische/ds-clustering/actions/workflows/workflow-07.yml)

# Clustering

In this repo we will have a look at clustering.

## Task

Please work in pairs through all the notebooks in this particular order:

1. [Comparing Clustering Algorithms](1_Comparing_Clustering_Algorithms.ipynb)
2. [Clustering for Customer Segmentation](2_Clustering_for_Customer_Segmentation.ipynb)
3. [Image Clustering](3_Clustering_Images.ipynb)
4. [BONUS: Text Clustering](4_Bonus_Clustering_Texts.ipynb)

## Set up your Environment

Please make sure you have forked the repo and set up a new virtual environment. 

The added [requirements file](requirements.txt) contains all libraries and dependencies we need to execute the clustering notebooks.

*Note: If there are errors during environment setup, try removing the versions from the failing packages in the requirements file. M1 shizzle.*

### **`macOS`** type the following commands : 

make sure to install **GDAL** if you haven't done it before.

If you haven't installed it yet, begin at `step_1`. Otherwise, proceed to `step_2`.

- We have also added a [Makefile](Makefile) which has the recipe called 'setup' which will run all the commands for setting up the environment.
Feel free to check and use if you are tired of copy pasting so many commands.

     ```BASH
    make setup
    ```
    After that active your environment by following commands:
    ```BASH
    source .venv/bin/activate
    ```
Or ....

- `Step_1:` Update Homebrew and install GDAL by following commands:
    ```sh
    brew update
    brew install GDAL
    ```
  
- `Step_2:` Install the virtual environment and the required packages by following commands:

    ```BASH
    pyenv local 3.11.3
    python3 -m venv .venv
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

    For `Git-bash` CLI :
  
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
