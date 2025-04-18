try:
    file = open('sample.txt', 'r')
    lines = file.readlines()
except FileNotFoundError:
    print("The file 'sample.txt' was not found")
else:
    for i, line in enumerate(lines):
        print(f"Line {i}: {line}")
    file.close()