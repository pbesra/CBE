from sympy import Matrix
class cbe:
    def getCoefficient(self, List):
        A = dict()
        B = []
        for compound in List:
            elements = list(compound)
            l = ''
            for e in range(len(elements)):
                num = 1
                if (elements[e].isupper()):
                    l = elements[e]
                    j = e + 1
                    if (j == len(elements)):
                        A[l] = 1
                    while (j < len(elements)):
                        if (elements[j].islower()):
                            l += elements[j]
                        elif (elements[j].isupper()):
                            num = 1
                            A[l] = num
                            l = ''
                            break
                        elif (elements[j].isnumeric()):
                            num = elements[j]
                            A[l] = num
                            l = ''
                            break
                        j += 1
            B.append(A)
            A = {}
        return (B)

    def numEquations(self, left):
        unique_elements = set()
        for elements in left:
            for e in elements:
                unique_elements.add(e)
        return ([unique_elements, len(unique_elements)])

    def equation(self, left, right, n):
        eList, m = self.numEquations(left)
        eList = list(eList)
        A = []
        B = []
        for x in eList:
            l = []
            for u in left:

                found = 0
                for t in u:
                    if (t == x):
                        found = 1
                        l.append(int(u[t]))
                        break
                if (found == 1):
                    continue
                else:
                    l.append(0)

            A.append(l)
        for x in eList:
            l = []
            for u in right:

                found = 0
                for t in u:
                    if (t == x):
                        found = 1
                        l.append(-int(u[t]))
                        break
                if (found == 1):
                    continue
                else:
                    l.append(0)

            B.append(l)
        C = []
        for i in range(len(A)):
            C.append(A[i] + B[i])
        return ([C, len(eList)])

    def getBalancedEquation(self, lhsList, rhsList, nullspace):
        left_eqn = ''

        for i in range(len(lhsList)):
            if (i is len(lhsList) - 1):
                left_eqn += str(nullspace[i]) + lhsList[i]
            else:
                left_eqn += str(nullspace[i]) + lhsList[i] + '+'

        right_eqn = ''
        for i in range(len(rhsList)):
            if (i is len(rhsList) - 1):
                right_eqn += str(nullspace[m + i]) + rhsList[i]
            else:
                right_eqn += str(nullspace[m + i]) + rhsList[i] + '+'

        balanced = left_eqn + '-->' + right_eqn
        return (balanced)

lhs = 'NaOH+H2SO4'
rhs = 'Na2SO4+H2O'
lhsList = lhs.split('+')
rhsList = rhs.split('+')
molecules = lhsList + rhsList
m = len(lhsList)

chemical=cbe()
B = chemical.getCoefficient(lhsList)
C = chemical.getCoefficient(rhsList)

A, n =chemical.equation(B, C, len(B) + len(C))
nullspace = Matrix(A).nullspace()[0].tolist()

ans =chemical.getBalancedEquation(lhsList, rhsList, nullspace)
print(ans)
