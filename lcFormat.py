
import sys, string, re

# nb of columns/features per record
NB_COL=42

# "employment length","code","initial listing status"] "fico range" "loan id" 
fields = ["loan id","amount requested","amount funded by investors","interest rate","loan length","application date","application expiration date","issued date","credit grade","loan title","loan purpose","loan description","monthly payment","status","total amount funded","debt-to-income ratio","remaining principal funded by investors","payments to date (funded by investors)","remaining principal","payments to date","screen name","city","state","home ownership","monthly income","fico range","earliest credit line","open credit lines","total credit lines","revolving credit balance","revolving line utilization","inquiries in the last 6 months","accounts now delinquent","delinquent amount","delinquencies (last 2 yrs)","months since last delinquency","public records on file","months since last record","education","employment length","code","initial listing status"]

f2id = dict(zip(fields, xrange(NB_COL)))
id2f = dict(zip(xrange(NB_COL), fields))

field_class = "status"

fields_num = ["amount requested","amount funded by investors","monthly payment","total amount funded","remaining principal funded by investors","payments to date (funded by investors)","remaining principal","payments to date","monthly income","open credit lines","total credit lines","revolving credit balance","inquiries in the last 6 months","accounts now delinquent","delinquent amount","delinquencies (last 2 yrs)","months since last delinquency","public records on file","months since last record"]

fields_pc = ["interest rate","debt-to-income ratio","revolving line utilization"]

fields_date = ["application date","application expiration date","issued date","earliest credit line"]

fields_str = ["loan title", "loan description", "screen name", "city", "education"]

fields_categorial = ["loan length","credit grade","loan purpose","state","home ownership"] 

targets = ["fully paid", "charged off", 'default', 'issued', 'current', 'performing payment plan', 'late (16-30 days)', 'late (31-120 days)', 'in review', 'in grace period', 'loan is being issued']

class lcRecord(dict):
    def __str__(self):
        ids = sorted(self.keys())
        lStr = map(lambda id: str((id2f[id], self[id])),  ids)
        return " ".join(lStr)

class lcRow2Rec():
    def __init__(self):
        self.patPolicy = re.compile("^does not meet the current credit policy  status: ")

    def row2Rec(self, row):
        assert len(row)==NB_COL, "len(row)="+str(len(row))+" / NB_COL="+str(NB_COL)
        # converts text in all fields to lower
        row = map(string.lower, row)
        # create record by mapping field ids with their value
        lcRec = lcRecord(dict(zip(xrange(NB_COL), row)))

        # assign class to record
        i = f2id["status"]
        v = lcRec[i].strip()
        match = self.patPolicy.match(v)
        if match:
            lcRec.oldPolicy = True
            v = v[match.end():]
        lcRec.target = v #targets.index(v)
        
        del lcRec[i]

        for f in fields_num:
            try:
                i = f2id[f]
                v = lcRec[i]
                if len(v) == 0:
                    # empty num field
                    del lcRec[i]
                else:
                    lcRec[i] = float(v)
            except ValueError as e:
                print type(e), e
                print "Field: %s, id: %d, lcRec[%d]: %s" % (f, i, i, lcRec[i])
                print lcRec
                sys.exit()

        for f in fields_pc:
            i = f2id[f]
            v = lcRec[i]
            if len(v) == 0:
                del lcRec[i]
            else:
                if v[-1] == "%":
                    v = v[:-1]
                lcRec[i] = round(float(v)/100, 4)

        for f in fields_date:
            i = f2id[f]
            del lcRec[i]

        for f in fields_str:
            i = f2id[f]
            del lcRec[i]

        for f in ["employment length","code","initial listing status", "fico range", "loan id"]:
            i = f2id[f]
            del lcRec[i]
        #print lcRec
        return lcRec
