
## Installing pyenv-win

To set up `pyenv-win` on your Windows system, follow these steps:

- **Download pyenv-win ZIP-archive**: [pyenv-win](https://github.com/pyenv-win/pyenv-win/archive/master.zip)

- **Start a new PowerShell with admin privileges**:
   - Right-click on the PowerShell icon in the start menu.
   - Choose "Run as administrator."

Run the following command to enable script execution:
   ```PowerShell
   Set-ExecutionPolicy unrestricted
   ```
Press 'A' to choose Yes to ALL. After this, you can close the admin PowerShell and open a new one without admin privileges.

1. **Create a new folder** <.pyenv> in your user folder. You can do this using the Explorer or with the following PowerShell command:
    ```PowerShell
    mkdir $HOME/.pyenv
    ```
2. **Extract the ZIP-archive** and copy the pyenv-win folder and the .version file from the pyenv-win-master folder into the newly created .pyenv folder in your user directory.
3. **Set the environment variables:**

    Run these commands to set the environment variables:
    ```PowerShell
    [System.Environment]::SetEnvironmentVariable('PYENV', $env:USERPROFILE + "\.pyenv\pyenv-win\", "User")
    [System.Environment]::SetEnvironmentVariable('PYENV_HOME', $env:USERPROFILE + "\.pyenv\pyenv-win\", "User")
    ```
4. **Add the bin folder to the PATH variable:**

    Add pyenv-win to your PATH for easy access. Run this command:
    ```PowerShell
    [System.Environment]::SetEnvironmentVariable('path', $env:USERPROFILE + "\.pyenv\pyenv-win\bin;" + $env:USERPROFILE + "\.pyenv\pyenv-win\shims;" + [System.Environment]::GetEnvironmentVariable('path', "User"), "User")
    ```
    for security warning when running pyenv, you can disable this warning by "unblocking" the pyenv script with the following command:
    ```PowerShell
    Unblock-File $HOME/.pyenv/pyenv-win/bin/pyenv.ps1
    ```
    **`Note:`** If want to use git-bash shell you can Update your configuration (~/.bashrc or ~/.zshrc for Zsh users). Add the following line to set the PATH:

     ```BASH
    echo 'export PATH="$HOME/.pyenv/shims:$PATH"' >> ~/.bashrc
    ```
5. close the current PowerShell session and open a new one .

6. Now, you can run pyenv by entering:
    ```PowerShell
    pyenv --version
    ```
## Continue with the Setup
After successfully installing `pyenv-win` ,you can set up `pyenv` to manage Python versions for your projects.
1. **Install Python 3.11.3 :**
    Now, you can use pyenv to install Python 3.11.3 locally. Run the following command:
    ```PowerShell
    pyenv install 3.11.3
    ```
2. **Set the Local Python Version :**
This makes Python 3.11.3 your project's default version.   
    ```PowerShell
    pyenv local 3.11.3
    ```
3. **Create a Virtual Environment :**
This isolates your project from the system-wide Python installation.

    **`PowerShell CLI :`**

    ```PowerShell
    python -m venv .venv
    .venv\Scripts\Activate.ps1
    python -m pip install --upgrade pip
    ``` 
    
    **`Git-bash CLI :`**
    ```BASH
    python -m venv .venv
    source .venv/Scripts/activate
    python -m pip install --upgrade pip
    ```

    **`Note`** : 
    - If you encounter an error when trying to run `python -m pip install --upgrade pip`, try using the following command:
        ```PowerShell
        python.exe -m pip install --upgrade pip
        ```

    - If you want to deactivate the Environment run:
        ```PowerShell 
        deactivate
        ```