
question = """CREATE TABLE IF NOT EXISTS questions(
    question_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    question_description VARCHAR(255) NOT NULL,
    date_created TIMESTAMP NOT NULL,
    user_id INT NOT NULL,
    CONSTRAINT questions_user_id_fkey FOREIGN KEY(user_id)
        REFERENCES users(user_id) 
        ON DELETE CASCADE     
);"""

answer = """CREATE TABLE IF NOT EXISTS answers(
    answer_id SERIAL PRIMARY KEY,
    answer VARCHAR (255) NOT NULL,
    user_id INT NOT NULL,
    question_id INT NOT NULL,
    CONSTRAINT answers_question_id_fkey FOREIGN KEY(question_id)
        REFERENCES questions(question_id)   
        ON DELETE CASCADE
);"""

user = """CREATE TABLE IF NOT EXISTS users(
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    user_password VARCHAR(255) NOT NULL
);"""



# comment = """CREATE TABLE IF NOT EXISTS comments(
#     comment_id SERIAL PRIMARY KEY,
#     answer_id INT NOT NULL,
#     user_id INT NOT NULL,
#     comment VARCHAR (255) NOT NULL,
#     CONSTRAINT comments_answer_id_fkey FOREIGN KEY(answer_id)
#         REFERENCES answers(answer_id)
#         ON DELETE CASCADE
#     );"""



# vote = """CREATE TABLE IF NOT EXISTS votes(
#     vote_id SERIAL PRIMARY KEY,
#     answer_id INT NOT NULL,
#     user_id INT NOT NULL,
#     up_vote INT,
#     down_vote INT,
#     CONSTRAINT comments_answer_id_fkey FOREIGN KEY(answer_id)
#         REFERENCES answers(answer_id)    
#         ON DELETE CASCADE 
#     );"""
      

 
    
    




