num = int(input())
while num == 0:
    print("Вы ввели 0, повторите попытку.")
    num = int(input())
flag = False
for i in range(2,num//2+1):
    if num%i == 0:
        flag = True
        break
if flag == True:
    print("Число не простое")
else:
    print("Число простое")