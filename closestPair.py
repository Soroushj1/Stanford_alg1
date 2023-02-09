import math

points = [(9128, 9),
(6251, 5),
(7220, 5),
(5061, 6),
(1786, 8),
(6438, 6),
(1, 8),
(3790, 6),
(6247, 6),
(7608, 8)]
#sorted points in terms of x are placed in a new array sortedPoints
def Px(points):
    if len(points) == 1:
        return points
    mid = len(points)//2
    left = points[:mid]
    right = points[mid:]
    sortedLeft = Px(left)
    sortedRight = Px(right)
    i = j = 0
    sortedPoints = []
    while i<len(sortedLeft) and j < len(sortedRight):
        if sortedLeft[i][0] < sortedRight[j][0]:
            sortedPoints.append(sortedLeft[i])
            i +=1 
        else:
            sortedPoints.append(sortedRight[j])
            j +=1 
    while i<len(sortedLeft):
        sortedPoints.append(sortedLeft[i])
        i +=1
    while j<len(sortedRight):
        sortedPoints.append(sortedRight[j])
        j+=1
    return sortedPoints

print(Px(points))

            

#sorted points in terms of y are placed in a new array sortedPoints
def Py(points):
    if len(points) == 1:
        return points
    mid = len(points)//2
    left = points[:mid]
    right = points[mid:]
    Py(left)
    Py(right)
    i = j = k=0
    while i<len(left) and j < len(right):
        if left[i][1] < right[j][1]:
            points[k] = left[i]
            i +=1 
        else:
            points[k] = right[j]
            j +=1 
        k+=1
    while i<len(left):
        points[k] = left[i]
        i +=1
        k+=1
    while j<len(right):
        points[k] = right[j]
        j+=1
        k+=1
    return points

print(Py(points))

def closestPair(Px, Py):
    
    if len(Px) < 4: 
        return defaultCalc(Px)
    
    Qx = Px[:(len(Px)//2)]
    Rx = Px[(len(Px)//2):]
    Ry, Qy = [],[]
    
    for point in Py:
        if point[0] <= Qx[-1][0]:
            Qy.append(point)
        else:
            Ry.append(point)
            
    
    dist1, (p1, q1) = closestPair(Qx,Qy)
    dist2, (p2,q2) = closestPair(Rx,Ry)
    delta = min(dist1,dist2)
    #delta = min(defaultCalc([p1,q1])[0], defaultCalc([p2,q2])[0])
    dist3, (p3, q3) = splitPair(Px,Py, delta)
    if dist3<delta: 
        return dist3, (p3,q3)
    elif dist1<dist2:
        return dist1, (p1, q1)
    else:
        return dist2, (p2,q2)
        

def splitPair(Px,Py,delta):
    
    xbar = Px[len(Px)//2][0]
    Sy=[]
    for i in range(len(Py)):
        if xbar-delta< Py[i][0] < xbar+delta:
            Sy.append(Py[i])
    
    best = delta
    best_pair = None
    for i in range(len(Sy)-1):
        for j in range(1, min(7, len(Sy)-i)):
            distance =defaultCalc([Sy[i],Sy[i+j]])[0] 
            if distance< best:
                best = distance
                best_pair=(Sy[i],Sy[i+j])
                
    return best, best_pair if best_pair!= None else (None, None)
    
    
        
def defaultCalc(Px):
    min = math.sqrt((Px[0][0]- Px[1][0])**2 + (Px[0][1]- Px[1][1])**2)
    a, b = 0, 1
    for i in range(len(Px)-1):
        for j in range(i+1, len(Px)):
            d = math.sqrt((Px[i][0]- Px[j][0])**2 + (Px[i][1]- Px[j][1])**2)
            if d < min: 
                min = d
                a, b = i, j
    return min, (Px[a],Px[b])
            

pointsX = Px(points)
pointsY= Py(points)

print(closestPair(pointsX,pointsY))


