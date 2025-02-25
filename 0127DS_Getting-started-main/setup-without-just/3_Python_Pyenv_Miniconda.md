# Python, pyenv and the wonderful world of virtual environments

- [Pyenv](#install-pyenv)
- [Python](#install-python-versions)
- [Virtual environments](#install-your-first-virtual-environment)
- [Pyenv and venv](#Creating-virtual-environments-with-pyenv-and-venv)
- [Miniconda](#Creating-virtual-environments-with-miniconda)
- [Troubleshooting](#Troubleshooting)

If you open the terminal and run the command `python --version` you will see that Python is already installed as part of the operating system. The default Python version installed on your Mac is 2.7. 
But the world has moved on and working in Data Science nowadays usually requires the use of Python 3. 
Actually you might want (or have) to use different Python 3 version for different projects. There are several tools available to help you with this task. During the bootcamp we will use pyenv and virtual environments to install, organize and manage different versions of Python (and other libraries) on your computer.

You can think of this as if you were planning on going biking: for biking in the city you need a city bike maybe with a bike basket and a fluffy seat. For going mountain biking you will need a mountain bike with mud flaps, no bike basket and you might also need a proper helmet with professional glasses. This is similar to working on different data science projects... for some you will need basic python libraries... for others you will need more advanced ones and sometimes they will only work with specific versions (if you wear a bike helmet in the city it will be a different one you need for mountain biking)


## Install pyenv

[Pyenv](https://github.com/pyenv/pyenv) is a simple Python version management tool you can download for free using homebrew. 

```sh
brew update
brew install openssl readline sqlite3 xz zlib
brew install pyenv
```

After you installed pyenv you need to add another line to the .zshrc file. Open the file and add the second line somewhere nearly at the bottom of the file: 

```sh 
nano ~/.zshrc
```
```sh
eval "$(pyenv init --path)"
```
Save and exit the text editor. In nano, you can do this by pressing **Ctrl + O**, then Enter, and then **Ctrl + X** to exit.

```sh
# run this command in order to activate the changes to your profile in this terminal
source ~/.zshrc
```

There are several advantages for using a tool like pyenv. It allows you to easily download or switch between Python versions with a single command. You can also set the Python version of your choice as the global one. 
It even makes it possible to switch Python versions by changing the directory. This proves to be particularly useful when you have different directories for projects which require different versions of Python. 

## Install Python versions

After you installed pyenv you can easily install different Python versions. If you want to see a list of all available versions and flavors you can use the following command:

```sh 
pyenv install --list
```


For the bootcamp we will use Python 3.11.3. You can install it with:

```sh
pyenv install 3.11.3     
```

To set a specific version as the local (inside a directory) or global (everywhere) Python version you can use:

```sh
pyenv local 3.11.3
pyenv global 3.11.3
```


## Install your first virtual environment

Working on a Data Science project does not only require Python. Most of the time it will also involve a bunch of different packages and modules, which exist in different versions as well. You might work on project A which uses version 1.0 of a particular package and on the same time on project B which requires version 2.0 of the same package. The solution for avoiding a conflict and fulfilling both requirements is using virtual environments. It basically works like a magician pulling a rabbit out of a hat. When you no longer need the virtual environment - your rabbit - you put it back into the hat and conjure up a new, different environment.

![Abracadabra!](https://media4.giphy.com/media/l41lPv1RcGVE1q5mo/giphy.gif)


A virtual environment is a self-contained directory tree containing a Python installation of the version of your choice and a number of additional packages, which are all isolated from other environments. So each project you are working on should have its own virtual environment. Another advantage of using virtual environments is that if you want to share your project with someone else they can install an identical copy of your environment to make sure everything will work.   

There are different approaches on how to manage various virtual environments. We will introduce two different ways of creating those environments at this point. 

### Creating virtual environments with pyenv and [venv](https://docs.python.org/3/tutorial/venv.html) 

One way of creating virtual environments is to use the module `venv`. First of all move to the directory for which you want to create the virtual environment. Make sure you use the desired Python version either locally in this directory or globally (you can check the Python version either with `python --version` or `which python`). To set the local Python version and create a new environment you can use the following commands:

```sh
pyenv local 3.11.3
python -m venv .venv
```

It will create a new hidden folder called `.venv` to store all necessary files inside the directory. You could also replace .venv with a whole path where you want to save your environment. But we want to create our virtual environments inside our project folders. 
You can now activate the environment with: 

```sh
source .venv/bin/activate
```
`pip` is Python's package manager. Running pip install --upgrade pip updates it to the latest version, potentially providing bug fixes, improvements, and new features.
```sh
pip install --upgrade pip
``` 
**`Note`** : If you encounter an error when trying to run pip install --upgrade pip, it could be because you are missing the -m flag to specify the Python interpreter. To resolve this, consider using the following command:
```sh
python.exe -m pip install --upgrade pip
```
Adding the -m flag helps ensure that the pip command is executed within the context of the correct Python interpreter, which can resolve certain issues related to package installations and upgrades.


If you want to deactivate it run:

```sh 
deactivate
```

In order to use the real power of virtual environments we need to know how to install packages inside a specific environment. We can use a package installer for Python packages called Pip. The good news is: its already installed. We can simply run the command 

```sh
pip install <package_name>
```

and Pip will look for the latest version of the package in the Python Package Index (PyPI), calculate the dependencies and install all of them to ensure the new package will work flawlessly. 

There is another way of installing packages inside an environment. Let's assume you want to create the same environment as someone else is using with exactly the same package versions. In this case you don't need to install them by hand. You can also use a `requirements.txt` file. Make sure the file is located in the directory where you want to create your environment. The steps for creating and activating the environment are the same as shown above, but for installing the packages you can run: 

```sh 
pip install -r requirements.txt
``` 

Of course, you can also create a requirements.txt file yourself. Activate an environment where you have installed some packages. With the following commands, you can either print a list of packages and their version numbers or write the output directly to a file named `requirements.txt`.

```sh
# shows list of packages
pip freeze   
# writes list to file 
pip freeze > requirements.txt     
```

> You may wonder what the difference is between using `brew` and `pip`. They are both package installers, but brew, which is based on Ruby and Git, can be used to install all kinds of software packages, while pip, which is written in Python, can only be used to install Python packages. The main difference, however, is that brew installs packages globally and it cannot be used to install something only in a specific virtual environment. To install a package only locally in an environment you have to use pip!
> 


### Creating virtual environments with miniconda

You can also manage virtual environments by using `miniconda`. Maybe you have heard of **Anaconda** a distribution of Python and R. We will not download the whole Anaconda distribution since it contains a lot of stuff we will not use, but we can download the package manager `miniconda` directly using `brew`. Miniconda is a parallel way to deal with packages than pyenv and venv. You will also need to do some extra setup so that conda does not become the default package/env management tool.. 

```sh
brew install miniconda
```

You now have two options to create and install a new environment. You can either install it from an `environment.yml` file or step by step. At the beginning we will use an environment.yml file which contains a list of all the packages we want to install in a specific format. You can find the file called [nf_base_environment.yml](nf_base_environment.yml) in this repo.
Download the file and move to the folder where you stored it. With the following commands you can now activate `miniconda3` and install a new environment called `nf_base` (the name is defined at the top of the .yml file).

```sh
conda env create --file nf_base_environment.yml
```

In order to activate or deactivate the virtual environment run:

```sh 
conda activate nf_base
conda deactivate
```
While the environment is active you should see the Python version (in our case) 3.11.3 and the name of the environment (nf_base) in your terminal. 

In order to create an environment from scratch you can use this workflow:

```sh 
pyenv local miniconda3-latest
# Create new environment
conda create --name <env_name>
# Activate envrionment 
conda activate <env_name>
# Installing packages 
conda install <package_name>
# Deactivate environment
conda deactivate 
```



### Troubleshooting

Sometimes you might be doing everything right and it all goes wrong... Then you need to check if you are in the right place with respect to python:

```sh
python --version # Do you use the correct python version? Is it saying what you expect?
which python # Is it pointing to the place you expect your python to be?
# For example if you activated the pyenv and .venv there should be a .venv in the path and no conda
```

In case this is not pointing in the right place... well at least you now have a thing to fix.

In case scipy makes problems during the pip install try using:

```bash
brew install openblas
```

and then use this command to install scipy and numpy:

```bash
OPENBLAS="$(brew --prefix openblas)" pip install numpy scipy
```
