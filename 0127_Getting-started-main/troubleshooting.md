# Troubleshooting

Here you can find solutions to common errors and problems. 

- [Help! My ssh key is not stored in the buffer anymore. Where can I find it again?](#finding-the-ssh-key)
- [Oh no! setup.sh has failed and I don't know what to do.](#setupsh-has-failed)
- [Damn! Apparently the metageneration failed. :(](#metageneration-failed)
- [Please help me! I can't use Jupyter in VSCode with pyenv.](#unable-to-use-jupyter-in-vscode-with-pyenv)


## Finding the ssh key

If you run the command from step 6 in the README, the ssh key will be automatically stored in your buffer. If for whatever reason the buffer is cleared before you can enter the key on github, you can paste the following command into your terminal to copy it again: 

```sh
cat ~/.ssh/id_rsa.pub | pbcopy
```


## setup.sh has failed

If you type `./setup.sh` in your terminal and press Enter, it will invoke 3 setup scripts one after another - `setup1.sh`, `setup2.sh` and `setup3.sh`. 

They need to be executed 1 after the other. You can try checking which script failed by running them separately or even run the single steps inside the files manually.


## metageneration failed

![screenshot of metadata generation error](https://user-images.githubusercontent.com/6564007/218112999-e067cb61-8c32-431a-b819-26b744d7f479.JPG)

In most cases the problem was that Rust wasn't added to the $PATH variable. 
You can add it yourself to `.zshrc` using vim. To open the file in vim run:
```sh
vim ~/.zshrc
```
Add the following at the bottom of the file: `export PATH="$HOME/.cargo/bin:$PATH"`

run the following command to apply the changes:

```sh
source ~/.zshrc
```

You can check if this works by running `rustc --version`. If the output is a version number you solved the issue. 

However, if it's empty or gives an error you can try to reinstall rust using:

```sh
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

then run `source ~/.zshrc` to apply the changes.

Check the rust version again to confirm that the rustc command works.


## Unable to use Jupyter in VScode with PyEnv

In most cases, checking for activating the correct enviorment works. If not, check [this solution](https://github.com/microsoft/vscode-jupyter/issues/12820#issuecomment-1427167591) that requires installing a `VSIX` file.