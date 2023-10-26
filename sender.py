import threading
import time

def send_message(db_path, sender_name, message):
    connection = ??.connect(db_path)
    cursor = connection.cursor()
    
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO ASYNC_MESSAGE (SENDER_NAME, MESSAGE, CURRENT_TIME) VALUES (?, ?, ?)", (sender_name, message, current_time))
    
    connection.commit()
    connection.close()


