import matplotlib.pyplot as plt
import numpy as np

#with open('SNnames.txt') as f:
#    content= f.readlines()

with open('nonSNnames.txt') as g:
    new_content= g.readlines()

#content=[x.strip() for x in content]
new_content=[x.strip() for x in new_content]
'''
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
'''
hst=[]
oao=[]
iue=[]
xmm=[]
galex=[]


for x in new_content:
    if 'HST' in x:
        hst.append(x)

for x in new_content:
    if 'OAO' in x:
        oao.append(x)

for x in new_content:
    if 'IUE' in x:
        iue.append(x)

for x in new_content:
    if 'XMM' in x:
        xmm.append(x)

for x in new_content:
    if 'GALEX' in x:
        galex.append(x)


hst_bin_2018=0

for x in hst:
    if '18' in x:
        hst_bin_2018 = hst_bin_2018+1
    else:
        hst_bin_2018 = hst_bin_2018

print(hst_bin_2018)

hst_bin_2017=0

for x in hst:
    if '2017' in x:
        hst_bin_2017 = hst_bin_2017+1
    else:
        hst_bin_2017 = hst_bin_2017

print(hst_bin_2017)

hst_bin_2016=0

for x in hst:
    if '16' in x:
        hst_bin_2016 = hst_bin_2016+1
    else:
        hst_bin_2016 = hst_bin_2016

print(hst_bin_2016)

hst_bin_2015=0

for x in hst:
    if '15' in x:
        hst_bin_2015 = hst_bin_2015+1
    else:
        hst_bin_2015 = hst_bin_2015

print(hst_bin_2015)

hst_bin_2014=0

for x in hst:
    if '14' in x:
        hst_bin_2014 = hst_bin_2014+1
    else:
        hst_bin_2014 = hst_bin_2014

print(hst_bin_2014)

hst_bin_2013=0

for x in hst:
    if '13' in x:
        hst_bin_2013 = hst_bin_2013+1
    else:
        hst_bin_2013 = hst_bin_2013

print(hst_bin_2013)

hst_bin_2012=0

for x in hst:
    if '12' in x:
        hst_bin_2012 = hst_bin_2012+1
    else:
        hst_bin_2012 = hst_bin_2012

print(hst_bin_2012)

hst_bin_2011=0

for x in hst:
    if '11' in x:
        hst_bin_2011 = hst_bin_2011+1
    else:
        hst_bin_2011 = hst_bin_2011

print(hst_bin_2011)

hst_bin_2010=0

for x in hst:
    if '2010' in x:
        hst_bin_2010 = hst_bin_2010+1
    else:
        hst_bin_2010 = hst_bin_2010

print(hst_bin_2010)

hst_bin_2009=0

for x in hst:
    if '09' in x:
        hst_bin_2009 = hst_bin_2009+1
    else:
        hst_bin_2009 = hst_bin_2009

print(hst_bin_2009)

hst_bin_2008=0

for x in hst:
    if '08' in x:
        hst_bin_2008 = hst_bin_2008+1
    else:
        hst_bin_2008 = hst_bin_2008

print(hst_bin_2008)

hst_bin_2007=0

for x in hst:
    if '07' in x:
        hst_bin_2007 = hst_bin_2007+1
    else:
        hst_bin_2007 = hst_bin_2007

print(hst_bin_2007)

hst_bin_2006=0

for x in hst:
    if '06' in x:
        hst_bin_2006 = hst_bin_2006+1
    else:
        hst_bin_2006 = hst_bin_2006

print(hst_bin_2006)

hst_bin_2005=0

for x in hst:
    if '05' in x:
        hst_bin_2005 = hst_bin_2005+1
    else:
        hst_bin_2005 = hst_bin_2005

print(hst_bin_2005)

hst_bin_2004=0

for x in hst:
    if '04' in x:
        hst_bin_2004 = hst_bin_2004+1
    else:
        hst_bin_2004 = hst_bin_2004

print(hst_bin_2004)

hst_bin_2003=0

for x in hst:
    if '03' in x:
        hst_bin_2003 = hst_bin_2003+1
    else:
        hst_bin_2003 = hst_bin_2003

print(hst_bin_2003)

hst_bin_2002=0

for x in hst:
    if '02' in x:
        hst_bin_2002 = hst_bin_2002+1
    else:
        hst_bin_2002 = hst_bin_2002

print(hst_bin_2002)

hst_bin_2001=0

for x in hst:
    if '2001' in x:
        hst_bin_2001 = hst_bin_2001+1
    else:
        hst_bin_2001 = hst_bin_2001

print(hst_bin_2001)

hst_bin_2000=0

for x in hst:
    if '2000' in x:
        hst_bin_2000 = hst_bin_2000+1
    else:
        hst_bin_2000 = hst_bin_2000

print(hst_bin_2000)

hst_bin_1999=0

for x in hst:
    if '1999' in x:
        hst_bin_1999 = hst_bin_1999+1
    else:
        hst_bin_1999 = hst_bin_1999

print(hst_bin_1999)

hst_bin_1998=0

for x in hst:
    if '1998' in x:
        hst_bin_1998 = hst_bin_1998+1
    else:
        hst_bin_1998 = hst_bin_1998

print(hst_bin_1998)

hst_bin_1997=0

for x in hst:
    if '1997' in x:
        hst_bin_1997 = hst_bin_1997+1
    else:
        hst_bin_1997 = hst_bin_1997

print(hst_bin_1997)

hst_bin_1996=0

for x in hst:
    if '1996' in x:
        hst_bin_1996 = hst_bin_1996+1
    else:
        hst_bin_1996 = hst_bin_1996

print(hst_bin_1996)

hst_bin_1995=0

for x in hst:
    if '1995' in x:
        hst_bin_1995 = hst_bin_1995+1
    else:
        hst_bin_1995 = hst_bin_1995

print(hst_bin_1995)

hst_bin_1994=0

for x in hst:
    if '1994' in x:
        hst_bin_1994 = hst_bin_1994+1
    else:
        hst_bin_1994 = hst_bin_1994

print(hst_bin_1994)

hst_bin_1993=0

for x in hst:
    if '1993' in x:
        hst_bin_1993 = hst_bin_1993+1
    else:
        hst_bin_1993 = hst_bin_1993

print(hst_bin_1993)

hst_bin_1992=0

for x in hst:
    if '1992' in x:
        hst_bin_1992 = hst_bin_1992+1
    else:
        hst_bin_1992 = hst_bin_1992

print(hst_bin_1992)

hst_bin_1991=0

for x in hst:
    if '1991' in x:
        hst_bin_1991 = hst_bin_1991+1
    else:
        hst_bin_1991 = hst_bin_1991

print(hst_bin_1991)

hst_bin_1990=0

for x in hst:
    if '1990' in x:
        hst_bin_1990 = hst_bin_1990+1
    else:
        hst_bin_1990 = hst_bin_1990

print(hst_bin_1990)

hst_bin_1989=0

for x in hst:
    if '1989' in x:
        hst_bin_1989 = hst_bin_1989+1
    else:
        hst_bin_1989 = hst_bin_1989

print(hst_bin_1989)

hst_bin_1988=0

for x in hst:
    if '1988' in x:
        hst_bin_1988 = hst_bin_1988+1
    else:
        hst_bin_1988 = hst_bin_1988

print(hst_bin_1988)

hst_bin_1987=0

for x in hst:
    if '1987' in x:
        hst_bin_1987 = hst_bin_1987+1
    else:
        hst_bin_1987 = hst_bin_1987

print(hst_bin_1987)

hst_bin_1986=0

for x in hst:
    if '1986' in x:
        hst_bin_1986 = hst_bin_1986+1
    else:
        hst_bin_1986 = hst_bin_1986

print(hst_bin_1986)

hst_bin_1985=0

