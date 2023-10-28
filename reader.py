import psycopg2
import threading
import time

def read_available_messages(sender_name):
    while True:
        cursor.execute('SELECT SENDER_NAME, MESSAGE, SENT_TIME FROM ASYNC_MESSAGES WHERE RECEIVED_TIME IS NULL AND SENDER_NAME != %s LIMIT 1',
                       (sender_name,))
        message = cursor.fetchone()

        if message:
            sender, message_text, sent_time = message
            received_time = time.strftime('%Y-%m-%d %H:%M:%S')
            print(f'Sender {sender} sent "{message_text}" at time {sent_time}')
            cursor.execute('UPDATE ASYNC_MESSAGES SET RECEIVED_TIME = %s WHERE SENDER_NAME = %s AND RECEIVED_TIME IS NULL',
                           (received_time, sender))
            conn.commit()

        time.sleep(1)  # Adjust the interval as needed

# Create a PostgreSQL database connection
conn = psycopg2.connect(
    dbname='mydb',
    user='postgres',
    password='August2003',
    host='127.0.0.1',
    port='5432'
)
cursor = conn.cursor()

# Define the sender_name variable or retrieve it from the sender
sender_name = 'Shamsiyya'

reader_thread = threading.Thread(target=read_available_messages, args=(sender_name,))
reader_thread.start()
reader_thread.join()
