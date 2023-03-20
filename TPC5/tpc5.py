import re

flag=0
cash=0
accepted=["1c","2c","5c","10c","20c","50c","1e","2e"]
while True:
    line=input()
    if(flag):
        if re.match("(?i:MOEDA)",line):
            coinvalues = re.findall(r"\d+[ce]",line)
            for currency in coinvalues:
                if currency in accepted:
                    if(currency[-1]=="c"): cash+=int(currency[:-1])
                    elif(currency[-1]=="e"): cash+=int(currency[:-1])*100
                else:
                    print(f"{currency} - moeda inválida; ")
            print(f"saldo = {int(cash/100)}e{cash%100}c")
        elif re.match("(?i:POUSAR)",line):
            print(f"troco = {int(cash/100)}e{cash%100}c; Volte sempre!")
            flag=0
            cash=0
        elif re.match("(?i:ABORTAR)",line):
            flag=0
            cash=0
        elif re.match("(?i:t=)",line):
            number = re.search(r'[^(601|641)](\d{9}|00\d+)$',line).group(1)
            if(number):
                if re.match(r"00",number):
                    if(cash<150):
                        print("Saldo insuficiente.")
                    else:
                        cash-=150
                elif number[0]=="2":
                    if(cash<25):
                        print("Saldo insuficiente.")
                    else:
                        cash-=25
                elif re.match(r"808",number):
                    if(cash<10):
                        print("Saldo insuficiente.")
                    else:
                        cash-=10
                print(f"Saldo = {int(cash/100)}e{cash%100}c")
            else:
                print("Esse número não é permitido neste telefone. Queira discar novo número!")     
    else:
        if re.match("(?i:levantar)",line):
            flag=1
            print("Introduza moedas.")