for x in hst:
    if '1985' in x:
        hst_bin_1985 = hst_bin_1985+1
    else:
        hst_bin_1985 = hst_bin_1985

print(hst_bin_1985)

hst_bin_1984=0

for x in hst:
    if '1984' in x:
        hst_bin_1984 = hst_bin_1984+1
    else:
        hst_bin_1984 = hst_bin_1984

print(hst_bin_1984)

hst_bin_1983=0

for x in hst:
    if '1983' in x:
        hst_bin_1983 = hst_bin_1983+1
    else:
        hst_bin_1983 = hst_bin_1983

print(hst_bin_1983)

hst_bin_1982=0

for x in hst:
    if '1982' in x:
        hst_bin_1982 = hst_bin_1982+1
    else:
        hst_bin_1982 = hst_bin_1982

print(hst_bin_1982)

hst_bin_1981=0

for x in hst:
    if '1981' in x:
        hst_bin_1981 = hst_bin_1981+1
    else:
        hst_bin_1981 = hst_bin_1981

print(hst_bin_1981)

hst_bin_1980=0

for x in hst:
    if '1980' in x:
        hst_bin_1980 = hst_bin_1980+1
    else:
        hst_bin_1980 = hst_bin_1980

print(hst_bin_1980)

hst_bin_1979=0

for x in hst:
    if '1979' in x:
        hst_bin_1979 = hst_bin_1979+1
    else:
        hst_bin_1979 = hst_bin_1979

print(hst_bin_1979)

hst_bin_1978=0

for x in hst:
    if '1978' in x:
        hst_bin_1978 = hst_bin_1978+1
    else:
        hst_bin_1978 = hst_bin_1978

print(hst_bin_1978)

hst_bin_1972=0

for x in hst:
    if '1972' in x:
        hst_bin_1972 = hst_bin_1972+1
    else:
        hst_bin_1972 = hst_bin_1972

print(hst_bin_1972)


oao_bin_2018=0

for x in oao:
    if '18' in x:
        oao_bin_2018 = oao_bin_2018+1
    else:
        oao_bin_2018 = oao_bin_2018

print(oao_bin_2018)

oao_bin_2017=0

for x in oao:
    if '2017' in x:
        oao_bin_2017 = oao_bin_2017+1
    else:
        oao_bin_2017 = oao_bin_2017

print(oao_bin_2017)

oao_bin_2016=0

for x in oao:
    if '16' in x:
        oao_bin_2016 = oao_bin_2016+1
    else:
        oao_bin_2016 = oao_bin_2016

print(oao_bin_2016)

oao_bin_2015=0

for x in oao:
    if '15' in x:
        oao_bin_2015 = oao_bin_2015+1
    else:
        oao_bin_2015 = oao_bin_2015

print(oao_bin_2015)

oao_bin_2014=0

for x in oao:
    if '14' in x:
        oao_bin_2014 = oao_bin_2014+1
    else:
        oao_bin_2014 = oao_bin_2014

print(oao_bin_2014)

oao_bin_2013=0

for x in oao:
    if '13' in x:
        oao_bin_2013 = oao_bin_2013+1
    else:
        oao_bin_2013 = oao_bin_2013

print(oao_bin_2013)

oao_bin_2012=0

for x in oao:
    if '12' in x:
        oao_bin_2012 = oao_bin_2012+1
    else:
        oao_bin_2012 = oao_bin_2012

print(oao_bin_2012)

oao_bin_2011=0

for x in oao:
    if '11' in x:
        oao_bin_2011 = oao_bin_2011+1
    else:
        oao_bin_2011 = oao_bin_2011

print(oao_bin_2011)

oao_bin_2010=0

for x in oao:
    if '2010' in x:
        oao_bin_2010 = oao_bin_2010+1
    else:
        oao_bin_2010 = oao_bin_2010

print(oao_bin_2010)

oao_bin_2009=0

for x in oao:
    if '09' in x:
        oao_bin_2009 = oao_bin_2009+1
    else:
        oao_bin_2009 = oao_bin_2009

print(oao_bin_2009)

oao_bin_2008=0

for x in oao:
    if '08' in x:
        oao_bin_2008 = oao_bin_2008+1
    else:
        oao_bin_2008 = oao_bin_2008

print(oao_bin_2008)

oao_bin_2007=0

for x in oao:
    if '07' in x:
        oao_bin_2007 = oao_bin_2007+1
    else:
        oao_bin_2007 = oao_bin_2007

print(oao_bin_2007)

oao_bin_2006=0

for x in oao:
    if '06' in x:
        oao_bin_2006 = oao_bin_2006+1
    else:
        oao_bin_2006 = oao_bin_2006

print(oao_bin_2006)

oao_bin_2005=0

for x in oao:
    if '05' in x:
        oao_bin_2005 = oao_bin_2005+1
    else:
        oao_bin_2005 = oao_bin_2005

print(oao_bin_2005)

oao_bin_2004=0

for x in oao:
    if '04' in x:
        oao_bin_2004 = oao_bin_2004+1
    else:
        oao_bin_2004 = oao_bin_2004

print(oao_bin_2004)

oao_bin_2003=0

for x in oao:
    if '03' in x:
        oao_bin_2003 = oao_bin_2003+1
    else:
        oao_bin_2003 = oao_bin_2003

print(oao_bin_2003)

oao_bin_2002=0

for x in oao:
    if '02' in x:
        oao_bin_2002 = oao_bin_2002+1
    else:
        oao_bin_2002 = oao_bin_2002

print(oao_bin_2002)

oao_bin_2001=0

for x in oao:
    if '2001' in x:
        oao_bin_2001 = oao_bin_2001+1
    else:
        oao_bin_2001 = oao_bin_2001

print(oao_bin_2001)

oao_bin_2000=0

for x in oao:
    if '2000' in x:
        oao_bin_2000 = oao_bin_2000+1
    else:
        oao_bin_2000 = oao_bin_2000

print(oao_bin_2000)

oao_bin_1999=0

for x in oao:
    if '1999' in x:
        oao_bin_1999 = oao_bin_1999+1
    else:
        oao_bin_1999 = oao_bin_1999

print(oao_bin_1999)

oao_bin_1998=0

for x in oao:
    if '1998' in x:
        oao_bin_1998 = oao_bin_1998+1
    else:
        oao_bin_1998 = oao_bin_1998

print(oao_bin_1998)

oao_bin_1997=0

for x in oao:
    if '1997' in x:
        oao_bin_1997 = oao_bin_1997+1
    else:
        oao_bin_1997 = oao_bin_1997

print(oao_bin_1997)

oao_bin_1996=0

for x in oao:
    if '1996' in x:
        oao_bin_1996 = oao_bin_1996+1
    else:
        oao_bin_1996 = oao_bin_1996

print(oao_bin_1996)

oao_bin_1995=0

for x in oao:
    if '1995' in x:
        oao_bin_1995 = oao_bin_1995+1
    else:
        oao_bin_1995 = oao_bin_1995

print(oao_bin_1995)

oao_bin_1994=0

for x in oao:
    if '1994' in x:
        oao_bin_1994 = oao_bin_1994+1
    else:
        oao_bin_1994 = oao_bin_1994

print(oao_bin_1994)

oao_bin_1993=0

for x in oao:
    if '1993' in x:
        oao_bin_1993 = oao_bin_1993+1
    else:
        oao_bin_1993 = oao_bin_1993

print(oao_bin_1993)

oao_bin_1992=0

for x in oao:
    if '1992' in x:
        oao_bin_1992 = oao_bin_1992+1
    else:
        oao_bin_1992 = oao_bin_1992

print(oao_bin_1992)

oao_bin_1991=0

for x in oao:
    if '1991' in x:
        oao_bin_1991 = oao_bin_1991+1
    else:
        oao_bin_1991 = oao_bin_1991

print(oao_bin_1991)

