from collections import defaultdict

def read_file(filePath: str):
    file = open(filePath, 'r')
    Lines = file.readlines()

    num_list = []
    for Line in Lines:
        num_list.append(int(Line))

    return num_list

def add_numbers(num_list: list):
    num_dict = defaultdict(list)
    for i in enumerate(num_list):
        num_dict[i[1]].append(i[0])
    
    return num_dict

def target_count(num_dict: dict, targets : range):
    unique_keys = list(num_dict.keys())
    count = 0
    for key in unique_keys:
        for target in targets:
            if num_dict[target - key] != 0:
                count += 1
    return count


def main():
    num_list = read_file('Chapter2\\2-4 2-Sum.txt')
    num_dict = add_numbers(num_list)
    range = (-10000, 10001)
    print(target_count(num_dict, range))

if __name__ == '__main__':
    main()