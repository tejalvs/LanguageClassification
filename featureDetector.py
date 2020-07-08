import re
vowels=['a','e','i','o','u']

commonDutchWords = ['niet','wat','ze', 'zijn', 'maar', 'die', 'heb','voor', 'ben','mijn','dit','hem','hebben','heeft','nu', 'allemaal',    'gedaan',    'huis',    'zij',    'jaar',    'vader',
                    'doet',    'vrouw',    'geld',    'hun',    'anders','zitten',    'niemand',    'binnen','spijt',    'maak',    'staat',    'werk',    'moeder',    'gezien',    'waren',
                    'wilde','praten',    'genoeg',    'meneer',    'klaar',    'ziet',    'elkaar',    'uur',    'zegt',    'helpen',    'helemaal','graag',    'krijgen',    'werd',    'zonder',
                    'nodig',    'twee',    'tegen',    'maken', 'wordt',    'mag',    'altijd',    'wacht',    'geef',    'dag',    'zeker',  'naam',    'vriend',    'beetje',    'jongen',
                    'snel',    'geven',    'achter', 'wanneer',    'kinderen',    'onder','hoe', 'kom',    'gaan',    'bent',    'haar',    'doen',  'daar',    'al',    'ons',    'gaat',
                    'hebt',    'waarom',    'deze',    'laat', 'moeten',    'wie',    'alles', 'kunnen',    'nooit',    'komt',    'misschien',    'iemand',    'veel',    'worden',    'onze',
                    'leven',    'weer', ]

commonEnglishWords=['the','be','to','of','and','from','in','that','have','so','it','for','not','on','with','he','as','you','do','at','this','but']

dutchDiaphthong=['oe','eu','ei','ij','ui','uw','ou','aai','eeuw','ooi','oei','ieuw']

articlesEng=['a','an','the']

articlesDutch=['een', 'de', 'het', 'groene', 'groen', 'hij', 'zij', 'haar', 'hem', 'zijn', 'dit', 'deze', 'die', 'dat', 'wie', 'wat']

def checkIJPattern(token):
    for alpha in token:
        alpha = alpha.lower()
        if 'ij' in alpha:
            return 1
    return 0


def checkCommonDutchWords(token):
    for alpha in token:
        if alpha.lower() in commonDutchWords:
            return 1
    return 0

def checkCommonEnglishWords(token):
    for alpha in token:
        if alpha.lower() in commonEnglishWords:
            return 0
    return 1

def checkDutchDiaphthong(token):
    for alpha in token:
        for dh in dutchDiaphthong:
            if dh in alpha.lower():
                return 1
    return 0


def checkRepeatedVowels(token):
    repeatedVowel=['aa','ee','ii','oo','uu']

    for alpha in repeatedVowel:
        for beta in token:
            if alpha.lower() in beta.lower():
                return 1
    return 0


def checkCharOtherThanEnglish(token):
    for alpha in token:
        if not re.match("^[a-zA-Z0-9_-]*$", alpha):
            return 1
    return 0

def checkIfStartsWithD(token):
    for alpha in token:
        if alpha[0][0].lower() == 'd':
            return 1
    return 0

def checkDutchArticles(token):
    for alpha in token:
        if alpha.lower() in articlesDutch:
            return 1
    return 0

def checkEnglishArticles(token):
    for alpha in token:
        if alpha.lower() in articlesEng:
            return 0
    return 1

def checkAvgWordLength(token):
    sum=0;
    length= len(token)
    for alpha in token:
        sum=sum+len(alpha)
    avg=sum/length
    if avg>7.0:
        return 1
    return 0

def prepareFeatureChart(statement):
    featureChart= [checkAvgWordLength(statement.split(' ')), checkEnglishArticles(statement.split(' ')),
                   checkDutchArticles(statement.split(' ')), checkIfStartsWithD(statement.split(' ')),
                   checkCharOtherThanEnglish(statement.split(' ')), checkRepeatedVowels(statement.split(' ')),
                   checkDutchDiaphthong(statement.split(' ')), checkCommonEnglishWords(statement.split(' ')),
                   checkCommonDutchWords(statement.split(' ')), checkIJPattern(statement.split(' '))]
    #print(featureChart)
    return featureChart

#prepareFeatureChart("aankoop van allerlei vervoerbewijzen kan men bij voorkeur terecht aan de biljettenautomaat die ter beschikking ")