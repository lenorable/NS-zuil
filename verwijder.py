output = 1

getallen = []
while True:
    inp = input('getal of "stop": ')
    if inp != "stop":
        getallen.append(int(inp))
    else:
        for i in getallen:
            output = output * i
            print(output)
            break