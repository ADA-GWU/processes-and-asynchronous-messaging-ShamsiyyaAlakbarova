import psycopg2
import threading
import time

def read_available_messages():
    while True:
        cursor.execute('SELECT * FROM ASYNC_MESSAGES WHERE RECEIVED_TIME IS NULL AND SENDER_NAME != %s LIMIT 1',
                       (sender_name,))
        message = cursor.fetchone()

        if message:
            sender_name, message_text, sent_time, _ = message
            received_time = time.strftime('%Y-%m-%d %H:%M:%S')
            print(f'Sender {sender_name} sent "{message_text}" at time {sent_time}')
            cursor.execute('UPDATE ASYNC_MESSAGES SET RECEIVED_TIME = %s WHERE ID = %s', (received_time, message[0]))
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

reader_thread = threading.Thread(target=read_available_messages)
reader_thread.start()
reader_thread.join()
