# หาผลรวมเบอร์โทรศัพท์ของผู้ใช้
phone = input("ป้อนเบอร์โทรศัพท์ 10 หลัก: ") # string

total = sum(int(c) for c in phone)
# print(total)
# ทำนายผลรวมที่ได้
if total in (9, 14, 15, 19, 23, 24, 32, 36, 40, 41, 42, 44, 45, 46, 50, 51, 54, 55, 56, 59, 63, 64, 65):
    print("ดีมาก")
elif total in (69, 79):
    print("โอกาสประสบผลสำเร็จสูง อุปสรรคน้อย เจริญรุ่งเรือง ร่ำรวย รวดเร็ว และมีความสุข")
elif total in (10, 13, 16, 18, 20, 22, 25, 26, 28, 31, 35, 38, 39, 47, 49, 52, 53, 57, 58, 60, 61):
    print("ดีปานกลาง")
elif total in (62, 66, 68, 74, 75):
    print("เหนื่อย มีอุปสรรค แต่ยังมีโอกาสประสบผลสำเร็จ หากมีความพยายาม")        
elif total in (11, 12, 17, 21, 27, 29, 30, 33, 34, 37, 43, 48, 67, 70, 71, 72, 73, 76, 77, 78, 80):
    print("เหนื่อยมาก อุปสรรคมาก เจอปัญหารุมเร้า การงาน การเงิน ความรัก เกิดอุบัติเหตุชีวิตไม่จบไม่สิ้น") 
else:
    print("ไม่พบข้อมูล")
