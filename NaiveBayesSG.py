data = [
    {"outlook":"sunny", "temp":"hot", "humidity":"high", "wind":"weak", "class":"no" },
    {"outlook":"sunny", "temp":"hot", "humidity":"high", "wind":"strong", "class":"no" },
    {"outlook":"overcast", "temp":"hot", "humidity":"high", "wind":"weak", "class":"yes" },
    {"outlook":"rain", "temp":"mild", "humidity":"high", "wind":"weak", "class":"yes" },
    {"outlook":"rain", "temp":"cool", "humidity":"normal", "wind":"weak", "class":"yes" },
    {"outlook":"rain", "temp":"cool", "humidity":"normal", "wind":"strong", "class":"no" },
    {"outlook":"overcast", "temp":"cool", "humidity":"normal", "wind":"strong", "class":"yes" },
    {"outlook":"sunny", "temp":"mild", "humidity":"high", "wind":"weak", "class":"no" },
    {"outlook":"sunny", "temp":"cool", "humidity":"normal", "wind":"weak", "class":"yes" },
    {"outlook":"rain", "temp":"mild", "humidity":"normal", "wind":"weak", "class":"yes" },
    {"outlook":"sunny", "temp":"mild", "humidity":"normal", "wind":"strong", "class":"yes" },
    {"outlook":"overcast", "temp":"mild", "humidity":"high", "wind":"strong", "class":"yes" },
    {"outlook":"overcast", "temp":"hot", "humidity":"normal", "wind":"weak", "class":"yes" },
    {"outlook":"rain", "temp":"mild", "humidity":"high", "wind":"strong", "class":"no" }
]

test = {"outlook":"rain", "temp":"mild", "humidity":"high", "wind":"strong"}

def Prior(data,clsValue, clsName="class"):
    count = 0.0
    for i in data:
        if i[clsName] == clsValue:
            count+=1

    return count/len(data)

def ConditionalProb(data, clsValue,xName, xValue,clsName="class"):
    count1 = 0.0
    count2 = 0.0
    for i in data :
        if i[clsName] == clsValue:
            count1+=1
            if i[xName] == xValue:
                count2+=1

    return count2/count1

pYes = []
pNo = []
def Likelihood(data, clsYes, clsNo, test):
    for key,val in test.items():
        ProbYes = ConditionalProb(data, clsYes, key, val)
        ProbNo= ConditionalProb(data, clsNo, key, val)
        #print
        pYes.append(ProbYes)
        pNo.append(ProbNo)

    return {clsYes:ProbYes,clsNo:ProbNo}

Likelihood(data,"yes","no",test)

def Posterior(prob):
    total = 1
    for x in prob :
        total *= x
    return total

PriorYes = Prior(data,"yes")
PriorNo = Prior(data, "no")
PlayYes = Posterior(pYes) * PriorYes
PlayNo = Posterior(pNo) * PriorNo

print PlayYes
print PlayNo

if PlayYes < PlayNo :
    print "Kita maen"
else:
    print "Kita ga maen"
