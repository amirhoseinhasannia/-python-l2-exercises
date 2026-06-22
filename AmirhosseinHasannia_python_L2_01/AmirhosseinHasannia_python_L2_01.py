"hasannia_exrecise"

from getpass import getpass  # برای دریافت پسورد بدون نمایش در صفحه

# دریافت نام کاربری (تا زمانی که خالی نباشد)
while True:
    uname = input("Please enter your username: ")
    if uname == "":
        print("Username cannot be empty. Please try again.")
    else:
        break

# ---------------------------------------------------------------------

# دریافت پسورد (با getpass که پسورد را نمایش نمی‌دهد)
while True:
    upass = getpass("Please enter your password:")
    if upass == "":
        print("Password cannot be empty. Please try again. ")
    else:
        break

# ---------------------------------------------------------------------

# چاپ نام کاربری و پسورد
print(f"Username:{uname}")
print(f"Password:{upass}\n")

# بررسی هشت فیلتر روی پسورد
print("Filter checks:")
score_pass = 8  # امتیاز اولیه
Reason_for_rejection = ""  # ثبت دلایل رد پسورد

# 1. حداقل طول 8 کاراکتر
if len(upass) < 8:
    print("X Password is shorter than 8 characters.")
    score_pass -= 1
    Reason_for_rejection += "Password is shorter than 8 characters.\n"
else:
    print("Password length is sufficient. ")

# 2. داشتن حداقل یک حرف انگلیسی
if not any(i.isalpha() for i in upass):
    print("X Password does not contain any English letters.")
    score_pass -= 1
    Reason_for_rejection += "Password does not contain any English letters.\n"
else:
    print("Contains at least one English letter.")

# 3. داشتن حداقل یک کاراکتر خاص @ $ !
if not any(i in "@$!" for i in upass):
    print("X password does not contain any special characters.")
    score_pass -= 1
    Reason_for_rejection += "password does not contain any special characters.\n"
else:
    print("Contains at least one special character.")

# 4. داشتن حداقل یک حرف بزرگ انگلیسی
if not any(i.isupper() for i in upass):
    print("X Password does not contain any uppercase letters.")
    score_pass -= 1
    Reason_for_rejection += "Password does not contain any uppercase letters.\n"
else:
    print("Contains at least one uppercase letter. ")

# 5. یکسان نبودن با نام کاربری
if upass == uname:
    print("X Password is identical to the username.")
    score_pass -= 1
    Reason_for_rejection += "Password is identical to the username.\n"
else:
    print("Password is not identical to the username.")

# 6. پسورد برابر با swapcase نام کاربری نباشد
if upass == uname.swapcase():
    print("X Password is the swapcase version of the username.")
    score_pass -= 1
    Reason_for_rejection += "Password is the swapcase version of the username.\n"
else:
    print("Password is not the swapcase version of the username.")

# 7. نسخه خاص‌سازی‌شده‌ی نام کاربری با @ $ ! 0 نباشد
uname_lower = uname.lower()
replacements = {"a": "@", "i": "!", "s": "$", "o": "0"}  # جدول جایگزینی
for k, v in replacements.items():
    uname_lower = uname_lower.replace(k, v)

if upass.lower() == uname_lower:
    print(
        "X Is a special-character version of the username"
        " (s → $, a → @, i → !, o → 0)."
    )
    score_pass -= 1
    Reason_for_rejection += (
        "Is a special-character version of the username (s → $, a → @, i → !, o → 0).\n"
    )
else:
    print("Password is not a special-character version of the username.")

# 8. یکی نبودن با لیست پسوردهای خیلی رایج
Xpass = [
    "123456",
    "12345678",
    "12345",
    "111111",
    "123456789",
    "qwerty",
    "asdfgh",
    "zxcvbnm",
    "password",
    "admin",
    "P@s$w0rd",
]

if upass in Xpass:
    print("X Password is one of the most common passwords.")
    score_pass -= 1
else:
    print("Not a common password.")

# ---------------------------------------------------------------------

# چاپ امتیاز نهایی
print(f"\nFinal Score: {score_pass} out of 8")

# تعیین سطح امنیتی
if score_pass == 8:
    print("Security Level: Strong")
elif score_pass <= 7 and score_pass >= 4:
    print("Security Level: Medium")
else:
    print("Security Level: Very Weak")

# چاپ دلایل رد شدن بخش‌ها
print(f"Because \n{Reason_for_rejection}")

# دو فعالیت اضافه وجود داشت  در انتهای فایل تمرین که تکراری و راحت بود. در این کد قرار ندادم
