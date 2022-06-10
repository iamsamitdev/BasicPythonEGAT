# การสร้างตัวแปรไม่ต้องระบุชนิดข้อมูล
a = 3
b = 4.95
c = "Python Programming"

print(a)
print(b)
print(c)

print(a, b, c)

# สามารถสร้างตัวแปรหลายตัวพร้อมกันในบรรทัดเดียว
x = y = z = 10
j, k = 5, 15

print(x, y, z)
print(j, k)

# Boolean
status = True
msg = False

print(status, msg)
print(status == 1)
print(msg == 0)

# การแสดงร่วมกับข้อความ
# วิธีที่ 1 ใช้ Concat String
print("ราคาสินค้าต่อชิ้น", b, "บาท มีจำนวน", a, "ชิ้น")

# วิธีที่ 2 ใช้ Interpolation String
print("ราคาสินค้าต่อชิ้น %.2f บาท มีจำนวน %d ชิ้น" % (b, a))

# วิธีที่ 3 ใช้ Format String
print(f"ราคาสินค้าต่อชิ้น {b} บาท มีจำนวน {a} ชิ้น")
