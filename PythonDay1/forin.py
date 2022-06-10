# loop through string
site = 'marcuscode'
for n in site:
    print(n)

# loop through list
names = ['Mateo', 'John', 'Eric', 'Mark', 'Robert']
for n in names:
    print(n)

numbers = [10, 20, 30, 40, 50, 60, 70, 80]
for n in numbers:
    print(n)

# คำสั่ง for loop กับฟังก์ชัน range()
a = list(range(10))
b = list(range(1, 11))
c = list(range(0, 30, 5))
d = list(range(0, -10, -1))

print(a)
print(b)
print(c)
print(d)

# คำสั่ง continue
for i in range(1, 11):   
    if i % 2 == 1:
        continue  # skip ข้ามเลขคี่ไป
    print(i, end = ', ')
