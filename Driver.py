import sys

import featureDetector as fd


def prepareData(inputfile):
    s=','
    readfile = open(inputfile,encoding="utf8")
    writefile = open("dataset.csv", "w", encoding="utf-8")
    header=['AvgWordLength','EnglishArticles','DutchArticles','StartsWithD','CharOtherThanEnglish','RepeatedVowels','DutchDiaphthong',
            'CommonEnglishWords','CommonDutchWords', 'IJPattern', 'ResultLanguage']
    print(str(header))
    writefile.write(s.join(header)+"\n")
    for line in readfile:
        lineSplit=line.split('|')
        feature=fd.prepareFeatureChart(lineSplit[1])
        feature.append(lineSplit[0])
        featureString = s.join(str(x) for x in feature)
        print(featureString)
        writefile.write(featureString)
        writefile.write("\n")

def main(mode,trainingfile):
    prepareData(trainingfile)




if __name__ == "__main__":
    mode = sys.argv[1]
    trainingFile = sys.argv[2]
    main(mode,trainingFile)

