# คือการ import มาทั้งหมด
# import number

# print(number.factorial(5)) # 5x4x3x2x1
# print(number.fibonacci(100))

# การ import มาบางส่วนของไฟล์
# from number import factorial, fibonacci
# from number import *

# print(factorial(5))
# print(fibonacci(100))

# การ import พร้อมกับตั้งชื่อนามแฝง
# from number import factorial as ft, fibonacci as fb

# print(ft(5))
# print(fb(100))

# Import จาก package numberpackage
from numberpackage import calculate as cl
from numberpackage import number as nb

print(cl.plus(2,3))
print(nb.factorial(5))
print(nb.fibonacci(100))
