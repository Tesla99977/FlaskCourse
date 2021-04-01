result = int(input())
sym = input()
while sym != "=":
    space = sym.find(" ")
    num2 = int(sym[space+1:])
    sym = sym[:space]
    if sym == "+":
        result = result + num2
    elif sym == "-":
        result = result - num2
    elif sym == "*":
        result = result * num2
    elif sym == "/":
        result = result / num2
    elif sym == "**":
        result = result**num2
    else:
        print("Операция неясна, повторите ввод!")
    sym = input()
print(result)