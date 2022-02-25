import json

def separation(line, unit_list=[]):
    for i_unit in range(len(line)):
        if line[i_unit].isupper():
            if (i_unit + 1) < len(line) and line[i_unit + 1].islower():
                unit = line[i_unit] + line[i_unit + 1]
            else:
                unit = line[i_unit]
            unit_list.append(unit)

    return unit_list

with open('import_file_3.txt') as file:
    line = file.readline()
    unit_list = separation(line)

periodic_table = json.load(open('periodic_table.json'))

res_list = ''
for i_list in unit_list:
    res_list += str(periodic_table.get(i_list))

    with open('output_file_3.txt', 'a') as output_file:
        output_file.write(str(res_list))