# การสร้างตัวแปรแบบ List
numbers = [-1, 2, 5, 8, 10, 13]
names = ['Mateo', 'Danny', 'James', 'Thomas', 'Luke']
mixed = [-2, 5, 84.5, "Mountain", "Python", True]

# การแสดงผล list
print(numbers)
print(numbers[0])
print(numbers[3])
# print(numbers[6]) # Error IndexError: list index out of range
print(numbers[-1])
print(numbers[-2])

print(names[2])
print(mixed[2])

# ทำการเปลี่ยนค่าสมาชิกภายใน List
names[0] = "Bob"
print(names[0])

# การสร้าง List แบบว่าง
numbers2 = []

# เพิ่มสมาชิกใน List ว่าง
numbers2.append(5)
numbers2.append(10)
numbers2.append(15)
numbers2.append(20)

print(numbers2)
print(numbers2[3])

print("----------------------------")

numbers = [10, 20, 30, 40, 50, 60, 70]

# อ่านสมาชิกทั้งหมด
sum = 0
for n in numbers:
    sum += n
    # print(n)

print(sum)

print("----------------------------")

names2 = ['Mateo', 'Danny', 'James', 'Thomas', 'Luke']
print(len(names2))

for i in range(0, len(names2)):
    print(names2[i].upper(), end=" ")
