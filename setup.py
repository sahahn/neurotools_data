from setuptools import setup, find_packages

setup(name='neurotools_data',
      version='1.2.2',
      description='The associated reference and default data for neurotools',
      url='http://github.com/sahahn/neurotools_data',
      author='Sage Hahn',
      author_email='sahahn@uvm.edu',
      license='MIT',
      packages=find_packages(),
      zip_safe=False,
      include_package_data=True,
      package_data={'neurotools_data': ['*/*/*', '*/*']},
      package_dir={'neurotools_data': 'neurotools_data'})