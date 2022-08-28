dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4, 'five': 5}
dict2={}
for i in dict:
    a=dict.get(i)
    if a>=3: dict2[i]=a
print(dict2)