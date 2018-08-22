[![Build Status](https://travis-ci.org/emukungu/StackOverflow-lite.svg?branch=ft-post-a-question-%23159866594)](https://travis-ci.org/emukungu/StackOverflow-lite) [![Coverage Status](https://coveralls.io/repos/github/emukungu/StackOverflow-lite/badge.svg?branch=ft-post-a-question-%23159866594)](https://coveralls.io/github/emukungu/StackOverflow-lite?branch=ft-post-a-question-%23159866594) [![Maintainability](https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/maintainability)](https://codeclimate.com/github/codeclimate/codeclimate/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/test_coverage)](https://codeclimate.com/github/codeclimate/codeclimate/test_coverage)

# StackOverflow-lite
StackOverflow-lite is a platform where people can ask questions and provide answers.

## Project APIs

API endpoint | Functionality
-------------|--------------
GET /api/v1/questions| Get all questions
POST /api/v1/questions| Post a question
GET /api/v1/questions/questionId| Get a specific question
POST api/v1/questions/questionId/answer| Post an answer

## Setup/Installation Requirements
* git bash
* Postman
* vscode

## Technologies Used
* Python/flask

## Setting up the project
Clone repository from link below
* git clone `https://github.com/emukungu/StackOverflow-lite.git`

Setup virtual environment
* mkvirtualenv 'virtualenv_name' 

Install project requirements
* pip install -r requirements.txt

Run the tests
* pytest 

Run the application to start the server
* python app.py 

### License
MIT License

Copyright (c) 2018 **Esther**

