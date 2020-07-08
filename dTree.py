import Node
trainingset=[]
file = open("dataset.csv")
header=file.readline().replace("\n","").split(",")
for row in file:
    row = row.replace("\n","")
    trainingset.append(row.split(","))


def createDecisionTree(featureSet,parentSet):
    if(len(featureSet)==1):
        countDutch=0
        countEnglish=0
        for alpha in parentSet:
            if alpha[len(alpha)-1]=='en':
                countEnglish+=countEnglish
            if alpha[len(alpha)-1]=='nl':
                countDutch+=countDutch
            if countDutch > countEnglish:
                return Node("nl")
            if countEnglish>countDutch:
                return Node("en")
    if(len(featureSet)==2):
        countDutch=0
        countEnglish=0
        for alpha in featureSet:
            if alpha[len(alpha) - 1] == 'en':
                countEnglish += countEnglish
            if alpha[len(alpha) - 1] == 'nl':
                countDutch += countDutch
        if countDutch > countEnglish:
            return Node("nl")
        if countEnglish>countDutch:
            return Node("en")
    else:













