import os
import re
import datetime

##Initializing Empty List Variables
arpData = []
filteredArpData = []

#Initializing Current Date and Time/Change Date Format
t = datetime.datetime.now()
formattedDate = datetime.date.today()

#Read the ARP Table for current machine
with os.popen('arp -a') as f:
    arpData = f.read()

#Returns ARP Table Results as REGEX | Writes Duplicate Spoofed ARP only
def arpTableExtraction(arpData, filteredArpData):
    for line in re.findall('([-.0-9]+)\s+([-0-9a-f]{17})', arpData):
        filteredArpData = line

        if len(filteredArpData) == len(set(filteredArpData)):
            with open(f'ARP Spoofed {formattedDate}.txt', 'w+') as file:
                file.write(f"ARP has been Spoofed!\nThe IP and MAC Addresses are: {line}\nDate: {t}")
            return True
        else:
            return False

arpTableExtraction(arpData, filteredArpData)

