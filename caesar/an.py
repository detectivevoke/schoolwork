

with open("reverse.py", 'r') as inFile, open("ang/reverse.py", 'w') as outFile:
    for line in inFile:
        outFile.write(line.strip("\n")+"#i am not your slave, do it yourself \n")