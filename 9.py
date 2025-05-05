text = input("Enter a text: ")

letter_count = 0
digit_count = 0

for ch in text:
    if (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z'):
        letter_count = letter_count + 1
    elif ch >= '0' and ch <= '9':
        digit_count = digit_count + 1

print("Letters:", letter_count)
print("Digits:", digit_count)