oao_bin_1990=0

for x in oao:
    if '1990' in x:
        oao_bin_1990 = oao_bin_1990+1
    else:
        oao_bin_1990 = oao_bin_1990

print(oao_bin_1990)

oao_bin_1989=0

for x in oao:
    if '1989' in x:
        oao_bin_1989 = oao_bin_1989+1
    else:
        oao_bin_1989 = oao_bin_1989

print(oao_bin_1989)

oao_bin_1988=0

for x in oao:
    if '1988' in x:
        oao_bin_1988 = oao_bin_1988+1
    else:
        oao_bin_1988 = oao_bin_1988

print(oao_bin_1988)

oao_bin_1987=0

for x in oao:
    if '1987' in x:
        oao_bin_1987 = oao_bin_1987+1
    else:
        oao_bin_1987 = oao_bin_1987

print(oao_bin_1987)

oao_bin_1986=0

for x in oao:
    if '1986' in x:
        oao_bin_1986 = oao_bin_1986+1
    else:
        oao_bin_1986 = oao_bin_1986

print(oao_bin_1986)

oao_bin_1985=0

for x in oao:
    if '1985' in x:
        oao_bin_1985 = oao_bin_1985+1
    else:
        oao_bin_1985 = oao_bin_1985

print(oao_bin_1985)

oao_bin_1984=0

for x in oao:
    if '1984' in x:
        oao_bin_1984 = oao_bin_1984+1
    else:
        oao_bin_1984 = oao_bin_1984

print(oao_bin_1984)

oao_bin_1983=0

for x in oao:
    if '1983' in x:
        oao_bin_1983 = oao_bin_1983+1
    else:
        oao_bin_1983 = oao_bin_1983

print(oao_bin_1983)

oao_bin_1982=0

for x in oao:
    if '1982' in x:
        oao_bin_1982 = oao_bin_1982+1
    else:
        oao_bin_1982 = oao_bin_1982

print(oao_bin_1982)

oao_bin_1981=0

for x in oao:
    if '1981' in x:
        oao_bin_1981 = oao_bin_1981+1
    else:
        oao_bin_1981 = oao_bin_1981

print(oao_bin_1981)

oao_bin_1980=0

for x in oao:
    if '1980' in x:
        oao_bin_1980 = oao_bin_1980+1
    else:
        oao_bin_1980 = oao_bin_1980

print(oao_bin_1980)

oao_bin_1979=0

for x in oao:
    if '1979' in x:
        oao_bin_1979 = oao_bin_1979+1
    else:
        oao_bin_1979 = oao_bin_1979

print(oao_bin_1979)

oao_bin_1978=0

for x in oao:
    if '1978' in x:
        oao_bin_1978 = oao_bin_1978+1
    else:
        oao_bin_1978 = oao_bin_1978

print(oao_bin_1978)

oao_bin_1972=0

for x in oao:
    if '1972' in x:
        oao_bin_1972 = oao_bin_1972+1
    else:
        oao_bin_1972 = oao_bin_1972

print(oao_bin_1972)


iue_bin_2018=0

for x in iue:
    if '18' in x:
        iue_bin_2018 = iue_bin_2018+1
    else:
        iue_bin_2018 = iue_bin_2018

print(iue_bin_2018)

iue_bin_2017=0

for x in iue:
    if '2017' in x:
        iue_bin_2017 = iue_bin_2017+1
    else:
        iue_bin_2017 = iue_bin_2017

print(iue_bin_2017)

iue_bin_2016=0

for x in iue:
    if '16' in x:
        iue_bin_2016 = iue_bin_2016+1
    else:
        iue_bin_2016 = iue_bin_2016

print(iue_bin_2016)

iue_bin_2015=0

for x in iue:
    if '15' in x:
        iue_bin_2015 = iue_bin_2015+1
    else:
        iue_bin_2015 = iue_bin_2015

print(iue_bin_2015)

iue_bin_2014=0

for x in iue:
    if '14' in x:
        iue_bin_2014 = iue_bin_2014+1
    else:
        iue_bin_2014 = iue_bin_2014

print(iue_bin_2014)

iue_bin_2013=0

for x in iue:
    if '13' in x:
        iue_bin_2013 = iue_bin_2013+1
    else:
        iue_bin_2013 = iue_bin_2013

print(iue_bin_2013)

iue_bin_2012=0

for x in iue:
    if '12' in x:
        iue_bin_2012 = iue_bin_2012+1
    else:
        iue_bin_2012 = iue_bin_2012

print(iue_bin_2012)

iue_bin_2011=0

for x in iue:
    if '11' in x:
        iue_bin_2011 = iue_bin_2011+1
    else:
        iue_bin_2011 = iue_bin_2011

print(iue_bin_2011)

iue_bin_2010=0

for x in iue:
    if '2010' in x:
        iue_bin_2010 = iue_bin_2010+1
    else:
        iue_bin_2010 = iue_bin_2010

print(iue_bin_2010)

iue_bin_2009=0

for x in iue:
    if '09' in x:
        iue_bin_2009 = iue_bin_2009+1
    else:
        iue_bin_2009 = iue_bin_2009

print(iue_bin_2009)

iue_bin_2008=0

for x in iue:
    if '08' in x:
        iue_bin_2008 = iue_bin_2008+1
    else:
        iue_bin_2008 = iue_bin_2008

print(iue_bin_2008)

iue_bin_2007=0

for x in iue:
    if '07' in x:
        iue_bin_2007 = iue_bin_2007+1
    else:
        iue_bin_2007 = iue_bin_2007

print(iue_bin_2007)

iue_bin_2006=0

for x in iue:
    if '06' in x:
        iue_bin_2006 = iue_bin_2006+1
    else:
        iue_bin_2006 = iue_bin_2006

print(iue_bin_2006)

iue_bin_2005=0

for x in iue:
    if '05' in x:
        iue_bin_2005 = iue_bin_2005+1
    else:
        iue_bin_2005 = iue_bin_2005

print(iue_bin_2005)

iue_bin_2004=0

for x in iue:
    if '04' in x:
        iue_bin_2004 = iue_bin_2004+1
    else:
        iue_bin_2004 = iue_bin_2004

print(iue_bin_2004)

iue_bin_2003=0

for x in iue:
    if '03' in x:
        iue_bin_2003 = iue_bin_2003+1
    else:
        iue_bin_2003 = iue_bin_2003

print(iue_bin_2003)

iue_bin_2002=0

for x in iue:
    if '02' in x:
        iue_bin_2002 = iue_bin_2002+1
    else:
        iue_bin_2002 = iue_bin_2002

print(iue_bin_2002)

iue_bin_2001=0

for x in iue:
    if '2001' in x:
        iue_bin_2001 = iue_bin_2001+1
    else:
        iue_bin_2001 = iue_bin_2001

print(iue_bin_2001)

iue_bin_2000=0

for x in iue:
    if '2000' in x:
        iue_bin_2000 = iue_bin_2000+1
    else:
        iue_bin_2000 = iue_bin_2000

print(iue_bin_2000)

iue_bin_1999=0

for x in iue:
    if '1999' in x:
        iue_bin_1999 = iue_bin_1999+1
    else:
        iue_bin_1999 = iue_bin_1999

print(iue_bin_1999)

iue_bin_1998=0

for x in iue:
    if '1998' in x:
        iue_bin_1998 = iue_bin_1998+1
    else:
        iue_bin_1998 = iue_bin_1998

print(iue_bin_1998)

iue_bin_1997=0

for x in iue:
    if '1997' in x:
        iue_bin_1997 = iue_bin_1997+1
    else:
        iue_bin_1997 = iue_bin_1997

print(iue_bin_1997)

iue_bin_1996=0

for x in iue:
    if '1996' in x:
        iue_bin_1996 = iue_bin_1996+1
    else:
        iue_bin_1996 = iue_bin_1996

