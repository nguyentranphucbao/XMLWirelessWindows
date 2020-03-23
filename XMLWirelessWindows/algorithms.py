import string
#replaces
def replaces(strg, listRe, **listNew):
    re = strg
    for i in range(len(listRe)):
        re = re.replace(listRe[i], listNew[listRe[i].replace("{", "").replace("}", '')])
    return re
















