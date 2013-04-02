
import math
from sklearn import svm
from sklearn import cross_validation
import preprocessData as ppd


MODEL_DIR="./model/"

def trainSVM(trainData):
    svc = svm.SVC(kernel='linear')
    k_fold = cross_validation.StratifiedKFold(trainData["target"], n_folds=3)
    scores = []
    
    for train, test in k_fold:
        print "Iteration %d" % len(scores)
        svc.fit(trainData["data"][train], trainData["target"][train])
        score = svc.score(trainData["data"][test], trainData["target"][test])
        scores.append(score)
        print score
        
    avg = round(math.fsum(scores) / float(len(scores)), 4)
    #print scores
    print "Avg score: %.4f" % avg

def main():
    trainData = ppd.preprocessData(ppd.trainDataSmall)
    trainSVM(trainData)

if __name__ == "__main__":
    main()
