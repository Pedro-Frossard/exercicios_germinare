from time import sleep 

for i in range(10,-1,-1):
    if i == 10:
        print(i)
        continue
    sleep(1)
    print(i)
print('FELIZ ANO NOVOOOO')