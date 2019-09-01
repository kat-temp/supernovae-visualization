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
        if "inPGC" in x:
                content.remove(x)

bin_2019=0

for x in content:
    if '19' in x:
        bin_2019 = bin_2019+1
    else:
        bin_2019 = bin_2019

#print(bin_2019)


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

print(new_bin_2018)

new_bin_2017=0

for x in new_content:
    if '2017' in x:
        new_bin_2017 = new_bin_2017+1
    else:
        new_bin_2017 = new_bin_2017

print(new_bin_2017)

new_bin_2016=0

for x in new_content:
    if '16' in x:
        new_bin_2016 = new_bin_2016+1
    else:
        new_bin_2016 = new_bin_2016

print(new_bin_2016)

new_bin_2015=0

for x in new_content:
    if '15' in x:
        new_bin_2015 = new_bin_2015+1
    else:
        new_bin_2015 = new_bin_2015

print(new_bin_2015)

new_bin_2014=0

for x in new_content:
    if '14' in x:
        new_bin_2014 = new_bin_2014+1
    else:
        new_bin_2014 = new_bin_2014

print(new_bin_2014)

new_bin_2013=0

for x in new_content:
    if '13' in x:
        new_bin_2013 = new_bin_2013+1
    else:
        new_bin_2013 = new_bin_2013

print(new_bin_2013)

new_bin_2012=0

for x in new_content:
    if '12' in x:
        new_bin_2012 = new_bin_2012+1
    else:
        new_bin_2012 = new_bin_2012

print(new_bin_2012)

new_bin_2011=0

for x in new_content:
    if '11' in x:
        new_bin_2011 = new_bin_2011+1
    else:
        new_bin_2011 = new_bin_2011

print(new_bin_2011)

new_bin_2010=0

for x in new_content:
    if '2010' in x:
        new_bin_2010 = new_bin_2010+1
    else:
        new_bin_2010 = new_bin_2010

print(new_bin_2010)

new_bin_2009=0

for x in new_content:
    if '09' in x:
        new_bin_2009 = new_bin_2009+1
    else:
        new_bin_2009 = new_bin_2009

print(new_bin_2009)

new_bin_2008=0

for x in new_content:
    if '08' in x:
        new_bin_2008 = new_bin_2008+1
    else:
        new_bin_2008 = new_bin_2008

print(new_bin_2008)

new_bin_2007=0

for x in new_content:
    if '07' in x:
        new_bin_2007 = new_bin_2007+1
    else:
        new_bin_2007 = new_bin_2007

print(new_bin_2007)

new_bin_2006=0

for x in new_content:
    if '06' in x:
        new_bin_2006 = new_bin_2006+1
    else:
        new_bin_2006 = new_bin_2006

print(new_bin_2006)

new_bin_2005=0

for x in new_content:
    if '05' in x:
        new_bin_2005 = new_bin_2005+1
    else:
        new_bin_2005 = new_bin_2005

print(new_bin_2005)

new_bin_2004=0

for x in new_content:
    if '04' in x:
        new_bin_2004 = new_bin_2004+1
    else:
        new_bin_2004 = new_bin_2004

print(new_bin_2004)

new_bin_2003=0

for x in new_content:
    if '03' in x:
        new_bin_2003 = new_bin_2003+1
    else:
        new_bin_2003 = new_bin_2003

print(new_bin_2003)

new_bin_2002=0

for x in new_content:
    if '02' in x:
        new_bin_2002 = new_bin_2002+1
    else:
        new_bin_2002 = new_bin_2002

print(new_bin_2002)

new_bin_2001=0

for x in new_content:
    if '2001' in x:
        new_bin_2001 = new_bin_2001+1
    else:
        new_bin_2001 = new_bin_2001

print(new_bin_2001)

new_bin_2000=0

for x in new_content:
    if '2000' in x:
        new_bin_2000 = new_bin_2000+1
    else:
        new_bin_2000 = new_bin_2000

print(new_bin_2000)

new_bin_1999=0

for x in new_content:
    if '1999' in x:
        new_bin_1999 = new_bin_1999+1
    else:
        new_bin_1999 = new_bin_1999

print(new_bin_1999)

new_bin_1998=0

for x in new_content:
    if '1998' in x:
        new_bin_1998 = new_bin_1998+1
    else:
        new_bin_1998 = new_bin_1998

print(new_bin_1998)

new_bin_1997=0

for x in new_content:
    if '1997' in x:
        new_bin_1997 = new_bin_1997+1
    else:
        new_bin_1997 = new_bin_1997

print(new_bin_1997)

new_bin_1996=0

for x in new_content:
    if '1996' in x:
        new_bin_1996 = new_bin_1996+1
    else:
        new_bin_1996 = new_bin_1996

print(new_bin_1996)

new_bin_1995=0

for x in new_content:
    if '1995' in x:
        new_bin_1995 = new_bin_1995+1
    else:
        new_bin_1995 = new_bin_1995

print(new_bin_1995)

new_bin_1994=0

for x in new_content:
    if '1994' in x:
        new_bin_1994 = new_bin_1994+1
    else:
        new_bin_1994 = new_bin_1994

print(new_bin_1994)

new_bin_1993=0

for x in new_content:
    if '1993' in x:
        new_bin_1993 = new_bin_1993+1
    else:
        new_bin_1993 = new_bin_1993

print(new_bin_1993)

new_bin_1992=0

