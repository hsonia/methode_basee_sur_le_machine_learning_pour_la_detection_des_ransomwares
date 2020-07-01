from sklearn import svm
from sklearn import datasets
import pandas as pd
import numpy as np
import re

data = pd.read_csv('/home/sonia/Bureau/RansomeWareDataset.csv')
df = pd.DataFrame(data)

nf = df.groupby("Family").size().count()
h = list(df)
d = df.to_numpy()

c = len(df.columns)
r = len(df.index)

s = []
b = []
for j in range(3, c):
    l = []
    n = 0
    for i in range(r):
        if(i == 0):
            if(d[0][j] != 0):
                if(d[0][0]==d[1][0]):
                    l.append(h[j])
                    n = 1
                else:
                    b.append(h[j])
            else:
                if(d[0][0]!=d[1][0]):
                    s.append(h[j])
        else:
            if(d[i][0]==d[i-1][0]):
                n += 1
                if(d[i][j]!=0):
                    l.append(h[j])
            else:
                if(len(l) <=((n-1)/2)):
                    s.append(h[j])
                    if(len(l)>0):
                        b.append(h[j])
                l.clear()
                n = 1
                if(d[i][0]==d[i+1][0]):
                    if(d[i][j]!=0):
                        l.append(h[j])
                else:
                    s.append(h[j])
                    if(d[i][j]!=0):
                        b.append(h[j])


def net_mot(s):
    i = 0
    while i < len(s):
        if (re.findall("key", str(s[i]).lower()) or (re.findall("crypt", str(s[i]).lower())) or (
                re.findall("reg", str(s[i]).lower())) or (re.findall("scmanager", str(s[i]).lower())) or (
                re.findall("privilege", str(s[i]).lower())) or (re.findall("file", str(s[i]).lower()))):
            del s[i]
        else:
            i += 1
    return s

s = net_mot(s)
b = net_mot(b)

i = 0
while i < len(b):
    if b[i] == b[i - 1]:
        del b[i]
    else:
        i += 1

i = 0
while i < (len(s)+1):
    if(i == 0):
        n = 1
        i += 1
    elif((i!=len(s)) and (s[i] == s[i-1])):
        n += 1
        i += 1
    elif(n< (2*nf/3)):
        for j in range(i-n, n):
            del s[i-n]
        i -= n
        n = 1
    elif(n == nf):
        l.append(s[i-n])
        for j in range(i - n, n):
            del s[i - n]
        i -= n
        n = 1
    elif(n == (nf-1)):
        f = 'f'
        for e in b:
            if (s[i-n] == e):
                f = 't'
                break
        if(f == 't'):
            l.append(s[i-n])
            for j in range(i - n, n):
                del s[i - n]
            i -= n
            n = 1
        else:
            for j in range(i - n, n):
                del s[i - n]
            i -= n
            n = 1
    else:
        l.append(s[i-n])
        for j in range(i - n, n):
            del s[i - n]
        i -= n
        n = 1
s += l
#print(len(s),s)
df.drop(labels = s, axis = 1, inplace = True)
#print(df)
