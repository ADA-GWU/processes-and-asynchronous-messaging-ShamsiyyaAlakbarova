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
user_input_thread.join()'''

import psycopg2
import threading
import time
import random

# Function to send a message
def send_message(sender_name, message, conn):
    sent_time = time.strftime('%Y-%m-%d %H:%M:%S')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO ASYNC_MESSAGES (SENDER_NAME, MESSAGE, SENT_TIME) VALUES (%s, %s, %s)',
                   (sender_name, message, sent_time))
    conn.commit()

# Number of database servers
num_threads = 5
threads = []

# Define the list of database server IPs here
db_server_ips = ['127.0.0.1', '192.168.0.173']
connections = []

# Create connections to each database server
for ip in db_server_ips:
    conn = psycopg2.connect(
        host=ip,
        database="mydb",
        user="postgres",
        password="August2003"
    )
    connections.append(conn)

# Define your sender_name
sender_name = 'Shamsiyya'

def user_input_loop():
    while True:
        user_input = input("Enter a message (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        # Choose a random connection
        connection = random.choice(connections)
        send_message(sender_name, user_input, connection)

# Create threads for sending messages
for i in range(num_threads):
    thread = threading.Thread(target=user_input_loop)
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

# Close all database connections when done
for conn in connections:
    conn.close()
