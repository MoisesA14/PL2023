import re
import statistics
import json
import sys

json_list = []
vals_list = []
info_list = []

csv_file = open(sys.argv[1],"r")

lines = list(csv_file.readlines())

matches = re.finditer(r"(\w+)(?:\{(\d+)(?:,(\d+))?})?(?:::)?(\w+)?", lines[0])

for match in matches:
    info_list.append(match.group(1))
    if (match.group(2) != None):
        data_string = r""
        for i in range(0,int(match.group(2))):
            data_string += r",(\d+)"
        if (match.group(3) != None):
            for i in range(int(match.group(2)),int(match.group(3))):
                data_string += r",(\d+)?"
        if (match.group(4) != None):
            vals_list.append((data_string,match.group(4)))
        else:
            vals_list.append((data_string,None))

    else:
        data_string = r"([\w ]+)"
        vals_list.append((data_string,None))

for line in lines[1:]:
    tam = len(info_list)

    obj = {}
    for i,(val,calc) in enumerate(vals_list):
        if val == r"([\w ]+)":
            splits = re.split(r"([\w ]+)", line, 1)
            line = splits[2]
            obj[info_list[i]] = splits[1]
        else:
            splits = re.split(val, line, 1)
            line = splits [-1]
            list = []
            for s in splits[1:len(splits)-1]:
                if s is not None:
                    list.append(int(s))

            save = info_list[i]
            value = None

            if calc == 'media':
                value = statistics.mean(list)
                info_list[i] = info_list[i] + "_media"
            elif calc == 'sum':
                value = sum(list)
                info_list[i] = info_list[i] + "_sum"
            elif calc == 'min':
                value = min(list)
                info_list[i] = info_list[i] + "_min"
            elif calc == 'max':
                value = max(list)
                info_list[i] = info_list[i] + "_max"
            elif calc == 'mode':
                value = statistics.mode(list)
                info_list[i] = info_list[i] + "_mode"
            elif calc == None:
                value = list

            obj[info_list[i]] = value

            info_list[i] = save

    if line == "\n" or line == "":
        json_list.append(obj)

with open(sys.argv[1][:-4] + ".json",'w') as json_file:
    json.dump(json_list, json_file, indent=4, ensure_ascii=False)