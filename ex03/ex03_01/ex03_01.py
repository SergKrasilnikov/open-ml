def check_operator(i_line):
    line = i_line.split()
    num = 0
    if line[0] == '+':
        num = int(line[1]) + int(line[2])
    elif line[0] == '-':
        num = int(line[1]) - int(line[2])
    elif line[0] == '*':
        num = int(line[1]) * int(line[2])
    elif line[0] == '//' and int(line[1]) > 0 and int(line[2]):
        num = int(line[1]) // int(line[2])
    elif line[0] == '%' and int(line[1]) > 0 and int(line[2]):
        num = int(line[1]) % int(line[2])
    elif line[0] == '**' and int(line[1]) > 0 and int(line[2]):
        num = int(line[1]) ** int(line[2])

    return num

with open('input_file.txt', 'r') as file:
    first_line = file.readline()
    res = check_operator(first_line)

    with open('output_file.txt', 'a') as output_file:
        output_file.write(str(res))

    for i_line in file:
        res = check_operator(i_line)
        with open('output_file.txt', 'a') as output_file:
            output_file.write(',' + str(res))
