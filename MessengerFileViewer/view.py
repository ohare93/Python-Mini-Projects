# https://github.com/chingjunetao/medium-article/blob/master/analyse-facebook-messenger-data/analyse-fb-message.py

import os
import json
from tqdm import tqdm
import csv
from datetime import datetime

directory = "/home/jmo/Downloads/facebook-jordanoha/messages/inbox"
folders = os.listdir(directory)

if ".DS_Store" in folders:
    folders.remove(".DS_Store")

with open("output.csv", 'a') as csv_file:
    writer = csv.writer(csv_file)

    for folder in tqdm(folders):
        print(folder)
        for filename in os.listdir(os.path.join(directory, folder)):
            if filename.startswith("message"):
                data = json.load(open(os.path.join(directory, folder, filename), "r"))
                for message in data["messages"]:
                    try:
                        date = datetime.fromtimestamp(message["timestamp_ms"] / 1000).strftime("%Y-%m-%d %H:%M:%S")
                        sender = message["sender_name"]
                        content = message["content"]

                        writer.writerow([date, sender, content])

                    except KeyError:
                        pass
