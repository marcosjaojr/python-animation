from PolygonFace import Face
import numpy as np

VERTICES = [
    [-1, -1, 0],
    [-1, 0, 0],
    [0, 0, 0],
    [0, 1, 0],
    [1, 2, 0],
    [1, 3, 0],
    [2, 3, 0],
    [2, 2, 0],
    [3, 1, 0],
    [3, 0, 0],
    [4, 0, 0],
    [4, -1, 0],
    [3, -1, 0],
    [2, -2, 0],
    [2, -3, 0],
    [1, -3, 0],
    [1, -2, 0],
    [0, -1, 0],
    [-1, -1, 4],
    [-1, 0, 4],
    [0, 0, 4],
    [0, 1, 4],
    [1, 2, 4],
    [1, 3, 4],
    [2, 3, 4],
    [2, 2, 4],
    [3, 1, 4],
    [3, 0, 4],
    [4, 0, 4],
    [4, -1, 4],
    [3, -1, 4],
    [2, -2, 4],
    [2, -3, 4],
    [1, -3, 4],
    [1, -2, 4],
    [0, -1, 4]
]

RAW_FACES = [
    ([1, 19, 20, 2], '#00BCD4'),
    ([2, 20, 21, 3], '#263238'),
    ([3, 21, 22, 4], '#ff8a80'),
    ([4, 22, 23, 5], '#827717'),
    ([5, 23, 24, 6], '#8D6E63'),
    ([6, 24, 25, 7], '#64DD17'),
    ([7, 25, 26, 8], '#C5CAE9'),
    ([8, 26, 27, 9], '#FF6D00'),
    ([9, 27, 28, 10], '#BCAAA4'),
    ([10, 28, 29, 11], '#4527A0'),
    ([11, 29, 30, 12], '#304FFE'),
    ([12, 30, 31, 13], '#795548'),
    ([13, 31, 32, 14], '#03A9F4'),
    ([14, 32, 33, 15], '#8BC34A'),
    ([15, 33, 34, 16], '#90A4AE'),
    ([16, 34, 35, 17], '#00796B'),
    ([17, 35, 36, 18], '#BBDEFB'),
    ([18, 36, 19, 1], '#9E9E9E'),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], '#66BB6A'),
    ([36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19], '#3F51B5')
]

# x -> -45, y -> 60
MISO = np.matrix([
    [0.5, -0.612, 0, 0],
    [0, 0.707, 0, 0],
    [0.866, 0.353, 0, 0],
    [0, 0, 0, 1]
])

# angulo 75graus
MOBL = np.matrix([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [(1.0/2.0)*np.cos(np.radians(75)), (1.0/2.0)*np.sin(np.radians(75)), 0, 0],
    [0, 0, 0, 1]
])

MPER = np.matrix([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, -(1.0/250.0)],
    [0, 0, 0, 1]
])

class Polygon:

    def __init__(self):
        self.vertices = VERTICES
        self._update_faces()
    
    def iso_proj(self):
        homogeined = [[item[0], item[1], item[2], 1] for item in self.vertices]
        self.vertices = (np.matrix(homogeined)*MISO).tolist()
        self._update_faces()

    def obliq_proj(self):
        homogeined = [[item[0], item[1], item[2], 1] for item in self.vertices]
        self.vertices = (np.matrix(homogeined)*MOBL).tolist()
        self._update_faces()

    def pers_proj(self):
        homogeined = [[item[0], item[1], item[2], 1] for item in self.vertices]
        self.vertices = (np.matrix(homogeined)*MPER).tolist()
        self._update_faces()

    def _update_faces(self):
        self.faces = [Face([self.vertices[i-1]
            for i in face[0]], face[1]) for face in RAW_FACES]
