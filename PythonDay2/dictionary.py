scores = {'james': 1828, 'thomas': 3628, 'danny': 9310}

print(scores)
print(scores['thomas'])

# เพิ่มสมาชิกใหม่เข้าไปใน Dictionary
scores['Bobby'] = 8200

print(scores)
print(scores['Bobby'])

# อัพเดทค่า
scores['thomas'] = 100
print(scores)

print("--------------------------")

countries = {
    'de': 'Germany', 
    'ua': 'Ukraine',
    'th': 'Thailand', 
    'nl': 'Netherlands'
}

# การ loop อ่านค่าสมาชิกใน dictionary
for k in countries:
    print(k)

print("--------------------------")

for v in countries.values():
    print(v)

print("--------------------------")

for k, v in countries.items():
    print(k,v)