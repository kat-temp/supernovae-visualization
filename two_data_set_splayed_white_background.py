import matplotlib.pyplot as plt
import numpy as np

with open('SNnames.txt') as f:
    content= f.readlines()

with open('nonSNnames.txt') as g:
    new_content= g.readlines()

content=[x.strip() for x in content]
new_content=[x.strip() for x in new_content]

y = str()

for x in content:
    if x==y:
        content.remove(x)

for x in content:
    if 'MASTER' in x:
        content.remove(x)

for x in content:
    if 'CSS' in x:
        content.remove(x) 

content.remove(content[747])
content.remove(content[746])

bin_2018=0

for x in content:
    if '18' in x:
        bin_2018 = bin_2018+1
    else:
        bin_2018 = bin_2018

#print(bin_2018)

bin_2017=0

for x in content:
    if '17' in x:
        bin_2017 = bin_2017+1
    else:
        bin_2017 = bin_2017

#print(bin_2017)

bin_2016=0

for x in content:
    if '16' in x:
        bin_2016 = bin_2016+1
    else:
        bin_2016 = bin_2016

#print(bin_2016)

bin_2015=0

for x in content:
    if '15' in x:
        bin_2015 = bin_2015+1
    else:
        bin_2015 = bin_2015

#print(bin_2015)

bin_2014=0

for x in content:
    if '14' in x:
        bin_2014 = bin_2014+1
    else:
        bin_2014 = bin_2014

#print(bin_2014)

bin_2013=0

for x in content:
    if '13' in x:
        bin_2013 = bin_2013+1
    else:
        bin_2013 = bin_2013

#print(bin_2013)

bin_2012=0

for x in content:
    if '12' in x:
        bin_2012 = bin_2012+1
    else:
        bin_2012 = bin_2012

#print(bin_2012)

bin_2011=0

for x in content:
    if '11' in x:
        bin_2011 = bin_2011+1
    else:
        bin_2011 = bin_2011

#print(bin_2011)

bin_2010=0

for x in content:
    if '10' in x:
        bin_2010 = bin_2010+1
    else:
        bin_2010 = bin_2010

#print(bin_2010)

bin_2009=0

for x in content:
    if '09' in x:
        bin_2009 = bin_2009+1
    else:
        bin_2009 = bin_2009

#print(bin_2009)

bin_2008=0

for x in content:
    if '08' in x:
        bin_2008 = bin_2008+1
    else:
        bin_2008 = bin_2008

#print(bin_2008)

bin_2007=0

for x in content:
    if '07' in x:
        bin_2007 = bin_2007+1
    else:
        bin_2007 = bin_2007

#print(bin_2007)

bin_2006=0

for x in content:
    if '06' in x:
        bin_2006 = bin_2006+1
    else:
        bin_2006 = bin_2006

#print(bin_2006)

bin_2005=0

for x in content:
    if '05' in x:
        bin_2005 = bin_2005+1
    else:
        bin_2005 = bin_2005

#print(bin_2005)

new_bin_2018=0

for x in new_content:
    if '18' in x:
        new_bin_2018 = new_bin_2018+1
    else:
        new_bin_2018 = new_bin_2018

#print(new_bin_2018)

new_bin_2017=0

for x in new_content:
    if '2017' in x:
        new_bin_2017 = new_bin_2017+1
    else:
        new_bin_2017 = new_bin_2017

#print(new_bin_2017)

new_bin_2016=0

for x in new_content:
    if '16' in x:
        new_bin_2016 = new_bin_2016+1
    else:
        new_bin_2016 = new_bin_2016

#print(new_bin_2016)

new_bin_2015=0

for x in new_content:
    if '15' in x:
        new_bin_2015 = new_bin_2015+1
    else:
        new_bin_2015 = new_bin_2015

#print(new_bin_2015)

new_bin_2014=0

for x in new_content:
    if '14' in x:
        new_bin_2014 = new_bin_2014+1
    else:
        new_bin_2014 = new_bin_2014

#print(new_bin_2014)

