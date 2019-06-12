#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 17:52:42 2019

@author: davidhagan
"""

import os

rootdir = "/Users/davidhagan/projects/uofw/maildir"
sublist = []
for directory, subdirectory, filenames in  os.walk(rootdir):
    print(directory, subdirectory, len(filenames))
    
from email.parser import Parser

file_to_read = "/Users/davidhagan/projects/uofw/maildir/allen-p/inbox/13."

with open(file_to_read, "r") as f:
    data = f.read()
    
email = Parser().parsestr(data)

print("\nTo: " , email['to'])
print("\n From: " , email['from'])
 
print("\n Subject: " , email['subject'])

print("\n \n Body: " , email.get_payload())

    if subdirectory.str.contains('inbox'):
        print(subdirectory)
receiverList = ()
import re
def parseEmail(email):
    fields = email.split("Subject:")[0].split('\n')
    messageID = fields[0].split(':')[1].strip()
    date = fields[1].split(':')[1].strip()
    sender = fields[2].split(':')[1].strip()
    message = email.replace('\n','').replace('\t','').strip()

    
    
    receivers = email.split("To:")[1].split('Subject:')[0].split(',')
    clean_receivers = [i.strip() for i in receivers]
    to = ",".join(clean_receivers)
    return([messageID,date,sender,to,message])


    
parseEmail(data)

    body = email.split("FileName:")[1].replace('\n','').replace('\t','')
    clean_body = body.replace('\n', '')
    
#!/bin/bash
echo "MessageID,Date,From,To,Body" > /tmp/enronCombined.csv
for i in /tmp/enron12/*.csv ; do
    echo "Processing $i"
    cat $i >> /tmp/enronCombined.csv
    rm $i
done
echo "Done"