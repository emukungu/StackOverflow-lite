import psycopg2
# from .routes.post_a_question_route import post

question = """CREATE TABLE questions(
    question_id INT PRIMARY KEY NOT NULL,
    title VARCHAR(255) NOT NULL,
    question_description VARCHAR(255) NOT NULL,
    date_created TIMESTAMP NOT NULL,
    user_id INT NOT NULL,
    CONSTRAINT question_user_id_fkey FOREIGN KEY(user_id)
        REFERENCES users(user_id) MATCH SIMPLE
        ON UPDATE NO ACTION ON DELETE NO ACTION
);"""

answer = """CREATE TABLE answers(
    answer VARCHAR (255) NOT NULL,
    user_id INT NOT NULL,
    question_id INT NOT NULL,
    CONSTRAINT answer_user_id_fkey FOREIGN KEY(user_id)
        REFERENCES users(user_id) MATCH SIMPLE
        ON UPDATE NO ACTION ON DELETE NO ACTION,
    CONSTRAINT answer_question_id_fkey FOREIGN KEY(question_id)
        REFERENCES questions(question_id) MATCH SIMPLE
        ON UPDATE NO ACTION ON DELETE NO ACTION
);"""

user ="""CREATE TABLE users(
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    user_password VARCHAR(255) NOT NULL,
    user_id INT PRIMARY KEY NOT NULL
);"""
        

def db_connection():
    """ Connect to database"""    
    con = psycopg2.connect(host="localhost", database="trial5", user="postgres", password="postgres")
    cursor = con.cursor()
    cursor.execute(user)     
    cursor.execute(question)
    cursor.execute(answer)
    con.commit()    
    cursor.close()
    con.close()

def another_connection():
    conn = psycopg2.connect(host="localhost", database="again", user="postgres", password="postgres")
    cur = conn.cursor()
    return cur


db_connection()

