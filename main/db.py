
question = """CREATE TABLE IF NOT EXISTS questions(
    question_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    question_description VARCHAR(255) NOT NULL,
    date_created TIMESTAMP NOT NULL,
    user_id INT NOT NULL,
    CONSTRAINT question_user_id_fkey FOREIGN KEY(user_id)
        REFERENCES users(user_id) 
);"""

answer = """CREATE TABLE IF NOT EXISTS answers(
    answer VARCHAR (255) NOT NULL,
    user_id INT NOT NULL,
    question_id INT NOT NULL,
    CONSTRAINT answer_user_id_fkey FOREIGN KEY(user_id)
        REFERENCES users(user_id) MATCH SIMPLE
        ON UPDATE NO ACTION ON DELETE NO ACTION,
    CONSTRAINT answer_question_id_fkey FOREIGN KEY(question_id)
        REFERENCES questions(question_id) 
);"""

user ="""CREATE TABLE IF NOT EXISTS users(
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    user_password VARCHAR(255) NOT NULL    
);"""
        

 
    
    




