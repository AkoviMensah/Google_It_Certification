#!/usr/bin/env python3
import shutil
import psutil
import time
import socket
from psutil import virtual_memory
import emails

while True:
    sender = "automation@example.com"
    receiver = "username@example.com"
    subject = ""
    total, used, free = shutil.disk_usage("/")
    mem = virtual_memory()
    THRESHOLD = 500 * 1024 * 1024  # 100MB
    if psutil.cpu_percent() > 0.8:
        subject = "Error - CPU usage is over 80%"
    elif (free / total) * 100 < 20:
        subject = "Error - Available disk space is less than 20%"
    elif mem.available <= THRESHOLD:
        subject = "Error - Available memory is less than 500MB"
    elif not socket.gethostbyname(socket.gethostname()) == "127.0.0.1":
        subject = "Error - localhost cannot be resolved to 127.0.0.1"
    body = "Please check your system and resolve the issue as soon as possible."
    
    if len(subject) > 1:
        message = emails.generate_error_report(sender, receiver, subject, body)
        emails.send(message)
    time.sleep(60)