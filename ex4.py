a = int(input('Please enter your number:'))
m = 0

while not a == 0:
    h = a % 10
    if h > m:
        m = h
    a = a // 10
print(m)