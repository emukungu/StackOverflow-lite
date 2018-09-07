[![Build Status](https://travis-ci.org/emukungu/StackOverflow-lite.svg?branch=develop)](https://travis-ci.org/emukungu/StackOverflow-lite) [![Coverage Status](https://coveralls.io/repos/github/emukungu/StackOverflow-lite/badge.svg?branch=develop)](https://coveralls.io/github/emukungu/StackOverflow-lite?branch=develop) [![Maintainability](https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/maintainability)](https://codeclimate.com/github/codeclimate/codeclimate/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/test_coverage)](https://codeclimate.com/github/codeclimate/codeclimate/test_coverage)

# StackOverflow-lite
StackOverflow-lite is a platform where people can ask questions and provide answers.

## Project APIs

API endpoint | Functionality
-------------|--------------
GET /api/v1/questions| Get all questions
POST /api/v1/questions| Post a question
GET /api/v1/questions/questionId| Get a specific question
POST api/v1/questions/questionId/answer| Post an answer

## Technologies Used
* Python 3.6
* Flask

## Setting up the project
Clone repository from link below
* git clone `https://github.com/emukungu/StackOverflow-lite.git`

Change directory
* cd StackOverflow-lite

Setup virtual environment
* mkvirtualenv 'virtualenv_name' 

Install project requirements
* pip install -r requirements.txt

Run the tests
* nosetests 

Run the application to start the server
* python run.py 

Open the browser to view the endpoints with their specifications
* localhost:5000 

## Demo
https://stackoverflow-esther.herokuapp.com/

### License
MIT License

Copyright (c) 2018 **Esther**

