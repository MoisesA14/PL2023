from prettytable import PrettyTable


def parse(myheart: str):
    struct = []
    with open(myheart, "r") as content:
        fstline = content.readline().strip().split(",")
        
        for line in content:
            row={}
            data = line.rstrip().split(",")

            for a in range(len(fstline)):
                row[fstline[a]] = data[a]

            struct.append(row)

    return struct


def distByGender (struct:list[object]):
  genders={'Masc. c/ doença':0, 'Fem. c/ doença':0}

  for dataset in struct:
    if dataset.get('temDoença')=='1':
      if dataset['Gender']=='M':
        genders['Masc. c/ doença']+=1
      elif dataset['Gender']=='F':
        genders['Fem. c/ doença']+=1
      else:
        print ('Error')
  return genders


def distByAge (struct):
    Ages=[]
    for dataset in struct:
        Ages.append(int(dataset['Age']))
    AgeMax=max(Ages)


    AgeRanges={}
    for a in range(30, AgeMax,4):
        AgeRanges[f"{a}-{a+4}"]=0

    for dataset in struct:
        Age=int(dataset['Age'])
        for gap in AgeRanges:
            i,f=map(int, gap.split("-"))
            if i<=Age<=f and dataset['temDoença']=='1':
                AgeRanges[gap]+=1

    return AgeRanges

def distByCholesterol(struct):
    col=[]
    for dataset in struct:
        col.append(int(dataset['colesterol']))
    

    colMin=min(col)
    colMax=max(col)

    colRanges={}
    for c in range(colMin,colMax,10):
        colRanges[f"{c}-{c+10}"]=0

    for dataset in struct:
        colest=int(dataset['colesterol'])
        for gap in colRanges:
            i,f=map(int, gap.split("-"))
            if i<=colest<=f and dataset['temDoença']=='1':
                colRanges[gap]+=1


    return colRanges

def tabelaDist(dic: dict, subject: str):

    table = PrettyTable(["Intervalo", subject])

    for content, number in dic.items():
        table.add_row([content, number])

    return table


def selectDistributions(data):
    subject: str
    selection= 1
    while (selection != 0):
        selection = int(input(
            "Selecionar:\n1 - Por género\n2 - Por idade\n3 - Por colesterol\n"))
        if selection != 0:
            if selection == 1:
                subject = "Gender"
                print(tabelaDist(distByGender(data),subject))
                break
                
            elif selection == 2:
                subject = "Age"
                print(tabelaDist(distByAge(data),subject))
                break
                
            elif selection == 3:
                subject = "Cholesterol"
                print(tabelaDist(distByCholesterol(data),subject))
                break
                
            else:
                print("Error")
                break


def main():
    data=parse("myheart.csv")
    selectDistributions(data)


main()