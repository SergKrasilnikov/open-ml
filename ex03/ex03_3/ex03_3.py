with open('import_file_2_1.txt') as file1, open('import_file_2_2.txt') as file2:
    first_line_file2 = file2.readline()
    first_line_file1 = file1.readline()
    line_second = first_line_file2.split()
    res = first_line_file1[int(line_second[0]):int(line_second[1]) + 1]
    with open('output_file_2.txt', 'a') as output_file:
        output_file.write(str(res))

    for line1, line2 in zip(file1, file2):
        line_second = line2.split()
        res = line1[int(line_second[0]):int(line_second[1]) + 1]
        with open('output_file_2.txt', 'a') as output_file:
            output_file.write(' ' + str(res))