print(iue_bin_1996)

iue_bin_1995=0

for x in iue:
    if '1995' in x:
        iue_bin_1995 = iue_bin_1995+1
    else:
        iue_bin_1995 = iue_bin_1995

print(iue_bin_1995)

iue_bin_1994=0

for x in iue:
    if '1994' in x:
        iue_bin_1994 = iue_bin_1994+1
    else:
        iue_bin_1994 = iue_bin_1994

print(iue_bin_1994)

iue_bin_1993=0

for x in iue:
    if '1993' in x:
        iue_bin_1993 = iue_bin_1993+1
    else:
        iue_bin_1993 = iue_bin_1993

print(iue_bin_1993)

iue_bin_1992=0

for x in iue:
    if '1992' in x:
        iue_bin_1992 = iue_bin_1992+1
    else:
        iue_bin_1992 = iue_bin_1992

print(iue_bin_1992)

iue_bin_1991=0

for x in iue:
    if '1991' in x:
        iue_bin_1991 = iue_bin_1991+1
    else:
        iue_bin_1991 = iue_bin_1991

print(iue_bin_1991)

iue_bin_1990=0

for x in iue:
    if '1990' in x:
        iue_bin_1990 = iue_bin_1990+1
    else:
        iue_bin_1990 = iue_bin_1990

print(iue_bin_1990)

iue_bin_1989=0

for x in iue:
    if '1989' in x:
        iue_bin_1989 = iue_bin_1989+1
    else:
        iue_bin_1989 = iue_bin_1989

print(iue_bin_1989)

iue_bin_1988=0

for x in iue:
    if '1988' in x:
        iue_bin_1988 = iue_bin_1988+1
    else:
        iue_bin_1988 = iue_bin_1988

print(iue_bin_1988)

iue_bin_1987=0

for x in iue:
    if '1987' in x:
        iue_bin_1987 = iue_bin_1987+1
    else:
        iue_bin_1987 = iue_bin_1987

print(iue_bin_1987)

iue_bin_1986=0

for x in iue:
    if '1986' in x:
        iue_bin_1986 = iue_bin_1986+1
    else:
        iue_bin_1986 = iue_bin_1986

print(iue_bin_1986)

iue_bin_1985=0

for x in iue:
    if '1985' in x:
        iue_bin_1985 = iue_bin_1985+1
    else:
        iue_bin_1985 = iue_bin_1985

print(iue_bin_1985)

iue_bin_1984=0

for x in iue:
    if '1984' in x:
        iue_bin_1984 = iue_bin_1984+1
    else:
        iue_bin_1984 = iue_bin_1984

print(iue_bin_1984)

iue_bin_1983=0

for x in iue:
    if '1983' in x:
        iue_bin_1983 = iue_bin_1983+1
    else:
        iue_bin_1983 = iue_bin_1983

print(iue_bin_1983)

iue_bin_1982=0

for x in iue:
    if '1982' in x:
        iue_bin_1982 = iue_bin_1982+1
    else:
        iue_bin_1982 = iue_bin_1982

print(iue_bin_1982)

iue_bin_1981=0

for x in iue:
    if '1981' in x:
        iue_bin_1981 = iue_bin_1981+1
    else:
        iue_bin_1981 = iue_bin_1981

print(iue_bin_1981)

iue_bin_1980=0

for x in iue:
    if '1980' in x:
        iue_bin_1980 = iue_bin_1980+1
    else:
        iue_bin_1980 = iue_bin_1980

print(iue_bin_1980)

iue_bin_1979=0

for x in iue:
    if '1979' in x:
        iue_bin_1979 = iue_bin_1979+1
    else:
        iue_bin_1979 = iue_bin_1979

print(iue_bin_1979)

iue_bin_1978=0

for x in iue:
    if '1978' in x:
        iue_bin_1978 = iue_bin_1978+1
    else:
        iue_bin_1978 = iue_bin_1978

print(iue_bin_1978)

iue_bin_1972=0

for x in iue:
    if '1972' in x:
        iue_bin_1972 = iue_bin_1972+1
    else:
        iue_bin_1972 = iue_bin_1972

print(iue_bin_1972)

xmm_bin_2018=0

for x in xmm:
    if '18' in x:
        xmm_bin_2018 = xmm_bin_2018+1
    else:
        xmm_bin_2018 = xmm_bin_2018

print(xmm_bin_2018)

xmm_bin_2017=0

for x in xmm:
    if '2017' in x:
        xmm_bin_2017 = xmm_bin_2017+1
    else:
        xmm_bin_2017 = xmm_bin_2017

print(xmm_bin_2017)

xmm_bin_2016=0

for x in xmm:
    if '16' in x:
        xmm_bin_2016 = xmm_bin_2016+1
    else:
        xmm_bin_2016 = xmm_bin_2016

print(xmm_bin_2016)

xmm_bin_2015=0

for x in xmm:
    if '15' in x:
        xmm_bin_2015 = xmm_bin_2015+1
    else:
        xmm_bin_2015 = xmm_bin_2015

print(xmm_bin_2015)

xmm_bin_2014=0

for x in xmm:
    if '14' in x:
        xmm_bin_2014 = xmm_bin_2014+1
    else:
        xmm_bin_2014 = xmm_bin_2014

print(xmm_bin_2014)

xmm_bin_2013=0

for x in xmm:
    if '13' in x:
        xmm_bin_2013 = xmm_bin_2013+1
    else:
        xmm_bin_2013 = xmm_bin_2013

print(xmm_bin_2013)

xmm_bin_2012=0

for x in xmm:
    if '12' in x:
        xmm_bin_2012 = xmm_bin_2012+1
    else:
        xmm_bin_2012 = xmm_bin_2012

print(xmm_bin_2012)

xmm_bin_2011=0

for x in xmm:
    if '11' in x:
        xmm_bin_2011 = xmm_bin_2011+1
    else:
        xmm_bin_2011 = xmm_bin_2011

print(xmm_bin_2011)

xmm_bin_2010=0

for x in xmm:
    if '2010' in x:
        xmm_bin_2010 = xmm_bin_2010+1
    else:
        xmm_bin_2010 = xmm_bin_2010

print(xmm_bin_2010)

xmm_bin_2009=0

for x in xmm:
    if '09' in x:
        xmm_bin_2009 = xmm_bin_2009+1
    else:
        xmm_bin_2009 = xmm_bin_2009

print(xmm_bin_2009)

xmm_bin_2008=0

for x in xmm:
    if '08' in x:
        xmm_bin_2008 = xmm_bin_2008+1
    else:
        xmm_bin_2008 = xmm_bin_2008

print(xmm_bin_2008)

xmm_bin_2007=0

for x in xmm:
    if '07' in x:
        xmm_bin_2007 = xmm_bin_2007+1
    else:
        xmm_bin_2007 = xmm_bin_2007

print(xmm_bin_2007)

xmm_bin_2006=0

for x in xmm:
    if '06' in x:
        xmm_bin_2006 = xmm_bin_2006+1
    else:
        xmm_bin_2006 = xmm_bin_2006

print(xmm_bin_2006)

xmm_bin_2005=0

for x in xmm:
    if '05' in x:
        xmm_bin_2005 = xmm_bin_2005+1
    else:
        xmm_bin_2005 = xmm_bin_2005

print(xmm_bin_2005)

xmm_bin_2004=0

for x in xmm:
    if '04' in x:
        xmm_bin_2004 = xmm_bin_2004+1
    else:
        xmm_bin_2004 = xmm_bin_2004

print(xmm_bin_2004)

xmm_bin_2003=0

for x in xmm:
    if '03' in x:
        xmm_bin_2003 = xmm_bin_2003+1
    else:
        xmm_bin_2003 = xmm_bin_2003

print(xmm_bin_2003)

xmm_bin_2002=0

