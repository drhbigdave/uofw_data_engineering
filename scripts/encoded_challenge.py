
bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test
bin/kafka-topics.sh --list --zookeeper localhost:2181
bin/kafka-topics.sh --describe --zookeeper localhost:2181 [--topic test]


bin/kafka-console-consumer.sh --bootstrap-server sandbox-hdp.hortonworks.com:6667 --topic test

val area = {
	val PI = 3.1
	println(s"Inside scope 1, PI = $PI");
	{
		val PI = 3.14
		println(s"Inside scope 2, PI = $PI")
		PI * radius * radius
		}
	//PI * radius * radius
	}

for (day <- daysOfTheWeekList)
{
	day match{
	    case "Mon" => println("Manic Monday")
	    case otherDay => println(otherDay)
	}
}

for (day <- daysOfTheWeekList) yield
{
	day match{
	    case "Mon" => "Manic Monday"
	    case otherDay => otherDay
	}
}

for {i <- 0 until 7
     j <- daysOfTheWeekList}
{
	println(s"$i,$j")
}


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 22:26:10 2019

@author: davidhagan
"""

words = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq\
 ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw\
 rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb.\
 lmu ynnjw ml rfc spj.".split()
 
alpha = ('a', 'b', 'c', 'd')

print(alpha)
print(words)
ord('a')

codesplit = coded.split()

for x in codesplit:
    listoflists.append(list(x))
        
for a in listoflists:
    d=[]
    d.clear()
    for b in a:
        c = ord(b)
        d.append(c)
    ordlist.append(d)
    
shifted = []
for a in ordlist:
    d = []
    d.clear()
    for b in a:
        if b == 122:
           b = 98
        elif b == 121:
           b = 97
        elif b == 46:
            b = 46
        elif b == 40:
            b = 40
        elif b == 41:
            b = 41
        else:
           b = b + 2
        d.append(b)
    shifted.append(d)

decrypted = []      
for a in shifted:
    d = []
    d.clear()
    for b in a:
        c = (chr(b))
        d.append(c)
    decrypted.append(d)

for a in decrypted:
    print(''.join(a))
    



for a in range(97, 123):
    alphabet.append(chr(a))

alphstr = ''.join(alphabet)

alph_code = 'cdefghijklmnopqrstuvwxyzab'

trantab = str.maketrans(alphstr, alph_code)

print(words.translate(trantab))
    