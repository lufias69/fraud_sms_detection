def tokenisasi(kalimat, delimiter = [" ", ".",",",'?','!','@','#','%','^','*','(',')','<','>',
                                    '/','\\','[',']','{','}',':',"&"],  space = True):
    if space == True:
        delimiter = list(set([" "]+delimiter))
    else:
        delimiter = list(set(delimiter))
    token = list()
    temp = list()
    tem_delimiter = list()
    for i in kalimat:
        if i not in delimiter:
            temp.append(i)
        else:
            tem_delimiter.append(i)
            if len(temp)>1:
                token.append("".join(temp))
            if ' ' != i:
                token.append("".join(tem_delimiter))
            tem_delimiter = list()
            temp = list()
    if len(temp)>1:
        token.append("".join(temp))
    return token

print(tokenisasi("makan nasi, kepiting, tluer.fdf", space = False))