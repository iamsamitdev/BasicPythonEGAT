# การสร้างฟังก์ชันใน Python
def hello():
    print("Hello Python")


# การเรียกใช้งานฟังก์ชัน hello
hello()


# การสร้างฟังก์ชันใน Python
def info(msg):
    print("Welcom to ", msg)


# การเรียกใช้งานฟังก์ชัน info
info("ITGenius")


# การสร้างฟังก์ชันใน Python
def area(width, height):
    result = width * height
    return result


# การเรียกใช้งานฟังก์ชัน area
print("Area is", area(10, 20))


# สร้างฟังก์ชันเช็คเบอร์มงคล
def berdee(phone_number):

    total = 0
    if len(phone_number) == 10:
        # หาผลรวมเบอร์โทรศัพท์
        for n in phone_number:
            total = total + int(n)
        return total
    elif len(phone_number) > 10:
        return 'ป้อนเบอร์เกิน'
    elif len(phone_number) < 10:
        return 'ป้อนเบอร์ไม่ครบ 10 หลัก'
    else:
        return 'รูปแบบเบอร์ไม่ถูกต้อง'

# เรียกใช้งานฟังก์ชัน berdee   
phone = input("ป้อนเบอร์โทรศัพท์ของคุณ :") 
print(berdee(phone))


def show_info(name = "", salary = 84360, lang = "Python"):
    print('Name: %s' % name)
    print('Salary: %d' % salary)
    print('Language: %s' % lang)
    print()


# เรียกใช้ฟังก์ชัน show_info
show_info()
show_info("Samit")
show_info("Wichai", 100000, "Java")