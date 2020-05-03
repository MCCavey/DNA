import sys
import csv

#check correct argument used
if len(sys.argv) != 3:
    print("Incorrect number of arguments")
    sys.exit()

#open csv file and find number of columns
f = open(sys.argv[1], 'r')
reader = csv.reader(f)
ncol = len(next(reader))  # Read first line and count columns
f.seek(0)                 # go back to beginning of file

#create dict to store no. of each SRT in a row
dict = {}
for row in reader:
    for x in range(ncol):
        if x != 0:
            dict[f'{row[x]}'] = 0
    break

#open sequence
file = open(sys.argv[2], "r")
sequence = file.read()

#loop through every char in sequence and see how many iterations of STR it has
index = 0
for char in sequence:
    f.seek(0)
    #loop through rows of csv but only act on 1st row
    for row in reader:
        #only look for srt's in row 0 of csv file, not "name" in the 1st column
        for x in range(ncol):
            if x != 0:
                #find how many of this SRT in a row from this char
                score = 0
                length = len(row[x])
                while(sequence.find(row[x], index, index + length) != -1):
                    score += 1
                    index += len(row[x])
                #if this is the longest run of that SRT, update dict
                if score > dict[row[x]]:
                    dict[row[x]] = score
        break
    index += 1



f.seek(0)
#create array of the SRT's
array = []
for row in reader:
    for x in range(ncol):
        array.append(row[x])
    break

f.seek(0)
for row in reader:
    for x in range (ncol):
        if x != 0:
            print(f"{row[x]}")
            print(f"{dict[array[x]]}")
            if row[x] != dict[array[x]]:
                break
            print(f"{row[0]}")





