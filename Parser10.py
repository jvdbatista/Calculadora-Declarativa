from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree

def buildParseTree(fplist, pStack, currentTree):
    if (len(fplist) == 0):
        return 0

    if fplist[0][0] == 'token parenEq':
        currentTree.insertLeft('')
        pStack.push(currentTree)
        currentTree = currentTree.getLeftChild()
        fplist.pop(0)
        buildParseTree(fplist, pStack, currentTree)

    elif fplist[0][0] == 'token num':
        currentTree.setRootVal(float(fplist[0][1]))
        parent = pStack.pop()
        currentTree = parent
        fplist.pop(0)
        buildParseTree(fplist, pStack, currentTree)

    elif fplist[0][0] == 'token string':
        currentTree.setRootVal(str(fplist[0][1]))
        parent = pStack.pop()
        currentTree = parent
        fplist.pop(0)
        buildParseTree(fplist, pStack, currentTree)

    elif fplist[0][0] == 'token oper':
        # print('Aqui +')
        currentTree.setRootVal(fplist[0][1])
        currentTree.insertRight('')
        pStack.push(currentTree)
        currentTree = currentTree.getRightChild()
        fplist.pop(0)
        buildParseTree(fplist, pStack, currentTree)

    elif fplist[0][0] == 'token parenDir':
        currentTree = pStack.pop()
        fplist.pop(0)
        buildParseTree(fplist, pStack, currentTree)

    else:
        buildParseTree(fplist, pStack, currentTree)
