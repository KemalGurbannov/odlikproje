from  math import sqrt

def euclideanDistance(point1 , point2):
    firstValue = (point1[1] - point2[1]) ** 2
    secondValue = (point1[0] - point2[0]) ** 2
    return  sqrt(firstValue + secondValue) 


points = [(2, 3), (1, 7), (1, 1), (4, 6)]
distances = []
i = 1
flag = 1

for i in range(len(points)):
    for j in range(i+1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

print("Noktalar arasındaki minimum Öklid mesafesi:", min(distances))