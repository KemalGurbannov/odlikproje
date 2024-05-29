# -*- coding: utf-8 -*-
from ursina import *


def euclideanDistance(point1, point2):
    firstValue = (point1[1] - point2[1]) ** 2
    secondValue = (point1[0] - point2[0]) ** 2
    return sqrt(firstValue + secondValue)


entities = {}


def visualization(point1, point2):
    vec1, vec2 = Vec3(*point1), Vec3(*point2)
    _distance = euclideanDistance(point1, point2)
    ortalam_koordinat = (vec1 + vec2) / 2
    line = Entity(model=Mesh(vertices=[point1, point2], mode="line", thickness=10))
    text = Text(text=str(round(_distance, 2)), position=ortalam_koordinat, scale=15, color=color.white)
    entities[_distance] = (line, text)


def percent(max_, value):
    x = int((value * 255) / max_)
    return x


def coloration(entities_: dict):
    max_distance = max(entities_)
    min_entities = min(entities_.items(), key=lambda e: e[0])
    for key, value in entities_.items():
        value_rgb = percent(max_=max_distance, value=key)
        value[1].color = value[0].color = color.rgb(255, value_rgb, value_rgb, 255)
    return min_entities[1][0]


points = [(2, 3, 0), (1, 7, 0), (1, 1, 0), (4, 6, 0)]
distances = []
i = 1
flag = 1

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        visualization(points[i], points[j])  #
        distances.append(distance)
print("Noktalar arasındaki minimum Öklid mesafesi:", min(distances))
app = Ursina()
# window.fullscreen = True


def show_min_line():
    coloration(entities).blink(duration=1)
    invoke(show_min_line, delay=1)


show_min_line()
EditorCamera()
app.run()
