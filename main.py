import re
from Tokenizer10 import *
from Parser10 import *
from Evaluete10 import *



eq = ''
eq = re.sub('^A-Za-z0-9.',"", eq)


def main(mod):

    if mod == '1':

        eq = input('equacao')
        if eq == '':
            exit(0)
        eq = re.sub('^A-Za-z0-9.', "", eq)

        pStack = Stack()
        eTree = BinaryTree('')
        pStack.push(eTree)
        currentTree = eTree

        x = Tokenizador(eq)
        olhaASSI = mapeando(x)
        if olhaASSI == True:
            zetASSI = removeANTESdoASSIGN(x, StrASSI='')

        lista3 = x.copy()

        pt = buildParseTree(lista3, pStack, currentTree)
        pt = eTree
        pt.postorder()

        u = evaluate(pt)

        print('Resultado ', u)

        if olhaASSI == True:
            if zetASSI in D:
                D[zetASSI] = u
            else:
                D.setdefault(zetASSI, u)
            zetASSI = ''

        listaFin2.clear()
        listaFin.clear()
        lista3.clear()
        main(mod)

    if mod == '2':
        eq = input('equacao')

        if eq == '':
            exit(0)

        eq = re.sub('^A-Za-z0-9.', "", eq)

        pStack = Stack()
        eTree = BinaryTree('')
        pStack.push(eTree)
        currentTree = eTree

        x = Tokenizador(eq)

        olhaASSI = mapeando(x)
        if olhaASSI == True:
            zetASSI = removeANTESdoASSIGN(x, StrASSI='')
        lista3 = x.copy()
        contadorNUMS = conta_ocorrencias(lista3)
        contadorNUMS -= 1
        zet = ColocaParenteses(lista3, contadorNUMS, contadorNUMS)

        pt = buildParseTree(zet, pStack, currentTree)
        pt = eTree
        pt.postorder()
        u = evaluate(pt)

        print('Resultado ', u)
        if olhaASSI == True:
            if zetASSI in D:
                D[zetASSI] = u
            else:
                D.setdefault(zetASSI, u)
        zetASSI = ''
        listaFin2.clear()
        listaFin.clear()
        lista3.clear()
        main(mod)

mod = input('Escolha o modulo')
main(mod)