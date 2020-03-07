import math
from math import floor,ceil,log10
def intToWord(num):
    num=num
    triplets=[]
    tripletNames=["thousand","million","billion","trillion"]
    if num==0:
        return "zero"
    if num==1:
        return "one"
    for i in range(0,ceil(log10(num)),3):
        #triplets.append()
        if i!=0:
            triplets.append(floor((num*10**(-i))%10**(i)))
        else:
            triplets.append(num%1000)
    triplets.reverse()
    output=""
    for i in range(len(triplets)):
        tripletToUse=len(triplets)-i-2
        #print(tripletToUse)
        output+=(tripleDigitToWord(triplets[i]))
        if tripletToUse!=-1:
            output+=" {}".format(tripletNames[tripletToUse])
        if i!=len(triplets)-1:
            output+=", "
    
    #print(output)
    #print(triplets)
    return output
def tripleDigitToWord(num=123):
    #single="zero one two three four five six seven eight nine".split()
    single=['','one','two','three','four','five','six','seven','eight','nine']
    double=["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
    teens=["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"] #Numbers 10-19 (Not strictly numbers ending in -teen)
    output=""
    if num==0:
        return "zero"
    if num>=100:
        output+="{} hundred".format(single[floor(num/100)])
    doubleNum=num%100
    if num>100 and doubleNum>0:
        output+=" and "
    if doubleNum<10:
        output+=single[doubleNum]
    elif doubleNum<20:
        output+=teens[doubleNum%10]
    else:
        singleNum=num%10
        if singleNum==0:
            output+=double[floor(doubleNum/10)]
        else:
            output+="{}-{}".format(double[floor(doubleNum/10)],single[singleNum])
    return output
def main():
    
    doc=open("everyNumToOneMillion.txt","w")
    for i in range(0,1000000,1):
        #doc.append(intToWord(i)+"\n")
        doc.write(intToWord(i)+"\n")
        print(i)
    doc.close()
    print("Done!")
main()
