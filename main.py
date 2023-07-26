from pyrogram import Client
import time, os
a = int(input("Input start phone in format [DC][4NUMS]: "))
phone_numbers = []
for i in range(6600000 + a, 6639999):
    phone_numbers.append("+999" + str(i))

number = phone_numbers[0]
code = phone_numbers[0][6] * 5
print(f"[BRV2] {number} : {code}")

app = Client(number,
             api_id=,
             api_hash="",
             test_mode=True,
             phone_number=number,
             phone_code=code)

print("[BRV2] Client prepared, starting.")
while True:
    try:
        with app:
            # Do something here #
            os.remove(f"{number}.session")
            phone_numbers.pop(0)
            number = phone_numbers[0]
            code = phone_numbers[0][6] * 5
            print(f"[BRV2] {number} : {code}")
            app = Client(number,
             api_id=,
             api_hash="",
             test_mode=True,
             phone_number=number,
             phone_code=code)
            print("[BRV2] Client prepared, starting.")
            time.sleep(1.5)
    except:
        os.remove(f"{number}.session")
        phone_numbers.pop(0)
        number = phone_numbers[0]
        code = phone_numbers[0][6] * 5
        print(f"[BRV2] {number} : {code}")
        app = Client(number,
             api_id=,
             api_hash="",
             test_mode=True,
             phone_number=number,
             phone_code=code)
        print("[BRV2] Client prepared, starting.")
        time.sleep(1.5)
        

