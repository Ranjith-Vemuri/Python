import argparse
import sys
import time


# Taking input as a file, reading a file and checking the email syntax and returns a dictionary
def read(file):
    try:
        with open(file, 'r') as f:
            rl = f.readlines()
            li = [i for i in rl if i.strip()]
        if len(li) <= 0:
            raise Exception(f"{file} File Exists but no Data Found.")
        dic = {}
        for i in li:
            if '@' in i:
                parts = i.split('@')
                if len(parts) == 2 and '.' in parts[1]:
                    dic[i] = True
        return dic
    except FileNotFoundError:
        print(f"File {file} not found.")
        sys.exit(1)


# Taking 2 dictionaries, performs union of those Dictionaries and returns as a list
def union(l1, l2):
    l3 = {}
    l3.update(l1)
    l3.update(l2)
    u = {}
    for i in l3:
        if i not in u:
            u[i] = True
    return list(u.keys())


# Taking 2 dictionaries, performs intersection of those Dictionaries and returns as a list
def intersection(l1, l2):
    if len(l1) <= len(l2):
        inst = {}
        for i in l1:
            if i in l2 and i not in inst:
                inst[i] = True
        return list(inst.keys())
    else:
        inst = {}
        for i in l2:
            if i in l1 and i not in inst:
                inst[i] = True
        return list(inst.keys())


# Taking 2 dictionaries, performs minus of those Dictionaries and returns as a list
def minus(l1, l2):
    if len(l1) <= len(l2):
        m = {}
        for i in l1:
            if i not in l2 and i not in m:
                m[i] = True
        return list(m.keys())
    else:
        for i in l2:
            if i in l1:
                del l1[i]
        return list(l1.keys())


# Taking input as a result and writing in resultant file
def write(file, result):
    with open(file, 'w') as f:
        f.write(''.join(result))


# main function to call the all functions
def main(arg):
    try:
        start_time = time.time()
        l1 = read(arg.input1)
        l2 = read(arg.input2)
        if sys.argv[0] == 'union.py':
            result = union(l1, l2)
        elif sys.argv[0] == 'intersection.py':
            result = intersection(l1, l2)
        elif sys.argv[0] == 'minus.py':
            result = minus(l1, l2)
        else:
            raise ValueError("Invalid Operation. Valid Operations are: union, intersection, minus.")
        write(arg.output, result)
        end_time = time.time()
        print(f'Output: {arg.input1}: {len(l1)} emails, {arg.input2}: {len(l2)} emails,', end=' ')
        print(f'{arg.output}: {len(result)} emails; Time taken: {int(end_time - start_time)} seconds')
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Process input files and perform Union, intersection, and minus operations on email lists.'
    )
    parser.add_argument('input1', type=str, help='path to first input file')
    parser.add_argument('input2', type=str, help='path to second input file')
    parser.add_argument('output', type=str, help='path to output file')
    args = parser.parse_args()
    main(args)
