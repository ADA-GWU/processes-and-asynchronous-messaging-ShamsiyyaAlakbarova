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

def send_message(sender_name, message, conn):
    sent_time = time.strftime('%Y-%m-%d %H:%M:%S')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO ASYNC_MESSAGES (SENDER_NAME, MESSAGE, SENT_TIME) VALUES (%s, %s, %s)',
                   (sender_name, message, sent_time))
    conn.commit()

def user_input_loop(sender_name, connections):
    while True:
        user_input = input("Enter a message (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        connection = random.choice(connections)  # Choose a random connection
        send_message(sender_name, user_input, connection)

num_threads = 5  # Number of database servers
threads = []

# Define the list of database server IPs here
db_server_ips = ['server1_ip', 'server2_ip', 'server3_ip', 'server4_ip', 'server5_ip']
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

for i in range(num_threads):
    sender_name = 'Shamsiyya'
    thread = threading.Thread(target=send_message, args=(sender_name, 'user_input', random.choice(connections)))
    threads.append(thread)
    thread.start()

user_input_thread = threading.Thread(target=user_input_loop, args=(sender_name, connections))
user_input_thread.start()
user_input_thread.join()

# Close all database connections when done
for conn in connections:
    conn.close()
