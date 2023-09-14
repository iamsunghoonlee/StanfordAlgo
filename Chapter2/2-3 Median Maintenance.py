def read_file(filePath: str):
    file = open(filePath, 'r')
    Lines = file.readlines()

    num_list = []
    for Line in Lines:
        num_list.append(Line)

    return num_list


def main():
    num_list = read_file("Chapter2\\2-3 Median Maintenance.txt")
    

if __name__ == "main":
