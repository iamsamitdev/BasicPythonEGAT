for i in range(1, 101):
    if i % 5 == 0:
        print(f"{i:03}") # ขึ้นบรรทัดใหม่ print('%03d' % i)
    else:
        print(f"{i:03}", end=" ") # บรรทัดเดียวกัน print('%03d' % i)
