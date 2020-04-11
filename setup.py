# encoding: utf8
from distutils.core import setup
from setuptools import find_packages
from os import path

with open(path.join(path.abspath(path.dirname(__file__)), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

install_requires = ['matplotlib']

setup(name='japanize-matplotlib',
      version='1.1.0',
      description='matplotlibのフォント設定を自動で日本語化する',
      author='uehara1414',
      author_email='akiya.noface@gmail.com',
      url='https://github.com/uehara1414/japanize-matplotlib',
      long_description=long_description,
      long_description_content_type="text/markdown",
      license='MIT License',
      packages=find_packages(),
      install_requires=install_requires,
      include_package_data=True,
      package_data={
          'japanize_matplotlib': ['fonts/*'],
      })
