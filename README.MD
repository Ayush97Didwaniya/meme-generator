# Overview

Meme generator is a multimedia application to dynamically generate memes, including an image with an overlaid quote.

## Stack Used
Python3.9

## Project setup
To run the application first we need to install dependencies, go to root folder and run below command.

```bash
pip install -r requirements.txt
```

pdftotext may not be installed on your local machine (Mac or Windows). If this is the case, you can install using the open source [XpdfReader utility](https://www.xpdfreader.com/pdftotext-man.html)

In QuoteEngine/PDFIngestor.py file -
```bash
call = subprocess.call(['pdftotext', path, tmp]) 
```
if above function doesnt work then use below code instead of above calling function:
```bash
pdftotext = r"C:\xpdf-tools-win-4.03\bin32\pdftotext.exe"
call = subprocess.call(['pdftotext','-layout', path, tmp])
```
where pdftotext will define path of 'pdftotext.exe' file.

## Project run
- To run the project through command line. go to src folder and run below command to generate meme's.
```bash 
Python3 meme.py
```
you can provide three optional CLI arguments:
```bash 
--body a string quote body
--author a string quote author
--path an image path
```
The output will come in './tmp' directory.

- To serve the application on browser you need to run app.py
```bash 
Python3 app.py
```
It will show you url on which application is running.<br />
after hitting the url, It will show you 'random' named button to generate a new meme. <br />
User can add its custom meme by doing manual entry on create meme form. <br />
once user click on create meme it will generate customized meme.

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
 - pandas : a fast and easy to use datastructure for tabular data.
 - Pillow : Offers features to work with graphics and has interfaces for filtering, resizing, and drawing onto the images (including drawing text!)
 - requests : Requests allows you to send HTTP/1.1 requests extremely easily. 
 - Flask : Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications.
 - Python-docx : we need to install the python-docx library to work with word documents in Python. 
 - setuptools : python-docx library requires a new version of a Python helper module called setuptools.