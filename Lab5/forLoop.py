# this is a test to learn the whole for loop thing, it isnt part of the lab Dami

for x in range(5, 10):
    print(x)

print('-----------------------------------------------------------------------------')
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
for d in days:
    print(d)

print('-----------------------------------------------------------------------------')

for i, d in enumerate(days):
    print(i, d)

# this is the break and continue stuffs, used for breaking out of a looped code
print('-----------------------------------------------------------------------------')

for x in range(1, 15):
    if x == 12:
        break
    if (x % 2) == 0:
        continue
    print(x)
print('-----------------------------------------------------------------------------')


def multi_Add(*args):
    result = 0
    for b in args:
        result = result + b
    return result


print(multi_Add(4, 5, 10, 12))


def power(num, x=1):
    result = 1
    for c in range(x):
        result = result * num
    return result


print(power(5, 2))
