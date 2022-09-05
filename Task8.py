with open('file_1.txt','r',) as f:
    text = f.read()
    text2 = text[::-1]
with open('file_2.txt','w',) as f:
    f.write(text2)

with open('file_1.txt','r',) as f:
    print('file_1 \n' +f.read())

with open('file_2.txt','r',) as f:
    print(' \nfile_2 \n' + f.read())
