#!/usr/bin/env python

from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(name='tadasets',
      version='0.0.1',
      description='Great data sets for Topological Data Analysis.',
      long_description=long_description,
      long_description_content_type="text/markdown",	
      author='Nathaniel Saul',
      author_email='nathaniel.saul@wsu.edu',
      url='https://github.com/sauln/tadasets',
      license='MIT',
      packages=['tadasets'],
      include_package_data=True,
      install_requires=[
        'numpy',
      ],
      python_requires='>=2.7,!=3.1,!=3.2,!=3.3',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'Intended Audience :: Financial and Insurance Industry',
        'Intended Audience :: Healthcare Industry',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Mathematics',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
      ],
      keywords='topological data analysis, data sets, test data'
     )
