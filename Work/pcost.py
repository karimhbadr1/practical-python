# pcost.py
#
# Exercise 1.27
def portfolio_cost(filename):
    with open(filename,'rt') as file:
        header=next(file)
        total_cost=0.0
        for line in file:
            row=line.split(',')
            total_cost=total_cost+(float(row[1])*float(row[2]))
    return(total_cost)
cost=portfolio_cost('Data/portfolio.csv')
print('Total cost:',cost)