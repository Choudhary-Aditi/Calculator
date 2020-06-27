def Pourcentage(value,percentage):
    return value*percentage/100

def usaformula(data,info):
    type_of_person = int(data.get('type_of_person'))
    income = int(data.get('Income'))
    Number_children = int(data.get('Number_children'))
    profit = 1200
    if type_of_person == 0:
        min_value = info['min_single']
        max_value = info['max_single']
    if type_of_person == 1:
        min_value = info['min_married']
        max_value = info['max_married']
        profit = 2400
    else:
        min_value = info['min_Head_of_houshold']
        max_value = info['max_Head_of_houshold']
    if income < min_value:
        return profit + (Number_children * 500)
    if income < max_value:
        diffrence = ((income-min_value)/100)*5
        return profit + (Number_children * 500) - diffrence
    if income > max_value:
        diffrence = ((income - min_value) / 100) * 5
        children_profit = (Number_children * 500)
        if diffrence > children_profit:
            return 0
        return children_profit - diffrence


def franceformula(data,info):
    income = int(data.get('Income'))
    if income <= info['min_wage']:
        return income
    elif income < info['max_value']:
        return Pourcentage(income, 70)
    else:
        return 0
def ukformula(data,info):
    income = int(data.get('Income'))
    if income < info['min_value']:
        return Pourcentage(income, 80)
    elif income >= info['min_value']:
        return 2500
def germanyformula(data,info):
    income = int(data.get('Income'))
    N_children = int(data.get('Number_children'))
    if N_children > 0:
        return Pourcentage(income, 67)
    else:
        return Pourcentage(income, 60)


def canadaformula(data,info):
    N_children = int(data.get('Number_children'))
    return 2000 + (N_children * 300)


def australiaformula(data,info):
    income = int(data.get('Income'))
    if income <= 1500:
        return 1500
    else:
        return 0
