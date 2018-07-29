#!/usr/bin/python
# -*- coding: utf-8 -*-
print("\
30以下の自然数の集合uを全体集合とする。uの要素のうち、3の倍数の集合をa, 4の倍数の集合をbとする。")#とき、次の値を求めなさい。
u=range(1,31)
i=0
a = []
for x in u:
  if (x%3 == 0):
    if (i==0):
      a=[x]
      i=i+1
    else:
      a=a+[x]
      i=i+1
b = []
i=0
for x in u:
  if (x%4 == 0):
    b.append(x)
    i=i+1
i=0
print("u: "+str(list(u)))
print("a: "+str(list(a)))
print("b: "+str(list(b)))

bdash=set(u).difference(set(b))
print("b―: "+str(bdash))

acupB=set(a).intersection(set(bdash))
print("a∩b―: "+str(acupB))
print("n(a∩b―) : "+str(len(list(acupB))))
