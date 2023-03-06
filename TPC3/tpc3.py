import re
import json

dicts_file = []

def make_dictionary():
    file = open("processos.txt","r")
    for line in file:
        dictionary = {}
        items = line.split("::")
        if (len(items) < 6):
            continue
        dictionary["number"] = items[0]
        date_y_m_d = items[1].split("-")
        dictionary["year"] = date_y_m_d[0]
        dictionary["month"] = date_y_m_d[1]
        dictionary["day"] = date_y_m_d[2]
        dictionary["name"] = items[2]
        dictionary["dad"] = items[3]
        dictionary["mom"] = items[4]
        dictionary["extras"] = items[5]
        dicts_file.append(dictionary)

#a) Frequência de processos por ano

def processes_per_year():
    result = {}
    for entry in dicts_file:
        year = entry["year"]
        result[year] = result.setdefault(year, 0) + 1
    return result

def det_century(century : str):
    half = len(century)//2
    cen = int(century[:half])
    if (int(century[half:]) != 0):
        cen += 1
    return cen

def det_names(name : str):
    names = name.split(" ")
    return names

def name_count_sorted(list_dicts):
    names = {}
    for i in list_dicts.values(): 
        for m,n in i.items():
            if (m in names.keys()):
                names[m] = names[m] + n
            else:
                names[m] = n
        names = dict(sorted(names.items(),key=lambda x: x[1]))
    return names

#b)Frequência de nomes próprios e apelidos p/ século & 5 mais usados

def names_per_century():
    result = {}
    for entry in dicts_file:
        century = det_century(entry["year"])
        result[century] = result.setdefault(century,{})
        names = det_names(entry["name"])
        firstname = names[0]
        surname = names[-1]
        result[century][firstname] = result[century].setdefault(firstname,0) + 1
        result[century][surname] = result[century].setdefault(surname,0) + 1
    names = name_count_sorted(result)
    keys = list(names)
    for x in range(-1,-6,-1):
        print(str(keys[x]) + ":" + str(names[keys[x]]) + "\n")
    return result

#c) Frequência de cada relação

def rel_freq():
    result = {}
    for entry in dicts_file:
        relationships = re.findall(',((\w+)( \w+)*)\.',entry["extras"])
        for element in relationships:
            result[element[0]] = result.setdefault(element[0],0) + 1
    return result

#d) 20 primeiros registos em json

def first_20_records():
    result = open("result.json","w")
    for i in range(0,19):
        result.write(json.dumps(dicts_file[i], indent=4))
    result.close()
        
make_dictionary()