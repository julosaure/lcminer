
import sys, argparse, csv, pprint
import numpy as np, sklearn as skl, sklearn.feature_extraction as skl_fe
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
    # distribution of classes among records
    x = {}
    for s in records:
        try:
            x[s.target] += 1
        except KeyError:
            x[s.target] = 1
    print x
    return records

def removeIllFormed(records):
    # filter records without correct class labels
    # records = filter(lambda record: record.target in lcFormat.targets, records)
    print "nb records well formed="+str(len(records))
    return records

def normalize():
    pass

def records2Arrays(records):
    sk_records = {}
    sk_records["target_names"] = np.array(lcFormat.targets)
    sk_records["target"] = np.array([lcFormat.targets.index(rec.target) for rec in records])
    dv = skl_fe.DictVectorizer()
    sk_records["data"] = dv.fit_transform(records)
    sk_records["feature_names"] = dv.get_feature_names()
    
    #pp = pprint.PrettyPrinter()
    #pp.pprint(sk_records)
    print sk_records
    return sk_records

def preprocessData(data):
    rows = readCsv(data)
    records = csv2Records(rows)
    records = removeIllFormed(records)
    sk_records = records2Arrays(records)
    return sk_records

if __name__ == "__main__":
    preprocessData(trainData)