new_bin_2013=0

for x in new_content:
    if '13' in x:
        new_bin_2013 = new_bin_2013+1
    else:
        new_bin_2013 = new_bin_2013

#print(new_bin_2013)

new_bin_2012=0

for x in new_content:
    if '12' in x:
        new_bin_2012 = new_bin_2012+1
    else:
        new_bin_2012 = new_bin_2012

#print(new_bin_2012)

new_bin_2011=0

for x in new_content:
    if '11' in x:
        new_bin_2011 = new_bin_2011+1
    else:
        new_bin_2011 = new_bin_2011

#print(new_bin_2011)

new_bin_2010=0

for x in new_content:
    if '2010' in x:
        new_bin_2010 = new_bin_2010+1
    else:
        new_bin_2010 = new_bin_2010

#print(new_bin_2010)

new_bin_2009=0

for x in new_content:
    if '09' in x:
        new_bin_2009 = new_bin_2009+1
    else:
        new_bin_2009 = new_bin_2009

#print(new_bin_2009)

new_bin_2008=0

for x in new_content:
    if '08' in x:
        new_bin_2008 = new_bin_2008+1
    else:
        new_bin_2008 = new_bin_2008

#print(new_bin_2008)

new_bin_2007=0

for x in new_content:
    if '07' in x:
        new_bin_2007 = new_bin_2007+1
    else:
        new_bin_2007 = new_bin_2007

#print(new_bin_2007)

new_bin_2006=0

for x in new_content:
    if '06' in x:
        new_bin_2006 = new_bin_2006+1
    else:
        new_bin_2006 = new_bin_2006

#print(new_bin_2006)

new_bin_2005=0

for x in new_content:
    if '05' in x:
        new_bin_2005 = new_bin_2005+1
    else:
        new_bin_2005 = new_bin_2005

#print(new_bin_2005)

a=[]

for x in range(bin_2018):
    a.append(2018)

for x in range(bin_2017):
    a.append(2017)
    
for x in range(bin_2016):
    a.append(2016)

for x in range(bin_2015):
    a.append(2015)
    
for x in range(bin_2014):
    a.append(2014)
    
for x in range(bin_2013):
    a.append(2013)
    
for x in range(bin_2012):
    a.append(2012)
    
for x in range(bin_2011):
    a.append(2011)
    
for x in range(bin_2010):
    a.append(2010)
    
for x in range(bin_2009):
    a.append(2009)
    
for x in range(bin_2008):
    a.append(2008)

for x in range(bin_2007):
    a.append(2007)
    
for x in range(bin_2006):
    a.append(2006)

for x in range(bin_2005):
    a.append(2005)

c=[]

for x in range(new_bin_2018):
    c.append(2018)

for x in range(new_bin_2017):
    c.append(2017)
    
for x in range(new_bin_2016):
    c.append(2016)

for x in range(new_bin_2015):
    c.append(2015)
    
for x in range(new_bin_2014):
    c.append(2014)
    
for x in range(new_bin_2013):
    c.append(2013)
    
for x in range(new_bin_2012):
    c.append(2012)
    
for x in range(new_bin_2011):
    c.append(2011)
    
for x in range(new_bin_2010):
    c.append(2010)
    
for x in range(new_bin_2009):
    c.append(2009)
    
for x in range(new_bin_2008):
    c.append(2008)

for x in range(new_bin_2007):
    c.append(2007)
    
for x in range(new_bin_2006):
    c.append(2006)

for x in range(new_bin_2005):
    c.append(2005)


b = np.arange(2005,2020, 1)

plt.hist(a,b, histtype='bar', rwidth=0.8, label="Swift Satellite")
plt.hist(c,b, histtype='bar', rwidth=0.8, label="Non Swift Satellite")
plt.title("Supernovae Captured by Satellites Each Year")
plt.legend(loc='upper left')
plt.xlabel("Year")
plt.xlim(left=2005)
plt.xlim(right=2019)
plt.xticks(b)
plt.ylabel("Number of Supernovae")
plt.show()
