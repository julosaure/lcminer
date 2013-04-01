
import sys, argparse, csv, string
import lcFormat

#----------------------------------------------------

# training data file in csv format
trainData="./data/LoanStats.h100.csv"
#trainData="./data/InFunding2StatsNew (1).csv"

#---------------------------------------------------

def readCsv(data):
    nbLinesRead = 0
    nbLinesParsed = 0
    rows = []
    with open(data, "r") as dataCsv:
        dataReader = csv.reader(dataCsv, delimiter=",")
        for row in dataReader:
            nbLinesRead += 1
            # skip non valid csv lines likes comments or headers
            if len(row) != lcFormat.NB_COL:
                continue
            # skip csv column names
            if row[0].lower() == "loan id":
                continue
            nbLinesParsed += 1
            rows.append(row)
                
    print "nb rows read="+str(nbLinesRead)
    print "nb rows parsed="+str(nbLinesParsed)
    return rows

def csv2Records(rows):
    converter = lcFormat.lcRow2Rec()
    records = map(converter.row2Rec, rows)
    return records

def removeIllFormed(records):
    # filter records without correct class labels
    records = filter(lambda record: record.target in lcFormat.targets, records)
    print "nb records well formed="+str(len(records))
    return records

def normalize():
    pass

def transform2Matrix():
    pass

def main():
    rows = readCsv(trainData)
    records = csv2Records(rows)
    records = removeIllFormed(records)

if __name__ == "__main__":
    main()
