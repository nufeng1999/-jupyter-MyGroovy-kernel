# Groovy kernel for Jupyter
[Example](https://github.com/nufeng1999/jupyter-MyGroovy-kernel/blob/master/example/jupyter_groovy_readme.ipynb "Example")
* Make sure you have the following requirements installed:
  * groovy
  * jupyter
  * python 3
  * pip

### Step-by-step

```bash
git clone https://github.com/nufeng1999/jupyter-MyGroovy-kernel.git
cd jupyter-MyGroovy-kernel
pip install -e .  # for system install: sudo install .
cd jupyter_MyGroovy_kernel && install_MyGroovy_kernel --user # for sys install: sudo install_dart_kernel
# now you can start the notebook
jupyter notebook
```

## License

[MIT](LICENSE.txt)
