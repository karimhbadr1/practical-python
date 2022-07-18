# mortgage.py
#
# Exercise 1.7
principal = 500000
rate = 0.05
payment = 2684.11
total_paid = 0.0
month=0
extra_payment=1000
extra_payment_start_month=61
extra_payment_end_month=108 

while principal>0 and (principal-payment>0):
    month+=1
    principal=principal*(1+rate/12)-payment
    total_paid=total_paid+payment
    if month>=extra_payment_start_month and month<=extra_payment_end_month:
        total_paid=total_paid+extra_payment
        principal=principal-extra_payment
    print('Month',month,'Total paid',round(total_paid,2),'Remaining',round(principal,2))

if (principal-payment<=0):
    month+=1
    payment=principal
    total_paid=total_paid+payment
    principal=principal-payment
    print('Month',month,'Total paid',round(total_paid,2),'Remaining',round(principal,2))


print('Total paid', round(total_paid, 2))
print('Months', month)