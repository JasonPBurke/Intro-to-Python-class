#calculate monthly paycheck for salespeople
#collect info from user
name = str(input('What is your name: '))
longevity = float(input('How many months have you been with the company: '))
salary = float(2000)
sales = float(input('What were your total sales: '))

#decide if user gets commission/bonus and calculate it if they do
if longevity > 3 and (sales >= 10000 and sales <=100000):
    com_rate = sales * .02
    bonus = float(0)
                    
elif longevity > 3 and (sales >= 100001 and sales <= 500000):
    com_rate = sales * .15
    bonus = float(1000)

elif longevity > 3 and (sales >= 500001 and sales <= 1000000):
    com_rate = sales * .28
    bonus = float(5000)
elif longevity > 3 and sales >1000000:
    com_rate = sales * .35
    bonus =float(100000)
else:
    com_rate = 0.0
    bonus = 0.0


# Reduce salary for >=3 vacation days taken in a month
vacation_days = int(input('How many vacation days have you take this month: '))
if vacation_days >= 3:
    v_deduction = 200.0
else:
    v_deduction = 0.0

# Decide if salesperson gets additional bonus based on tenure and sales
if longevity >= 60 and sales > 100000:
    additional_bonus = 1000.0
else:
    additional_bonus = 0.0

# Print out pay info to user
print('Name:',name, '\n')
print('Longevity:', longevity, 'Months', '\n')
print('Base Salary: $', format(salary, ',.2f'), '\n', sep='')
print('Commission earned: $', format(com_rate,',.2f'), '\n', sep='')
print('Bonus earned: $', format(bonus, ',.2f'), '\n', sep='')
print('Additional bonus: $', format(additional_bonus, ',.2f'), '\n', sep='')
print('Deductions: -$', format(v_deduction, ',.2f'), '\n',sep='')
print('Total pay: $', format(salary + com_rate + bonus + additional_bonus -
                             v_deduction, ',.2f'), '\n', sep='')
                             
