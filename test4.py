import time
import datetime
import sqlite3

while(1):
    log_mess = datetime.datetime.now().strftime("%Y--%m--%d %H:%M:%S")
    print(log_mess)
    time.sleep(1)


