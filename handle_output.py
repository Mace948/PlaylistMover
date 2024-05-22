def extractSongsFromFile(file_path):
    string_list = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            string_list.append(line.strip())
    return string_list

def saveStringsToFile(string_list, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        for string in string_list:
            file.write(string + '\n')
