from setuptools import setup, find_packages

setup(name='neurotools_data',
      version='1',
      description='The associated reference and default data for neurotools',
      url='http://github.com/sahahn/neurotools_data',
      author='Sage Hahn',
      author_email='sahahn@uvm.edu',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      package_data={'data': ['*/*/*', '*/*']},
      package_dir={'neurotools_data': 'neurotools_data'})