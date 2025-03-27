# Web Scraping top-up
The top-up is meant to be an hands-on session on web-scraping. 
Before starting the group warm-up in the notebook [scraping.ipynb](scraping.ipynb), follow the instructions below to setup the python environment and install the required libraries.


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
