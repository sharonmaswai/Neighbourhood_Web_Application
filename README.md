# HoodWatch
### by Sharon Maswai

## Description

This is web application that allows the user to creat an account, login,post neighbourhood concerns, view neighbourhoods, businesses and ammenities in those neighbourhoods.
## SETUP INSTRUCTIONS:

### Installation

1.Python 3.6.7

2.Django 1.11.8

### Cloning the repository

git clone https://github.com/sharonmaswai/neighbourhood.git

### Creating a virtual environment

sudo apt-get install python3.6-venv python3.6 -m venv --without-pip virtual source virtual/bin/activate

### Installing dependencies

pip install -r requirements.txt

### Running tests

python3.6 manage.py test photos awaards

### Running the Development server

python3.6 manage.py runserver

## BEHAVIOUR DRIVEN DEVELOPMENT

| Behaviour | Input  | Output |
| -- |-- |--|
|Sign up| Create credentials| Successful sign up if credentials are viable|
|Login|Enter login credentials | Go to landing page|
|View Concerns|Click concerns on navbar| Go to concerns page|
|View a single Neighbourhood, businesses and ammenities|Click on view button on the image|View a single neighbourhood's details, ammenities and businesses|
|Search Hood|Enter neighbourhood name on the search bar|Results of the search|



## TECHNOLOGIES USED

Python 3.6.7

Django 1.11.8

CSS

HTML

PostgreSQL

Bootstrap
 
## BUGS

There are no known bugs.


## CONTACTS

For more information and clarification contact me through chepsharon@gmail.com

## LICENSE

MIT License

Copyright (c) [2019] [SharonMaswai]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
