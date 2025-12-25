try:
    with open('sample.txt','r') as fh:
        data = fh.readlines()
    count=1
    print("Reading file content")
    for line in data:
        print(f"Line {count}: {line}",end='')
        count+=1
except FileNotFoundError as e:
    print(e)
