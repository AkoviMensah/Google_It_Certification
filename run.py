#! /usr/bin/env python3
import os
import requests
txt = os.listdir("supplier-data/descriptions/")
data = []
for i in txt:
        d = {}
        with open("./supplier-data/descriptions/" +i) as f:
            n = 1
            s = ""
            for line in f:
                if n == 1:
                    d["name"] = line.strip()
                if n == 2:
                    mass = line.strip().strip("lbs").strip()
                    d["weight"] = int(mass)
                if n > 2:
                    s = s + line.strip()
                n += 1
            d["description"] = s
        temp = i.split(".")
        d["image_name"] = temp[0] + ".jpeg"
        data.append(d)
        myurl = 'http://34.71.28.184/fruits/'
        getdata = requests.post(myurl, data= d)
        getdata.raise_for_status()
