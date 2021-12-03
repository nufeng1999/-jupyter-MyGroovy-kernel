from setuptools import setup

setup(name='jupyter_MyGroovy_kernel',
      version='0.0.1',
      description='Minimalistic Groovy kernel for Jupyter',
      author='nufeng',
      author_email='18478162@qq.com',
      license='MIT',
      classifiers=[
          'License :: OSI Approved :: MIT License',
      ],
      url='https://github.com/nufeng1999/jupyter-MyGroovy-kernel/',
      download_url='https://github.com/nufeng1999/jupyter-MyGroovy-kernel/tarball/0.0.1',
      packages=['jupyter_MyGroovy_kernel'],
      scripts=['jupyter_MyGroovy_kernel/install_MyGroovy_kernel'],
      keywords=['jupyter', 'notebook', 'kernel', 'groovy'],
      include_package_data=True
      )
