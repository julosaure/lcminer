
import sys, argparse, csv, fileinput, csv, string,re

NB_COLUMN=42

HEADER="""
@relation LoanStats

@attribute 'Loan ID' string
@attribute 'Amount Requested' numeric
@attribute 'Amount Funded By Investors' numeric
@attribute 'Interest Rate' string
@attribute 'Loan Length' {'36 months','60 months'}
@attribute 'Application Date' date yyyy-MM-dd
@attribute 'Application Expiration Date' date yyyy-MM-dd
@attribute 'Issued Date' date yyyy-MM-dd
@attribute 'CREDIT Grade' {E2,A2,A4,C1,B1,C4,B5,B3,A5,A3,B2,C2,F4,C5,E1,D3,B4,D1,F1,D4,C3,D2,F2,A1,E4,F3,E5,D5,E3,G5,F5,G1,G4,G3}
@attribute 'Loan Title' string
@attribute 'Loan Purpose' {debt_consolidation,other,credit_card,home_improvement,small_business,educational,vacation,moving,car,wedding,house,medical,major_purchase,renewable_energy}
@attribute 'Loan Description' string
@attribute 'Monthly PAYMENT' numeric
@attribute Status {'Fully Paid','Charged Off'}
@attribute 'Total Amount Funded' numeric
@attribute 'Debt-To-Income Ratio' string
@attribute 'Remaining Principal Funded by Investors' numeric
@attribute 'Payments To Date (Funded by investors)' numeric
@attribute 'Remaining Principal ' numeric
@attribute 'Payments To Date' numeric
@attribute 'Screen Name' string
@attribute City string
@attribute State {MA,MD,NC,CO,WI,FL,NY,GA,IN,VA,ME,NJ,CT,AZ,NE,WA,CA,OH,NM,MO,UT,LA,SC,KS,AL,TN,NH,SD,TX,DE,WY,KY,IL,OR,MN,DC,NV,VT,MI,IA,RI,PA,AR,HI,ID,OK,AK,MS,MT,WV}
@attribute 'Home Ownership' {OWN,MORTGAGE,RENT,NONE,OTHER}
@attribute 'Monthly Income' numeric
@attribute 'FICO Range' string 
@attribute 'Earliest CREDIT Line' date yyyy-MM-dd
@attribute 'Open CREDIT Lines' numeric
@attribute 'Total CREDIT Lines' numeric
@attribute 'Revolving CREDIT Balance' string
@attribute 'Revolving Line Utilization' string
@attribute 'Inquiries in the Last 6 Months' numeric
@attribute 'Accounts Now Delinquent' numeric
@attribute 'Delinquent Amount' numeric
@attribute 'Delinquencies (Last 2 yrs)' numeric
@attribute 'Months Since Last Delinquency' string
@attribute 'Public Records On File' numeric
@attribute 'Months Since Last Record' string
@attribute Education string
@attribute 'Employment Length' string
@attribute Code string
@attribute 'Initial Listing Status' {F}

@data
 
"""

# {660-664,810-814,740-744,690-694,760-764,755-759,785-789,670-674,705-709,715-719,775-779,750-754,675-679,700-704,795-799,770-774,720-724,710-714,'',745-749,680-684,780-784,790-794,665-669,685-689,735-739,800-804,765-769,725-729,695-699,730-734,820-824,805-809,815-819}
# """ + \ # {< 1 year,1 year,2 years,3 years,4 years,5 years,6 years,7 years,8 years,9 years,10+ years} 

def parseCsv(inputCsv, outputCsv):
    csvWriter = csv.writer(outputCsv, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, doublequote=False, escapechar='\\')
    with open(inputCsv) as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',', quotechar='"')
        for row in csvReader:
            if len(row) != NB_COLUMN:
                continue
            # remove "s
            row = map(lambda s:string.replace(s, '"', ' '), row)
            csvWriter.writerow(row)


M_STATUS = re.compile("(Fully Paid|Charged Off)")

def createArff(inputCsv, output):
    output.write(HEADER)
    cpt = 0
    for line in fileinput.input(inputCsv):
        if cpt == 0:
            # skip header line
            cpt += 1
            continue
        line = line.strip("\r\n")
        tab = line.split(",")
        print tab[13]
        if not M_STATUS.match(tab[13]):
            continue
        line = ",".join(tab)
        output.write(line+"\n")

def main(inputCsv, outputCsv):
    #parseCsv(inputCsv, outputCsv)
    createArff(inputCsv, outputCsv)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cleans an input csv file, and outputs the new csv (to stdout by default).")
    parser.add_argument("input", help="the input csv")
    parser.add_argument("-o", "--output", help="the output csv")
    args = parser.parse_args()

    out = sys.stdout
    if args.output:
        out = open(args.output, "w")

    main(args.input, out)

    if args.output:
        out.close()