for x in xmm:
    if '02' in x:
        xmm_bin_2002 = xmm_bin_2002+1
    else:
        xmm_bin_2002 = xmm_bin_2002

print(xmm_bin_2002)

xmm_bin_2001=0

for x in xmm:
    if '2001' in x:
        xmm_bin_2001 = xmm_bin_2001+1
    else:
        xmm_bin_2001 = xmm_bin_2001

print(xmm_bin_2001)

xmm_bin_2000=0

for x in xmm:
    if '2000' in x:
        xmm_bin_2000 = xmm_bin_2000+1
    else:
        xmm_bin_2000 = xmm_bin_2000

print(xmm_bin_2000)

xmm_bin_1999=0

for x in xmm:
    if '1999' in x:
        xmm_bin_1999 = xmm_bin_1999+1
    else:
        xmm_bin_1999 = xmm_bin_1999

print(xmm_bin_1999)

xmm_bin_1998=0

for x in xmm:
    if '1998' in x:
        xmm_bin_1998 = xmm_bin_1998+1
    else:
        xmm_bin_1998 = xmm_bin_1998

print(xmm_bin_1998)

xmm_bin_1997=0

for x in xmm:
    if '1997' in x:
        xmm_bin_1997 = xmm_bin_1997+1
    else:
        xmm_bin_1997 = xmm_bin_1997

print(xmm_bin_1997)

xmm_bin_1996=0

for x in xmm:
    if '1996' in x:
        xmm_bin_1996 = xmm_bin_1996+1
    else:
        xmm_bin_1996 = xmm_bin_1996

print(xmm_bin_1996)

xmm_bin_1995=0

for x in xmm:
    if '1995' in x:
        xmm_bin_1995 = xmm_bin_1995+1
    else:
        xmm_bin_1995 = xmm_bin_1995

print(xmm_bin_1995)

xmm_bin_1994=0

for x in xmm:
    if '1994' in x:
        xmm_bin_1994 = xmm_bin_1994+1
    else:
        xmm_bin_1994 = xmm_bin_1994

print(xmm_bin_1994)

xmm_bin_1993=0

for x in xmm:
    if '1993' in x:
        xmm_bin_1993 = xmm_bin_1993+1
    else:
        xmm_bin_1993 = xmm_bin_1993

print(xmm_bin_1993)

xmm_bin_1992=0

for x in xmm:
    if '1992' in x:
        xmm_bin_1992 = xmm_bin_1992+1
    else:
        xmm_bin_1992 = xmm_bin_1992

print(xmm_bin_1992)

xmm_bin_1991=0

for x in xmm:
    if '1991' in x:
        xmm_bin_1991 = xmm_bin_1991+1
    else:
        xmm_bin_1991 = xmm_bin_1991

print(xmm_bin_1991)

xmm_bin_1990=0

for x in xmm:
    if '1990' in x:
        xmm_bin_1990 = xmm_bin_1990+1
    else:
        xmm_bin_1990 = xmm_bin_1990

print(xmm_bin_1990)

xmm_bin_1989=0

for x in xmm:
    if '1989' in x:
        xmm_bin_1989 = xmm_bin_1989+1
    else:
        xmm_bin_1989 = xmm_bin_1989

print(xmm_bin_1989)

xmm_bin_1988=0

for x in xmm:
    if '1988' in x:
        xmm_bin_1988 = xmm_bin_1988+1
    else:
        xmm_bin_1988 = xmm_bin_1988

print(xmm_bin_1988)

xmm_bin_1987=0

for x in xmm:
    if '1987' in x:
        xmm_bin_1987 = xmm_bin_1987+1
    else:
        xmm_bin_1987 = xmm_bin_1987

print(xmm_bin_1987)

xmm_bin_1986=0

for x in xmm:
    if '1986' in x:
        xmm_bin_1986 = xmm_bin_1986+1
    else:
        xmm_bin_1986 = xmm_bin_1986

print(xmm_bin_1986)

xmm_bin_1985=0

for x in xmm:
    if '1985' in x:
        xmm_bin_1985 = xmm_bin_1985+1
    else:
        xmm_bin_1985 = xmm_bin_1985

print(xmm_bin_1985)

xmm_bin_1984=0

for x in xmm:
    if '1984' in x:
        xmm_bin_1984 = xmm_bin_1984+1
    else:
        xmm_bin_1984 = xmm_bin_1984

print(xmm_bin_1984)

xmm_bin_1983=0

for x in xmm:
    if '1983' in x:
        xmm_bin_1983 = xmm_bin_1983+1
    else:
        xmm_bin_1983 = xmm_bin_1983

print(xmm_bin_1983)

xmm_bin_1982=0

for x in xmm:
    if '1982' in x:
        xmm_bin_1982 = xmm_bin_1982+1
    else:
        xmm_bin_1982 = xmm_bin_1982

print(xmm_bin_1982)

xmm_bin_1981=0

for x in xmm:
    if '1981' in x:
        xmm_bin_1981 = xmm_bin_1981+1
    else:
        xmm_bin_1981 = xmm_bin_1981

print(xmm_bin_1981)

xmm_bin_1980=0

for x in xmm:
    if '1980' in x:
        xmm_bin_1980 = xmm_bin_1980+1
    else:
        xmm_bin_1980 = xmm_bin_1980

print(xmm_bin_1980)

xmm_bin_1979=0

for x in xmm:
    if '1979' in x:
        xmm_bin_1979 = xmm_bin_1979+1
    else:
        xmm_bin_1979 = xmm_bin_1979

print(xmm_bin_1979)

xmm_bin_1978=0

for x in xmm:
    if '1978' in x:
        xmm_bin_1978 = xmm_bin_1978+1
    else:
        xmm_bin_1978 = xmm_bin_1978

print(xmm_bin_1978)

xmm_bin_1972=0

for x in xmm:
    if '1972' in x:
        xmm_bin_1972 = xmm_bin_1972+1
    else:
        xmm_bin_1972 = xmm_bin_1972

print(xmm_bin_1972)


galex_bin_2018=0

for x in galex:
    if '18' in x:
        galex_bin_2018 = galex_bin_2018+1
    else:
        galex_bin_2018 = galex_bin_2018

print(galex_bin_2018)

galex_bin_2017=0

for x in galex:
    if '2017' in x:
        galex_bin_2017 = galex_bin_2017+1
    else:
        galex_bin_2017 = galex_bin_2017

print(galex_bin_2017)

galex_bin_2016=0

for x in galex:
    if '16' in x:
        galex_bin_2016 = galex_bin_2016+1
    else:
        galex_bin_2016 = galex_bin_2016

print(galex_bin_2016)

galex_bin_2015=0

for x in galex:
    if '15' in x:
        galex_bin_2015 = galex_bin_2015+1
    else:
        galex_bin_2015 = galex_bin_2015

print(galex_bin_2015)

galex_bin_2014=0

for x in galex:
    if '14' in x:
        galex_bin_2014 = galex_bin_2014+1
    else:
        galex_bin_2014 = galex_bin_2014

print(galex_bin_2014)

galex_bin_2013=0

for x in galex:
    if '13' in x:
        galex_bin_2013 = galex_bin_2013+1
    else:
        galex_bin_2013 = galex_bin_2013

print(galex_bin_2013)

galex_bin_2012=0

for x in galex:
    if '12' in x:
        galex_bin_2012 = galex_bin_2012+1
    else:
        galex_bin_2012 = galex_bin_2012

print(galex_bin_2012)

galex_bin_2011=0

for x in galex:
    if '11' in x:
        galex_bin_2011 = galex_bin_2011+1
    else:
        galex_bin_2011 = galex_bin_2011

print(galex_bin_2011)

galex_bin_2010=0

for x in galex:
    if '2010' in x:
        galex_bin_2010 = galex_bin_2010+1
    else:
        galex_bin_2010 = galex_bin_2010

