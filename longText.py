import re


long_text = """
Variopartner SICAV
529900LPCSV88817QH61
1. TARENO GLOBAL WATER SOLUTIONS FUND
LU2001709034
LU2057889995
LU2001709547
2. TARENO FIXED INCOME FUND
LU1299722972
3. TARENO GLOBAL EQUITY FUND
LU1299721909
LU1299722113
LU1299722030
4. MIV GLOBAL MEDTECH FUND
LU0329630999
LU0329630130
"""


key1 = ['name','lei','sub_fund']
key2 = ['title', 'isin']
list1 = re.split('[0-9]. ', long_text)
print(list1)
list2 = list(filter(None, list1[0].split('\n')))
print(list2)

dict1 = {}
list0 = []
for i in range (1,len(list1)):
    a,b = list1[i].split('\n',1)
    b = list(filter(None, b.split('\n')))
    dict1[key2[0]] = a
    dict1[key2[1]] = b
    list0.append(dict1)
print(list0)

result = dict(zip(key1, list2 + list0))
print(result)
