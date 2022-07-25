# pcost.py
#
# Exercise 1.27
import csv
from fileinput import filename
import sys
def portfolio_cost(filename):
    with open(filename,'rt') as file:
        rows=csv.reader(file)
        headers=next(file)
        total_cost=0.0
        for row in rows:
            try:
                nshares=int(row[1])
                price=float(row[2])
                total_cost+=nshares*price
            except ValueError:
                print('Bad row:',row)
    return(total_cost)

if len(sys.argv)==2:
    filename=sys.argv[1]
else:
    filename=input('Enter a filename:')
cost=portfolio_cost(filename)
print('Total cost:',cost)