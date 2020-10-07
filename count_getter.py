import csv
import numpy as np
from datetime import datetime
import time
import requests
import os
os.chdir('/Users/collinsinclair/Documents/Other/g1_capacity')


def get_count():

    print('Count requested: ' + str(datetime.now()))

    url = 'https://portal.rockgympro.com/portal/public/b01ab221559163c5e9a73e078fe565aa/occupancy?&iframeid=occupancyCounter&fId='
    text = requests.get(url).text
    line = ""

    for item in text.split("\n"):
        if "\'count\'" in item:
            line = (item.strip())

    count = int(line.split(":")[1][0:-1])

    print('Count: ' + str(count))

    return count

# t_end = time.time() + 60 * 60 * 5 # run for five hours before terminating


while True:

    if (datetime.now().hour > 5) and (datetime.now().hour < 22):

        try:

            with open('g1_occupancy.csv', mode='a') as occupancy:
                occupancy_writer = csv.writer(occupancy)
                occupancy_writer.writerow([datetime.now(), get_count()])

                print('Line written:    ' + str(datetime.now()) + '\n')

        except:
            print('There was an error writing a line at ' +
                  str(datetime.now()) + '\n')

    else:
        print('Waiting for open hours.\n')

    time.sleep(60 * 5)
