# تعریف حروف الفبا
lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                     'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                     'u', 'v', 'w', 'x', 'y', 'z']

uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                     'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                     'U', 'V', 'W', 'X', 'Y', 'Z']

text = input("Enter a message: ")
encrypted = ""

# پیمایش کاراکتر به کاراکتر
for char in text:
    # اگر حرف کوچک باشد
    if char in lowercase_letters:
        index = 0
        while index < len(lowercase_letters):
            if lowercase_letters[index] == char:
                break
            index = index + 1
        # رفتن ۳ خانه جلوتر با بررسی انتهای لیست
        new_index = index + 3
        if new_index >= len(lowercase_letters):
            new_index = new_index - 26
        encrypted = encrypted + lowercase_letters[new_index]

    # اگر حرف بزرگ باشد
    elif char in uppercase_letters:
        index = 0
        while index < len(uppercase_letters):
            if uppercase_letters[index] == char:
                break
            index = index + 1
        new_index = index + 3
        if new_index >= len(uppercase_letters):
            new_index = new_index - 26
        encrypted = encrypted + uppercase_letters[new_index]

    # اگر چیز دیگری بود (فاصله، عدد، علامت و...) بدون تغییر اضافه شود
    else:
        encrypted = encrypted + char

print("Encrypted message:", encrypted)