print(galex_bin_2010)

galex_bin_2009=0

for x in galex:
    if '09' in x:
        galex_bin_2009 = galex_bin_2009+1
    else:
        galex_bin_2009 = galex_bin_2009

print(galex_bin_2009)

galex_bin_2008=0

for x in galex:
    if '08' in x:
        galex_bin_2008 = galex_bin_2008+1
    else:
        galex_bin_2008 = galex_bin_2008

print(galex_bin_2008)

galex_bin_2007=0

for x in galex:
    if '07' in x:
        galex_bin_2007 = galex_bin_2007+1
    else:
        galex_bin_2007 = galex_bin_2007

print(galex_bin_2007)

galex_bin_2006=0

for x in galex:
    if '06' in x:
        galex_bin_2006 = galex_bin_2006+1
    else:
        galex_bin_2006 = galex_bin_2006

print(galex_bin_2006)

galex_bin_2005=0

for x in galex:
    if '05' in x:
        galex_bin_2005 = galex_bin_2005+1
    else:
        galex_bin_2005 = galex_bin_2005

print(galex_bin_2005)

galex_bin_2004=0

for x in galex:
    if '04' in x:
        galex_bin_2004 = galex_bin_2004+1
    else:
        galex_bin_2004 = galex_bin_2004

print(galex_bin_2004)

galex_bin_2003=0

for x in galex:
    if '03' in x:
        galex_bin_2003 = galex_bin_2003+1
    else:
        galex_bin_2003 = galex_bin_2003

print(galex_bin_2003)

galex_bin_2002=0

for x in galex:
    if '02' in x:
        galex_bin_2002 = galex_bin_2002+1
    else:
        galex_bin_2002 = galex_bin_2002

print(galex_bin_2002)

galex_bin_2001=0

for x in galex:
    if '2001' in x:
        galex_bin_2001 = galex_bin_2001+1
    else:
        galex_bin_2001 = galex_bin_2001

print(galex_bin_2001)

galex_bin_2000=0

for x in galex:
    if '2000' in x:
        galex_bin_2000 = galex_bin_2000+1
    else:
        galex_bin_2000 = galex_bin_2000

print(galex_bin_2000)

galex_bin_1999=0

for x in galex:
    if '1999' in x:
        galex_bin_1999 = galex_bin_1999+1
    else:
        galex_bin_1999 = galex_bin_1999

print(galex_bin_1999)

galex_bin_1998=0

for x in galex:
    if '1998' in x:
        galex_bin_1998 = galex_bin_1998+1
    else:
        galex_bin_1998 = galex_bin_1998

print(galex_bin_1998)

galex_bin_1997=0

for x in galex:
    if '1997' in x:
        galex_bin_1997 = galex_bin_1997+1
    else:
        galex_bin_1997 = galex_bin_1997

print(galex_bin_1997)

galex_bin_1996=0

for x in galex:
    if '1996' in x:
        galex_bin_1996 = galex_bin_1996+1
    else:
        galex_bin_1996 = galex_bin_1996

print(galex_bin_1996)

galex_bin_1995=0

for x in galex:
    if '1995' in x:
        galex_bin_1995 = galex_bin_1995+1
    else:
        galex_bin_1995 = galex_bin_1995

print(galex_bin_1995)

galex_bin_1994=0

for x in galex:
    if '1994' in x:
        galex_bin_1994 = galex_bin_1994+1
    else:
        galex_bin_1994 = galex_bin_1994

print(galex_bin_1994)

galex_bin_1993=0

for x in galex:
    if '1993' in x:
        galex_bin_1993 = galex_bin_1993+1
    else:
        galex_bin_1993 = galex_bin_1993

print(galex_bin_1993)

galex_bin_1992=0

for x in galex:
    if '1992' in x:
        galex_bin_1992 = galex_bin_1992+1
    else:
        galex_bin_1992 = galex_bin_1992

print(galex_bin_1992)

galex_bin_1991=0

for x in galex:
    if '1991' in x:
        galex_bin_1991 = galex_bin_1991+1
    else:
        galex_bin_1991 = galex_bin_1991

print(galex_bin_1991)

galex_bin_1990=0

for x in galex:
    if '1990' in x:
        galex_bin_1990 = galex_bin_1990+1
    else:
        galex_bin_1990 = galex_bin_1990

print(galex_bin_1990)

galex_bin_1989=0

for x in galex:
    if '1989' in x:
        galex_bin_1989 = galex_bin_1989+1
    else:
        galex_bin_1989 = galex_bin_1989

print(galex_bin_1989)

galex_bin_1988=0

for x in galex:
    if '1988' in x:
        galex_bin_1988 = galex_bin_1988+1
    else:
        galex_bin_1988 = galex_bin_1988

print(galex_bin_1988)

galex_bin_1987=0

for x in galex:
    if '1987' in x:
        galex_bin_1987 = galex_bin_1987+1
    else:
        galex_bin_1987 = galex_bin_1987

print(galex_bin_1987)

galex_bin_1986=0

for x in galex:
    if '1986' in x:
        galex_bin_1986 = galex_bin_1986+1
    else:
        galex_bin_1986 = galex_bin_1986

print(galex_bin_1986)

galex_bin_1985=0

for x in galex:
    if '1985' in x:
        galex_bin_1985 = galex_bin_1985+1
    else:
        galex_bin_1985 = galex_bin_1985

print(galex_bin_1985)

galex_bin_1984=0

for x in galex:
    if '1984' in x:
        galex_bin_1984 = galex_bin_1984+1
    else:
        galex_bin_1984 = galex_bin_1984

print(galex_bin_1984)

galex_bin_1983=0

for x in galex:
    if '1983' in x:
        galex_bin_1983 = galex_bin_1983+1
    else:
        galex_bin_1983 = galex_bin_1983

print(galex_bin_1983)

galex_bin_1982=0

for x in galex:
    if '1982' in x:
        galex_bin_1982 = galex_bin_1982+1
    else:
        galex_bin_1982 = galex_bin_1982

print(galex_bin_1982)

galex_bin_1981=0

for x in galex:
    if '1981' in x:
        galex_bin_1981 = galex_bin_1981+1
    else:
        galex_bin_1981 = galex_bin_1981

print(galex_bin_1981)

galex_bin_1980=0

for x in galex:
    if '1980' in x:
        galex_bin_1980 = galex_bin_1980+1
    else:
        galex_bin_1980 = galex_bin_1980

print(galex_bin_1980)

galex_bin_1979=0

for x in galex:
    if '1979' in x:
        galex_bin_1979 = galex_bin_1979+1
    else:
        galex_bin_1979 = galex_bin_1979

print(galex_bin_1979)

galex_bin_1978=0

for x in galex:
    if '1978' in x:
        galex_bin_1978 = galex_bin_1978+1
    else:
        galex_bin_1978 = galex_bin_1978

print(galex_bin_1978)

galex_bin_1972=0

for x in galex:
    if '1972' in x:
        galex_bin_1972 = galex_bin_1972+1
    else:
        galex_bin_1972 = galex_bin_1972

print(galex_bin_1972)

'''
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
'''
hst_graph=[]
oao_graph=[]
iue_graph=[]
xmm_graph=[]
galex_graph=[]



for x in range(hst_bin_2018):
    hst_graph.append(2018)

for x in range(hst_bin_2017):
    hst_graph.append(2017)
    
for x in range(hst_bin_2016):
    hst_graph.append(2016)

for x in range(hst_bin_2015):
    hst_graph.append(2015)
    
for x in range(hst_bin_2014):
    hst_graph.append(2014)
    
for x in range(hst_bin_2013):
    hst_graph.append(2013)
    
for x in range(hst_bin_2012):
    hst_graph.append(2012)
    
for x in range(hst_bin_2011):
    hst_graph.append(2011)
    
