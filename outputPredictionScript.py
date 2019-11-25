import sys

out = open("outputPrediction.txt", "w+")

with open(sys.argv[1]) as x:
    for line in x:
        l = line.split()
        l1, l2 = l[2].split(":")
        #print(l2)
        out.write(l2)
        out.write("\n")