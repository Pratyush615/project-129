import pandas as pd
import csv

file1 = "bright_stars.csv"
file2 = "unit_converted_stars.csv"

d1 = []
d2 = []

with open(file1,'r',encoding="utf-8") as f:
    csv_reader = csv.reader(f)
    for i in csv_reader:
        d1.append(i)
with open(file2,'r',encoding="utf-8") as f:
    csv_reader = csv.reader(f)
    for i in csv_reader:
        d2.append(i)

h1 = d1[0]
h2 = d2[0]

p1 = d1[1:]
p2 = d1[1:]

h=h1+h2

p = []

for i in p1:
    p.append(i)
for j in p2:
    p.append(j)
with open("total_stars.csv","w",encoding="utf-8") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(h)
    csv_writer.writerows(p)