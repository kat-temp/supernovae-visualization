import matplotlib.pyplot as plt
import numpy as np

with open('SNnames.txt') as f:
    swift_list= f.readlines()

swift_list=[x.strip() for x in swift_list]

y = str()

for x in swift_list:
    if x==y:
        swift_list.remove(x)

for x in swift_list:
    if 'MASTER' in x:
        swift_list.remove(x)

for x in swift_list:
        if "inPGC" in x:
                swift_list.remove(x)


print(swift_list)

bin_2019=0

for x in swift_list:
    if '19' in x:
        bin_2019 = bin_2019+1
    else:
        bin_2019 = bin_2019

print(bin_2019)


bin_2018=0

for x in swift_list:
    if '18' in x:
        bin_2018 = bin_2018+1
    else:
        bin_2018 = bin_2018

print(bin_2018)

bin_2017=0

for x in swift_list:
    if '17' in x:
        bin_2017 = bin_2017+1
    else:
        bin_2017 = bin_2017

print(bin_2017)

bin_2016=0

for x in swift_list:
    if '16' in x:
        bin_2016 = bin_2016+1
    else:
        bin_2016 = bin_2016

print(bin_2016)

bin_2015=0

for x in swift_list:
    if '15' in x:
        bin_2015 = bin_2015+1
    else:
        bin_2015 = bin_2015

print(bin_2015)

bin_2014=0

for x in swift_list:
    if '14' in x:
        bin_2014 = bin_2014+1
    else:
        bin_2014 = bin_2014

print(bin_2014)

bin_2013=0

for x in swift_list:
    if '13' in x:
        bin_2013 = bin_2013+1
    else:
        bin_2013 = bin_2013

print(bin_2013)

bin_2012=0

for x in swift_list:
    if '12' in x:
        bin_2012 = bin_2012+1
    else:
        bin_2012 = bin_2012

print(bin_2012)

bin_2011=0

for x in swift_list:
    if '11' in x:
        bin_2011 = bin_2011+1
    else:
        bin_2011 = bin_2011

print(bin_2011)

bin_2010=0

for x in swift_list:
    if '10' in x:
        bin_2010 = bin_2010+1
    else:
        bin_2010 = bin_2010

print(bin_2010)

bin_2009=0

for x in swift_list:
    if '09' in x:
        bin_2009 = bin_2009+1
    else:
        bin_2009 = bin_2009

print(bin_2009)

bin_2008=0

for x in swift_list:
    if '08' in x:
        bin_2008 = bin_2008+1
    else:
        bin_2008 = bin_2008

print(bin_2008)

bin_2007=0

for x in swift_list:
    if '07' in x:
        bin_2007 = bin_2007+1
    else:
        bin_2007 = bin_2007

print(bin_2007)

bin_2006=0

for x in swift_list:
    if '06' in x:
        bin_2006 = bin_2006+1
    else:
        bin_2006 = bin_2006

print(bin_2006)

bin_2005=0

for x in swift_list:
    if '05' in x:
        bin_2005 = bin_2005+1
    else:
        bin_2005 = bin_2005

print(bin_2005)