for x in range(hst_bin_2010):
    hst_graph.append(2010)
    
for x in range(hst_bin_2009):
    hst_graph.append(2009)
    
for x in range(hst_bin_2008):
    hst_graph.append(2008)

for x in range(hst_bin_2007):
    hst_graph.append(2007)
    
for x in range(hst_bin_2006):
    hst_graph.append(2006)

for x in range(hst_bin_2005):
    hst_graph.append(2005)

for x in range(hst_bin_2004):
    hst_graph.append(2004)

for x in range(hst_bin_2003):
    hst_graph.append(2003)

for x in range(hst_bin_2002):
    hst_graph.append(2002)

for x in range(hst_bin_2001):
    hst_graph.append(2001)

for x in range(hst_bin_2000):
    hst_graph.append(2000)

for x in range(hst_bin_1999):
    hst_graph.append(1999)

for x in range(hst_bin_1998):
    hst_graph.append(1998)

for x in range(hst_bin_1997):
    hst_graph.append(1997)

for x in range(hst_bin_1996):
    hst_graph.append(1996)

for x in range(hst_bin_1995):
    hst_graph.append(1995)

for x in range(hst_bin_1994):
    hst_graph.append(1994)

for x in range(hst_bin_1993):
    hst_graph.append(1993)

for x in range(hst_bin_1992):
    hst_graph.append(1992)

for x in range(hst_bin_1991):
    hst_graph.append(1991)

for x in range(hst_bin_1990):
    hst_graph.append(1990)

for x in range(hst_bin_1989):
    hst_graph.append(1989)

for x in range(hst_bin_1988):
    hst_graph.append(1988)

for x in range(hst_bin_1987):
    hst_graph.append(1987)

for x in range(hst_bin_1986):
    hst_graph.append(1986)

for x in range(hst_bin_1985):
    hst_graph.append(1985)

for x in range(hst_bin_1984):
    hst_graph.append(1984)

for x in range(hst_bin_1983):
    hst_graph.append(1983)

for x in range(hst_bin_1982):
    hst_graph.append(1982)

for x in range(hst_bin_1981):
    hst_graph.append(1981)

for x in range(hst_bin_1980):
    hst_graph.append(1980)

for x in range(hst_bin_1979):
    hst_graph.append(1979)

for x in range(hst_bin_1978):
    hst_graph.append(1978)

for x in range(hst_bin_1972):
    hst_graph.append(1972)



for x in range(oao_bin_2018):
    oao_graph.append(2018)

for x in range(oao_bin_2017):
    oao_graph.append(2017)
    
for x in range(oao_bin_2016):
    oao_graph.append(2016)

for x in range(oao_bin_2015):
    oao_graph.append(2015)
    
for x in range(oao_bin_2014):
    oao_graph.append(2014)
    
for x in range(oao_bin_2013):
    oao_graph.append(2013)
    
for x in range(oao_bin_2012):
    oao_graph.append(2012)
    
for x in range(oao_bin_2011):
    oao_graph.append(2011)
    
for x in range(oao_bin_2010):
    oao_graph.append(2010)
    
for x in range(oao_bin_2009):
    oao_graph.append(2009)
    
for x in range(oao_bin_2008):
    oao_graph.append(2008)

for x in range(oao_bin_2007):
    oao_graph.append(2007)
    
for x in range(oao_bin_2006):
    oao_graph.append(2006)

for x in range(oao_bin_2005):
    oao_graph.append(2005)

for x in range(oao_bin_2004):
    oao_graph.append(2004)

for x in range(oao_bin_2003):
    oao_graph.append(2003)

for x in range(oao_bin_2002):
    oao_graph.append(2002)

for x in range(oao_bin_2001):
    oao_graph.append(2001)

for x in range(oao_bin_2000):
    oao_graph.append(2000)

for x in range(oao_bin_1999):
    oao_graph.append(1999)

for x in range(oao_bin_1998):
    oao_graph.append(1998)

for x in range(oao_bin_1997):
    oao_graph.append(1997)

for x in range(oao_bin_1996):
    oao_graph.append(1996)

for x in range(oao_bin_1995):
    oao_graph.append(1995)

for x in range(oao_bin_1994):
    oao_graph.append(1994)

for x in range(oao_bin_1993):
    oao_graph.append(1993)

for x in range(oao_bin_1992):
    oao_graph.append(1992)

for x in range(oao_bin_1991):
    oao_graph.append(1991)

for x in range(oao_bin_1990):
    oao_graph.append(1990)

for x in range(oao_bin_1989):
    oao_graph.append(1989)

for x in range(oao_bin_1988):
    oao_graph.append(1988)

for x in range(oao_bin_1987):
    oao_graph.append(1987)

for x in range(oao_bin_1986):
    oao_graph.append(1986)

for x in range(oao_bin_1985):
    oao_graph.append(1985)

for x in range(oao_bin_1984):
    oao_graph.append(1984)

for x in range(oao_bin_1983):
    oao_graph.append(1983)

for x in range(oao_bin_1982):
    oao_graph.append(1982)

for x in range(oao_bin_1981):
    oao_graph.append(1981)

for x in range(oao_bin_1980):
    oao_graph.append(1980)

for x in range(oao_bin_1979):
    oao_graph.append(1979)

for x in range(oao_bin_1978):
    oao_graph.append(1978)

for x in range(oao_bin_1972):
    oao_graph.append(1972)



for x in range(iue_bin_2018):
    iue_graph.append(2018)

for x in range(iue_bin_2017):
    iue_graph.append(2017)
    
for x in range(iue_bin_2016):
    iue_graph.append(2016)

for x in range(iue_bin_2015):
    iue_graph.append(2015)
    
for x in range(iue_bin_2014):
    iue_graph.append(2014)
    
for x in range(iue_bin_2013):
    iue_graph.append(2013)
    
for x in range(iue_bin_2012):
    iue_graph.append(2012)
    
for x in range(iue_bin_2011):
    iue_graph.append(2011)
    
for x in range(iue_bin_2010):
    iue_graph.append(2010)
    
for x in range(iue_bin_2009):
    iue_graph.append(2009)
    
for x in range(iue_bin_2008):
    iue_graph.append(2008)

for x in range(iue_bin_2007):
    iue_graph.append(2007)
    
for x in range(iue_bin_2006):
    iue_graph.append(2006)

for x in range(iue_bin_2005):
    iue_graph.append(2005)

for x in range(iue_bin_2004):
    iue_graph.append(2004)

for x in range(iue_bin_2003):
    iue_graph.append(2003)

for x in range(iue_bin_2002):
    iue_graph.append(2002)

for x in range(iue_bin_2001):
    iue_graph.append(2001)

for x in range(iue_bin_2000):
    iue_graph.append(2000)

for x in range(iue_bin_1999):
    iue_graph.append(1999)

for x in range(iue_bin_1998):
    iue_graph.append(1998)

for x in range(iue_bin_1997):
    iue_graph.append(1997)

for x in range(iue_bin_1996):
    iue_graph.append(1996)

for x in range(iue_bin_1995):
    iue_graph.append(1995)

for x in range(iue_bin_1994):
    iue_graph.append(1994)

for x in range(iue_bin_1993):
    iue_graph.append(1993)

for x in range(iue_bin_1992):
    iue_graph.append(1992)

for x in range(iue_bin_1991):
    iue_graph.append(1991)

for x in range(iue_bin_1990):
    iue_graph.append(1990)

for x in range(iue_bin_1989):
    iue_graph.append(1989)

for x in range(iue_bin_1988):
    iue_graph.append(1988)

for x in range(iue_bin_1987):
    iue_graph.append(1987)

for x in range(iue_bin_1986):
    iue_graph.append(1986)

for x in range(iue_bin_1985):
    iue_graph.append(1985)

for x in range(iue_bin_1984):
    iue_graph.append(1984)

