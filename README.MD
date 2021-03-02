# Overview

Meme generator is a multimedia application to dynamically generate memes, including an image with an overlaid quote.

## Stack Used
Python3.9

## Project setup
To run the application first we need to install dependencies, go to root folder and run below command.

```bash
pip install -r requirements.txt
```
## Project run
To run the project through command line. go to src folder and run below command to generate meme's.
```bash 
Python3 meme.py
```
The output will come in './tmp' directory.

## Submodule description
#### - Quote Engine
The Quote Engine module is responsible for ingesting many types of files that contain quotes. For our purposes, a quote contains a body and an author:
```bash
"This is a quote body" - Author
```
#### - Meme Engine
The Meme Engine Module is responsible for manipulating and drawing text onto images.

## Depedencies description

Below listed dependencies used in project.
 - mypy :  To check if code is respecting the type hints.
 - pandas : a fast and easy to use datastructure for tabular data.
 - Pillow : Offers features to work with graphics and has interfaces for filtering, resizing, and drawing onto the images (including drawing text!)
 - pycodestyle : Utility to fix the indicated style violations. pycodestyle is a tool to check your Python code against some of the style conventions in PEP 8.
 - pydocstyle :  is a static analysis tool for checking compliance with Python docstring conventions.
 - pylint : Pylint is a Python static code analysis tool which looks for programming errors, helps enforcing a coding standard, sniffs for code smells and offers simple refactoring suggestions.
 - requests : Requests allows you to send HTTP/1.1 requests extremely easily. 
 - Flask : Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications.