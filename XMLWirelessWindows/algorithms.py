import string
#replaces
def replaces(strg, listRe, **listNew):
    if len(listRe) != len(listNew):
        raise ValueError("Value input incorret")
    for i in range(len(listRe)):
        re = strg.replace(listRe[i], listNew[listRe[i].replace("{", "").replace("}", '')])
    return re

















