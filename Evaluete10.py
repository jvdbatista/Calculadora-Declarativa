import operator

D = {}



def evaluate(parseTree):
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv,'^':operator.pow,'%':operator.mod}
    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()
    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC), evaluate(rightC))
    else:
        zeta = parseTree.getRootVal()
        if type(zeta) == type('a'):
            if zeta in D:
                alpha = D[zeta]
            else:
                alpha = 1
        else:
            alpha = zeta
        return alpha