[![Build Status](https://travis-ci.org/emukungu/StackOverflow-lite.svg?branch=database)](https://travis-ci.org/emukungu/StackOverflow-lite) [![Coverage Status](https://coveralls.io/repos/github/emukungu/StackOverflow-lite/badge.svg?branch=database)](https://coveralls.io/github/emukungu/StackOverflow-lite?branch=database) 
[![Maintainability](https://api.codeclimate.com/v1/badges/65d2700f7c2f583e0fd6/maintainability)](https://codeclimate.com/github/emukungu/StackOverflow-lite/maintainability)

# StackOverflow-lite
StackOverflow-lite is a platform where people can ask questions and provide answers.

## Project APIs

API endpoint | Functionality
-------------|--------------
GET /api/v1/questions| Get all questions
POST /api/v1/questions| Post a question
GET /api/v1/questions/questionId| Get a specific question
POST /api/v1/questions/questionId/answer| Post an answer
DELETE /api/v1/questions/questionId| Delete a question
POST /api/v1/auth/signup| Register a user
POST /api/v1/auth/login| Login a user

## Technologies Used
* Python 3.6
* Flask
* Postgresql

## Setting up the project
Clone repository from link below
* git clone `https://github.com/emukungu/StackOverflow-lite.git`

Change directory
* cd StackOverflow-lite

Setup virtual environment
* mkvirtualenv 'virtualenv_name' 

Install project requirements
* pip install -r requirements.txt

Create a database in postgresql
* create database database_name;

Run the application to start the server
* python run.py 

Run the tests
* nosetests 

Open the browser to view the endpoints with their specifications
* localhost:5000 

## Demo
https://stackoverflow-esther.herokuapp.com/

### License
MIT License

Copyright (c) 2018 **Esther**

