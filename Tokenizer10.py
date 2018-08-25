
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','.']
oper = ['+', '-', '*', '/','^','%']
parenEq = ['(']
parenDir = [')']
assi = ['=']
stri = ['A','a','B','b','C','c','D','d','E','e','F','f',
        'G','g','H','h','I','i','J','j','K','k','L','l','M','m',
        'N','n','O','o','P','p','Q','q','R','r','S','s','T','t','U','u',
        'V','v','W','w','X','x','Y','y','Z','z']

listaFin = []
listaFin2 = []

def Tokenizador(equa,cont=0):
    if (equa[cont] in oper):
        if (listaFin[-1][0] == 'token oper' or listaFin[-1][0] == 'token parenEq' or listaFin[-1][0] == 'token assign'):
            listaFin.append(('token num', equa[cont]))
        else:
            listaFin.append(('token oper', equa[cont]))
    elif (equa[cont] in stri):
        if cont == 0:
            listaFin.append(('token string', equa[cont]))
        elif (listaFin[-1][0] == 'token string'):
            listaFin.append(('token string', listaFin[-1][1] + equa[cont]))
            listaFin.pop(-2)
        else:
            listaFin.append(('token string', equa[cont]))
    elif (equa[cont] in assi):
        listaFin.append(('token assign', equa[cont]))
    elif (equa[cont] in parenEq):
        listaFin.append(('token parenEq', equa[cont]))
    elif (equa[cont] in parenDir):
        listaFin.append(('token parenDir', equa[cont]))
    elif (equa[cont] in nums):
        try:
            if (equa[cont] in nums):
                if (cont == 0 and equa[cont] in nums):
                    listaFin.append(('token num', equa[cont]))
                elif (equa[cont - 1] in nums or listaFin[-1][0] == 'token num'):
                    listaFin.append(('token num', listaFin[-1][1] + equa[cont]))
                    listaFin.pop(-2)
                elif (listaFin[-1][0] == 'token string'):
                    listaFin.append(('token string', listaFin[-1][1] + equa[cont]))
                    listaFin.pop(-2)
                else:
                    listaFin.append(('token num', equa[cont]))
        except:
            print('Error in the index probably')
    if (len(equa) == cont + 1):
        print(listaFin)
        return listaFin
    cont += 1
    return Tokenizador(equa,cont)


def mapeando(x,aux10=0):
    if (len(x) == aux10 + 1):
        print(listaFin)
        return False
    if x[aux10] == ('token assign', '='):
        return True
    else:
        aux10 += 1
        return mapeando(x,aux10)


def conta_ocorrencias(s):
    ocorrencias = 0
    for c in s:
        if c[0] == 'token num' or c[0] == 'token string':
            ocorrencias = ocorrencias + 1
    return ocorrencias



def removeANTESdoASSIGN(x,StrASSI,contadoNOVO = 0):
    if x[0][0] != 'token assign':
        StrASSI += x[0][1]
    if x[0][0] == 'token assign':
        x.pop(0)
        return StrASSI
    x.pop(0)
    if (len(x) == contadoNOVO + 1):
        return ''
    contadoNOVO += 1
    return removeANTESdoASSIGN(x,StrASSI,contadoNOVO)



# COLOCA PARENTESE NA LISTA J� TOKENIZADA
def ColocaParenteses(t1,ocorre,ocorre2,continha=0):
    if(t1[continha][0] == 'token parenEq' or  t1[continha][0] == 'token parenDir'):
        print('')
    if (t1[continha][0] == 'token oper' or t1[continha][0] == 'token assign'):
        listaFin2.append(t1[continha])
    if (t1[continha][0] == 'token num' or t1[continha][0] == 'token string'):
        #print('AQUIIIIII')
        #print(listaFin2)
        if ocorre > 0:
            listaFin2.append(('token parenEq', '('))
            ocorre -= 1
        listaFin2.append(t1[continha])
    if (len(t1) == continha + 1):
        while ocorre2 > 0:
            listaFin2.append(('token parenDir', ')'))
            ocorre2 -= 1
        return listaFin2
    continha += 1
    return ColocaParenteses(t1,ocorre,ocorre2,continha)

