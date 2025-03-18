[![Shipping files](https://github.com/neuefische/ds-dimensionality-reduction/actions/workflows/workflow-02.yml/badge.svg?branch=main&event=workflow_dispatch)](https://github.com/neuefische/ds-dimensionality-reduction/actions/workflows/workflow-02.yml)

# Dimensionality Reduction

In this repo we will have a look at dimensionality reduction.

## Task

Please work in pairs through all the notebooks in this particular order:

1. [Principal Component Analysis](1_Principal_Component_Analysis.ipynb)
2. [t-SNE](2_t_SNE.ipynb)
3. [PCA_in_Pipeline and SVM](3_PCA_in_Pipeline.ipynb)

In the first notebook you will see a short hands-on introduction to the principal component analysis using a sample dataset. In the solution branch you will find one solution how the first notebook could look like. In the second notebook you will find an introduction to a second dimensionality reduction algorithm: t-Distributed Stochastic Neighbor Embedding (t-SNE). And in the third notebook is a little throwback to the Support Vector Machines with an implementation of the PCA.

## Set up your Environment



### **`macOS`** type the following commands : 

- For installing the virtual environment you can either use the [Makefile](Makefile) and run `make setup` or install it manually with the following commands:

     ```BASH
    make setup
    ```
    After that active your environment by following commands:
  
    ```BASH
    source .venv/bin/activate
    ```
Or ....
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
