import fileinput
if 1:
    with fileinput.FileInput('./db',inplace='true', backup='.bak') as file:
        for line in file:
            lc=line.split()
            if len(lc)>0:
                k=len(lc)
                print('\'',end='')
                for i in range (0,k-2):
                    print (lc[i],end=' ')
                print (lc[k-2],end='')
                print('\'',end='')
                print (' : ',end='')
                print('\'',end='')
                print (lc[k-1],end='')
                print('\',')
            else:
                print(line,end='')
else :
    print("Invalid Input")

