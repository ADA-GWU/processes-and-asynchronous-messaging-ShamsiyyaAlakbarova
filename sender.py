'''import psycopg2
import threading
import time
import random

def send_message(sender_name, message):
    sent_time = time.strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('INSERT INTO ASYNC_MESSAGES (SENDER_NAME, MESSAGE, SENT_TIME) VALUES (%s, %s, %s)',
                   (sender_name, message, sent_time))
    conn.commit()

num_threads = 5  # Number of database servers
threads = []

# Create a PostgreSQL database connection
conn = psycopg2.connect(
    dbname='mydb',
    user='postgres',
    password='August2003',
    host='127.0.0.1',
    port='5432'
)
cursor = conn.cursor()

for i in range(num_threads):
    sender_name = 'Shamsiyya'
    thread = threading.Thread(target=send_message, args=(sender_name, ''))
    threads.append(thread)
    thread.start()

def user_input_loop():
    while True:
        user_input = input("Enter a message (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        random_thread = random.choice(threads)
        message_thread = threading.Thread(target=send_message, args=(sender_name, user_input))
        message_thread.start()

user_input_thread = threading.Thread(target=user_input_loop)
user_input_thread.start()
user_input_thread.join()'''

import psycopg2
import threading
import time
import random

def send_message(sender_name, message):
    sent_time = time.strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('INSERT INTO ASYNC_MESSAGES (SENDER_NAME, MESSAGE, SENT_TIME) VALUES (%s, %s, %s)',
                   (sender_name, message, sent_time))
    conn.commit()

num_threads = 5  # Number of database servers
threads = []

# Create a PostgreSQL database connection
conn = psycopg2.connect(
    host="localhost",
    database="mydb",
    user="postgres",
    password="August2003")
cursor = conn.cursor()

for i in range(num_threads):
    sender_name = 'Shamsiyya'
    thread = threading.Thread(target=send_message, args=(sender_name, 'user_input'))
    threads.append(thread)
    thread.start()

def user_input_loop():
    while True:
        user_input = input("Enter a message (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        message_thread = threading.Thread(target=send_message, args=(sender_name, user_input))
        message_thread.start()

user_input_thread = threading.Thread(target=user_input_loop)
user_input_thread.start()
user_input_thread.join()