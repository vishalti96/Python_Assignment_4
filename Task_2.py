data = input("Enter text to write to the file: ")
with open('output.txt','w') as fh:
    fh.write(data+"\n")
print("Data successfully written to output.txt")

additional_text = input("Enter additional text to append: ")
with open('output.txt','a') as fh:
    fh.write(additional_text+"\n")
print("Data successfully appended.")
print("Final content of output.txt: ")
with open('output.txt','r') as fh:
    for line in fh:
        print(line,end='')
