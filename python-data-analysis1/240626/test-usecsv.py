import usecsv
import os

print(os.getcwd())
os.chdir(r'D:\human-edu1\python-data-analysis1\240626')

a = [['국어','영어','수학'],[99,88,77]]
usecsv.writecsv('test.csv', a)

total = usecsv.opencsv(r'D:\human-edu1\python-data-analysis1\240626\popSeoul2023.csv')
print(usecsv.switch(total))