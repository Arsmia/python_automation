import csv

'''
with open('industry.csv') as csvfile:
    csvfile = csv.reader(csvfile)
    for row in csvfile:
        print(row)
'''

with open("mycsv", 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")
    csvwriter.writerow = csv.writer(['a', 'b', 'c'])
    csvwriter.writerow = csv.writer(['A', 'B', 'C'])
