import time

num = 0
count = 1

while True:
    if num == 1:
        print(f"Round {count} = {num}")
        num = 0
    else:
        print(f"Round {count} = {num}")
        num = 1
    if count >= 10:
        break
    time.sleep(1)
    count = count + 1