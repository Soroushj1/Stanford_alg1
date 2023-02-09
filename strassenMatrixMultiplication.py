
matrixA = [[1,2], [3,4]]
matrixC=[[2,0],[1,2]]
matrixB = [[1,3,4,5,5,6,6,7],[1,3,4,5,5,6,6,8],[1,3,4,5,5,6,6,9],[1,3,4,5,5,6,6,10],[1,3,4,5,5,6,6,11],[1,3,4,5,5,6,6,12],[1,3,4,5,5,6,6,13],[1,3,4,5,5,6,6,14]]

    
def matrixAddition(matrix_a, matrix_b):
    newMatrix = []
    finalMatrix = []
    for i in range(len(matrix_a)):
        for j in range(len(matrix_a[i])):
            newMatrix.append(matrix_a[i][j]+ matrix_b[i][j])
        finalMatrix.append(newMatrix)
        newMatrix = []
    return finalMatrix
    
def matrixSubtraction(matrix_a, matrix_b):
    newMatrix = []
    finalMatrix= []
    for i in range(len(matrix_a)):
        for j in range(len(matrix_a)):
            newMatrix.append(matrix_a[i][j]- matrix_b[i][j])
        finalMatrix.append(newMatrix)
        newMatrix = []
    return finalMatrix

def splitter(a):
    if len(a) == 2 and len(a[0])==2: 
        return a
    # lots of code version of the implementation!
    #newMatrix = []
    #matrixOutput = []
    #half = len(a)//2
    #for i in range(half):
    #    quarter = len(a[i])//2
    #    for j in range(len(a[i])//2):
    #        newMatrix.append(a[i][j])
    #    matrixOutput.append(newMatrix)
    #    newMatrix = []
    #return matrixOutput
    topLeft = [[a[i][j] for j in range(len(a)//2)] for i in range(len(a)//2)]
    botLeft = [[a[i][j] for j in range(len(a)//2 )] for i in range(len(a)//2, len(a))]
    topRight = [[a[i][j] for j in range(len(a)//2, len(a))] for i in range(len(a)//2)]
    botRight = [[a[i][j] for j in range(len(a)//2, len(a))] for i in range(len(a)//2, len(a))]
    return topLeft, topRight, botLeft, botRight


def defaultMultiplier(a,b):
    return  [[a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
                         [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]]]
    
    
    

def strassen(a,b):
    
    if len(a) % 2 != 0  and len(a[0]) % 2 != 0:
        raise Exception('matrices are not the right size')
    # base case is if its 2x2 then multiply 
    if len(a)==2 and len(a[0])==2:
       return defaultMultiplier(a,b)
    
    A,B,C,D = splitter(a)
    E,F,G,H = splitter(b)
    P1 =  strassen(A, matrixSubtraction(F,H))
    P2 = strassen(matrixAddition(A,B),H)
    P3 = strassen(matrixAddition(C,D),E)
    P4 = strassen(D,matrixSubtraction(G,E))
    P5 = strassen(matrixAddition(A,D),matrixAddition(E,H))
    P6 = strassen(matrixSubtraction(B,D),matrixAddition(G,H))
    P7 = strassen(matrixSubtraction(A,C),matrixAddition(E,F))
    tl = matrixSubtraction(matrixAddition(P5,matrixAddition(P4,P6)),P2)
    tr = matrixAddition(P1,P2)
    bl=matrixAddition(P3,P4)
    br=matrixSubtraction(matrixAddition(P1,P5),matrixAddition(P3,P7))
    
    newMatrix = []
    for i in range(len(tr)):
        newMatrix.append(tl[i]+tr[i])
    for i in range(len(br)):
        newMatrix.append(bl[i]+br[i])
        
        
        
    return newMatrix
        
    
            
    
print(strassen(matrixB,matrixB))

    