
import sys, argparse, csv
import lcFormat

#----------------------------------------------------

# training data file in csv format
trainData="./data/LoanStats.h100.csv"

#---------------------------------------------------

def readCsv():
    nbLinesRead = 0
    nbLinesParsed = 0
    records = []
    with open(trainData, "r") as trainDataCsv:
        trainDataReader = csv.reader(trainDataCsv, delimiter=",")
        for row in trainDataReader:
            nbLinesRead += 1
            # skip non valid csv lines likes comments or headers
            if len(row) == lcFormat.NB_COL:
                nbLinesParsed += 1
                records.append(row)
                #print "XX".join(row)
    print "nbLinesRead="+str(nbLinesRead)
    print "nbLinesParsed="+str(nbLinesParsed)
    return records

def removeIllFormed():
    pass

def normalize():
    pass

def transform2Matrix():
    pass

def main():
    readCsv()

if __name__ == "__main__":
    main()
