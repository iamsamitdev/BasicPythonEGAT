import time

num = 0
count = 1

while True:
    print(f"Round {count} = {num}")
    num = 0 if num == 1 else 1
    if count >= 10:
        break
    time.sleep(1)
    count = count + 1