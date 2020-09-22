#! /usr/bin/env python3
import requests
import os
n = []
for i in os.listdir("./supplier-data/images/"):
    if i.endswith("jpeg"):
        n.append(i)

url = "http://localhost/upload/"
for i in n:
    with open("supplier-data/images/" + i, "rb") as opened:
        r = requests.post(url, files={"file": opened})