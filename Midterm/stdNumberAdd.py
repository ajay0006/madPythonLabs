def getStdNumb():
    studNumb = input("Please enter your student Number")
    return studNumb


def convertStdNumb(stdNumb):
    listStdNumb = list(stdNumb)
    return listStdNumb


def loopAddStudNumb(dj):
    j = 0
    studNumbList = []
    print(len(dj), 'length of lists')
    for i in range(0, len(dj)):
        j += 1
        numbers = int(dj[j - 1])
        studNumbList.append(numbers)
        print(studNumbList)
    return studNumbList


def addstdnumber(dj1):
    print(sum(dj1))


a = getStdNumb()
b = convertStdNumb(a)
c = loopAddStudNumb(b)
addstdnumber(c)