for x in range(iue_bin_1983):
    iue_graph.append(1983)

for x in range(iue_bin_1982):
    iue_graph.append(1982)

for x in range(iue_bin_1981):
    iue_graph.append(1981)

for x in range(iue_bin_1980):
    iue_graph.append(1980)

for x in range(iue_bin_1979):
    iue_graph.append(1979)

for x in range(iue_bin_1978):
    iue_graph.append(1978)

for x in range(iue_bin_1972):
    
    iue_graph.append(1972)


for x in range(xmm_bin_2018):
    xmm_graph.append(2018)

for x in range(xmm_bin_2017):
    xmm_graph.append(2017)
    
for x in range(xmm_bin_2016):
    xmm_graph.append(2016)

for x in range(xmm_bin_2015):
    xmm_graph.append(2015)
    
for x in range(xmm_bin_2014):
    xmm_graph.append(2014)
    
for x in range(xmm_bin_2013):
    xmm_graph.append(2013)
    
for x in range(xmm_bin_2012):
    xmm_graph.append(2012)
    
for x in range(xmm_bin_2011):
    xmm_graph.append(2011)
    
for x in range(xmm_bin_2010):
    xmm_graph.append(2010)
    
for x in range(xmm_bin_2009):
    xmm_graph.append(2009)
    
for x in range(xmm_bin_2008):
    xmm_graph.append(2008)

for x in range(xmm_bin_2007):
    xmm_graph.append(2007)
    
for x in range(xmm_bin_2006):
    xmm_graph.append(2006)

for x in range(xmm_bin_2005):
    xmm_graph.append(2005)

for x in range(xmm_bin_2004):
    xmm_graph.append(2004)

for x in range(xmm_bin_2003):
    xmm_graph.append(2003)

for x in range(xmm_bin_2002):
    xmm_graph.append(2002)

for x in range(xmm_bin_2001):
    xmm_graph.append(2001)

for x in range(xmm_bin_2000):
    xmm_graph.append(2000)

for x in range(xmm_bin_1999):
    xmm_graph.append(1999)

for x in range(xmm_bin_1998):
    xmm_graph.append(1998)

for x in range(xmm_bin_1997):
    xmm_graph.append(1997)

for x in range(xmm_bin_1996):
    xmm_graph.append(1996)

for x in range(xmm_bin_1995):
    xmm_graph.append(1995)

for x in range(xmm_bin_1994):
    xmm_graph.append(1994)

for x in range(xmm_bin_1993):
    xmm_graph.append(1993)

for x in range(xmm_bin_1992):
    xmm_graph.append(1992)

for x in range(xmm_bin_1991):
    xmm_graph.append(1991)

for x in range(xmm_bin_1990):
    xmm_graph.append(1990)

for x in range(xmm_bin_1989):
    xmm_graph.append(1989)

for x in range(xmm_bin_1988):
    xmm_graph.append(1988)

for x in range(xmm_bin_1987):
    xmm_graph.append(1987)

for x in range(xmm_bin_1986):
    xmm_graph.append(1986)

for x in range(xmm_bin_1985):
    xmm_graph.append(1985)

for x in range(xmm_bin_1984):
    xmm_graph.append(1984)

for x in range(xmm_bin_1983):
    xmm_graph.append(1983)

for x in range(xmm_bin_1982):
    xmm_graph.append(1982)

for x in range(xmm_bin_1981):
    xmm_graph.append(1981)

for x in range(xmm_bin_1980):
    xmm_graph.append(1980)

for x in range(xmm_bin_1979):
    xmm_graph.append(1979)

for x in range(xmm_bin_1978):
    xmm_graph.append(1978)

for x in range(xmm_bin_1972):
    xmm_graph.append(1972)


for x in range(galex_bin_2018):
    galex_graph.append(2018)

for x in range(galex_bin_2017):
    galex_graph.append(2017)
    
for x in range(galex_bin_2016):
    galex_graph.append(2016)

for x in range(galex_bin_2015):
    galex_graph.append(2015)
    
for x in range(galex_bin_2014):
    galex_graph.append(2014)
    
for x in range(galex_bin_2013):
    galex_graph.append(2013)
    
for x in range(galex_bin_2012):
    galex_graph.append(2012)
    
for x in range(galex_bin_2011):
    galex_graph.append(2011)
    
for x in range(galex_bin_2010):
    galex_graph.append(2010)
    
for x in range(galex_bin_2009):
    galex_graph.append(2009)
    
for x in range(galex_bin_2008):
    galex_graph.append(2008)

for x in range(galex_bin_2007):
    galex_graph.append(2007)
    
for x in range(galex_bin_2006):
    galex_graph.append(2006)

for x in range(galex_bin_2005):
    galex_graph.append(2005)

for x in range(galex_bin_2004):
    galex_graph.append(2004)

for x in range(galex_bin_2003):
    galex_graph.append(2003)

for x in range(galex_bin_2002):
    galex_graph.append(2002)

for x in range(galex_bin_2001):
    galex_graph.append(2001)

for x in range(galex_bin_2000):
    galex_graph.append(2000)

for x in range(galex_bin_1999):
    galex_graph.append(1999)

for x in range(galex_bin_1998):
    galex_graph.append(1998)

for x in range(galex_bin_1997):
    galex_graph.append(1997)

for x in range(galex_bin_1996):
    galex_graph.append(1996)

for x in range(galex_bin_1995):
    galex_graph.append(1995)

for x in range(galex_bin_1994):
    galex_graph.append(1994)

for x in range(galex_bin_1993):
    galex_graph.append(1993)

for x in range(galex_bin_1992):
    galex_graph.append(1992)

for x in range(galex_bin_1991):
    galex_graph.append(1991)

for x in range(galex_bin_1990):
    galex_graph.append(1990)

for x in range(galex_bin_1989):
    galex_graph.append(1989)

for x in range(galex_bin_1988):
    galex_graph.append(1988)

for x in range(galex_bin_1987):
    galex_graph.append(1987)

for x in range(galex_bin_1986):
    galex_graph.append(1986)

for x in range(galex_bin_1985):
    galex_graph.append(1985)

for x in range(galex_bin_1984):
    galex_graph.append(1984)

for x in range(galex_bin_1983):
    galex_graph.append(1983)

for x in range(galex_bin_1982):
    galex_graph.append(1982)

for x in range(galex_bin_1981):
    galex_graph.append(1981)

for x in range(galex_bin_1980):
    galex_graph.append(1980)

for x in range(galex_bin_1979):
    galex_graph.append(1979)

for x in range(galex_bin_1978):
    galex_graph.append(1978)

for x in range(galex_bin_1972):
    galex_graph.append(1972)



b = np.arange(1971,2021, 1)

plt.rcParams.update({'font.size': 16})
font={'fontname': 'Arial', 'weight':'bold', 'size':'22'}
axis_font={'fontname': 'Arial', 'size':'18'}
#plt.hist(a,b, histtype='bar', rwidth=0.8, label="SWIFT")
plt.hist(hst_graph,b, histtype='bar', rwidth=0.8, label="HST")
plt.hist(galex_graph,b, histtype='bar', rwidth=0.8, label="GALEX")
plt.hist(oao_graph,b, histtype='bar', rwidth=0.8, label="OAO-2")
plt.hist(iue_graph,b, histtype='bar', rwidth=0.8, label="IUE")
plt.hist(xmm_graph,b, histtype='bar', rwidth=0.8, label="XMM-OM")
#plt.title("Supernovae Captured by Satellites Each Year") 
plt.legend(loc='upper left')
plt.xlabel("Year", **font)
plt.xlim(left=1971)
plt.xlim(right=2021)
plt.xticks(np.arange(1971,2021,3), **axis_font)
plt.yticks(**axis_font)
plt.ylabel("Number of Supernovae Observed in the Ultraviolet", **font)
plt.show() 