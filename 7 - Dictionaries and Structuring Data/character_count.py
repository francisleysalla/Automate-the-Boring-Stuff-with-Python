print("Write a text for me to count how much of each character is in it:")
text = input()
count = {}
for char in text:
    count.setdefault(char, 0)
    count[char] += 1

print(f"Here is the count of each character: {count}")