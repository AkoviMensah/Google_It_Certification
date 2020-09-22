#!/usr/bin/env python3
import os
import reports
import emails
import datetime
import reports


def main(argv):
    txt = os.listdir("supplier-data/descriptions/")
    data = []
    for i in txt:
            d = {}
            with open("./supplier-data/descriptions/" + i) as f:
                n = 1
                s = ""
                for line in f:
                    if n == 1:
                        d["name"] = line.strip()
                    if n == 2:
                        mass = line.strip().strip("lbs").strip()
                        d["weight"] = int(mass)
                    n = n + 1
            data.append(d)
    x = datetime.datetime.now()
    date = x.strftime("%B") + " " + x.strftime("%d") + ", " + x.strftime("%Y")
    title = "Processed Update on " + date
    p = ""
    for i in data:
        p = p + "name: " + i["name"] + "<br/>" + "weight: " + str(i["weight"]) + "<br/>" + "<br/>"

    if __name__ == "__main__":
        reports.generate_report("/tmp/processed.pdf", title, p)
        sender = "automation@example.com"
        receiver = "username@example.com"
        subject = "Upload Completed - Online Fruit Store"
        body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

        message = emails.generate_email(sender, receiver, subject, body, "/tmp/processed.pdf")
        emails.send(message)
main("hh")
