numbers = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]
a=len(numbers)
def f(x):
    for y in range(a):
        if x>50 and x%2!=0: return 1
    return 0
print(numbers)
print(list(filter(f,numbers)))