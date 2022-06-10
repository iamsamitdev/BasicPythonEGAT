# ลองเขียนโปรแกรมรับค่า username and password จากผู้ใช้
# มาทำงานเปรียบเทียบค่า

print("Please enter username and password")

username = input("Username: ")
password = input("Password: ")

# print(username, password)

# ตรวจสอบเงื่อนไขด้วย if...else
if(username == "admin" and password == "123456"):
    print("Login Success")
else:
    print("Login Fail!!")