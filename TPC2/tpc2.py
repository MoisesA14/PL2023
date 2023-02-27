def negSubtract(num):
    p = ""
    n = ""
    i = 0
    while num[i] != "-":
        p = p + num[i]
        i += 1
    i += 1
    while i < len(num):
        n = n + num[i]
        i += 1
    res = int(p)-int(n)
    return res

def main():
    On = True
    acc = 0
    num = "0"
    text = input("Inserir texto: ")
    print("\n")

    for i in range(0, len(text)):
        if text[i] != "=":
            if On:
                if text[i].isdigit() or text[i] == "-" and text[i+1].isdigit():
                    num = num + text[i]
                else:
                    if "-" in num: 
                     aux = negSubtract(num)
                     acc += int(aux)
                     num = "0"
                    else:
                        acc += int(num)
                        num = "0"

            if text[i] in "Oo" and text[i+1] in "Nn":
                On = True
            if text[i] in "Oo" and text[i+1] in "Ff" and text[i+2] in "Ff":
                On = False
        else:
            if "-" in num:
                aux = negSubtract(num) 
                acc += int(aux)
                num = "0"
            else:
                acc += int(num)
                num = "0"
            print("A soma total é:" + str(acc))

main()