for x in new_content:
    if '1992' in x:
        new_bin_1992 = new_bin_1992+1
    else:
        new_bin_1992 = new_bin_1992

print(new_bin_1992)

new_bin_1991=0

for x in new_content:
    if '1991' in x:
        new_bin_1991 = new_bin_1991+1
    else:
        new_bin_1991 = new_bin_1991

print(new_bin_1991)

new_bin_1990=0

for x in new_content:
    if '1990' in x:
        new_bin_1990 = new_bin_1990+1
    else:
        new_bin_1990 = new_bin_1990

print(new_bin_1990)

new_bin_1989=0

for x in new_content:
    if '1989' in x:
        new_bin_1989 = new_bin_1989+1
    else:
        new_bin_1989 = new_bin_1989

print(new_bin_1989)

new_bin_1988=0

for x in new_content:
    if '1988' in x:
        new_bin_1988 = new_bin_1988+1
    else:
        new_bin_1988 = new_bin_1988

print(new_bin_1988)

new_bin_1987=0

for x in new_content:
    if '1987' in x:
        new_bin_1987 = new_bin_1987+1
    else:
        new_bin_1987 = new_bin_1987

print(new_bin_1987)

new_bin_1986=0

for x in new_content:
    if '1986' in x:
        new_bin_1986 = new_bin_1986+1
    else:
        new_bin_1986 = new_bin_1986

print(new_bin_1986)

new_bin_1985=0

for x in new_content:
    if '1985' in x:
        new_bin_1985 = new_bin_1985+1
    else:
        new_bin_1985 = new_bin_1985

print(new_bin_1985)

new_bin_1984=0

for x in new_content:
    if '1984' in x:
        new_bin_1984 = new_bin_1984+1
    else:
        new_bin_1984 = new_bin_1984

print(new_bin_1984)

new_bin_1983=0

for x in new_content:
    if '1983' in x:
        new_bin_1983 = new_bin_1983+1
    else:
        new_bin_1983 = new_bin_1983

print(new_bin_1983)

new_bin_1982=0

for x in new_content:
    if '1982' in x:
        new_bin_1982 = new_bin_1982+1
    else:
        new_bin_1982 = new_bin_1982

print(new_bin_1982)

new_bin_1981=0

for x in new_content:
    if '1981' in x:
        new_bin_1981 = new_bin_1981+1
    else:
        new_bin_1981 = new_bin_1981

print(new_bin_1981)

new_bin_1980=0

for x in new_content:
    if '1980' in x:
        new_bin_1980 = new_bin_1980+1
    else:
        new_bin_1980 = new_bin_1980

print(new_bin_1980)

new_bin_1979=0

for x in new_content:
    if '1979' in x:
        new_bin_1979 = new_bin_1979+1
    else:
        new_bin_1979 = new_bin_1979

print(new_bin_1979)

new_bin_1978=0

for x in new_content:
    if '1978' in x:
        new_bin_1978 = new_bin_1978+1
    else:
        new_bin_1978 = new_bin_1978

print(new_bin_1978)

new_bin_1972=0

for x in new_content:
    if '1972' in x:
        new_bin_1972 = new_bin_1972+1
    else:
        new_bin_1972 = new_bin_1972

print(new_bin_1972)


a=[]

for x in range(bin_2019):
    a.append(2019)

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

for x in range(new_bin_2004):
    c.append(2004)

for x in range(new_bin_2003):
    c.append(2003)

for x in range(new_bin_2002):
    c.append(2002)

for x in range(new_bin_2001):
    c.append(2001)

for x in range(new_bin_2000):
    c.append(2000)

for x in range(new_bin_1999):
    c.append(1999)

for x in range(new_bin_1998):
    c.append(1998)

for x in range(new_bin_1997):
    c.append(1997)

for x in range(new_bin_1996):
    c.append(1996)

for x in range(new_bin_1995):
    c.append(1995)

for x in range(new_bin_1994):
    c.append(1994)

for x in range(new_bin_1993):
    c.append(1993)

for x in range(new_bin_1992):
    c.append(1992)

for x in range(new_bin_1991):
    c.append(1991)

for x in range(new_bin_1990):
    c.append(1990)

for x in range(new_bin_1989):
    c.append(1989)

for x in range(new_bin_1988):
    c.append(1988)

for x in range(new_bin_1987):
    c.append(1987)

for x in range(new_bin_1986):
    c.append(1986)

for x in range(new_bin_1985):
    c.append(1985)

for x in range(new_bin_1984):
    c.append(1984)

for x in range(new_bin_1983):
    c.append(1983)

for x in range(new_bin_1982):
    c.append(1982)

for x in range(new_bin_1981):
    c.append(1981)

for x in range(new_bin_1980):
    c.append(1980)

for x in range(new_bin_1979):
    c.append(1979)

for x in range(new_bin_1978):
    c.append(1978)

for x in range(new_bin_1972):
    c.append(1972)



b = np.arange(1971,2021, 1)

plt.hist(a,b, histtype='bar', rwidth=0.8, label="Swift Satellite")
plt.hist(c,b, histtype='bar', rwidth=0.8, label="Non Swift Satellite")
plt.title("Supernovae Captured by Satellites Each Year")
plt.legend(loc='upper left')
plt.xlabel("Year")
plt.xlim(left=1971)
plt.xlim(right=2021)
plt.xticks(np.arange(1971,2021,3))
plt.ylabel("Number of Supernovae")
plt.show()
