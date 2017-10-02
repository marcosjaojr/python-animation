#coding: utf-8
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.collections import PolyCollection, LineCollection
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import colors as mcolors
import numpy as np




# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import axes3d

def get_face_from_vertices(vertices):
    vertices.append(vertices[0])
    return {
        'x': [v[0] for v in vertices],
        'y': [v[1] for v in vertices],
        'z': [v[2] for v in vertices]
    }

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

V1 = [-1, -1, 0]
V2 = [-1, 0, 0]
V3 = [0, 0, 0]
V4 = [0, 1, 0]
V5 = [1, 2, 0]
V6 = [1, 3, 0]
V7 = [2, 3, 0]
V8 = [2, 2, 0]
V9 = [3, 1, 0]
V10 = [3, 0, 0]
V11 = [4, 0, 0]
V12 = [4, -1, 0]
V13 = [3, -1, 0]
V14 = [2, -2, 0]
V15 = [2, -3, 0]
V16 = [1, -3, 0]
V17 = [1, -2, 0]
V18 = [0, -1, 0]

V19 = [-1, -1, 1]
V20 = [-1, 0, 1]
V21 = [0, 0, 1]
V22 = [0, 1, 1]
V23 = [1, 2, 1]
V24 = [1, 3, 1]
V25 = [2, 3, 1]
V26 = [2, 2, 1]
V27 = [3, 1, 1]
V28 = [3, 0, 1]
V29 = [4, 0, 1]
V30 = [4, -1, 1]
V31 = [3, -1, 1]
V32 = [2, -2, 1]
V33 = [2, -3, 1]
V34 = [1, -3, 1]
V35 = [1, -2, 1]
V36 = [0, -1, 1]
VERTICES = [V1, V2, V3, V4, V5, V6, V7, V8, V9,
            V10, V11, V12, V13, V14, V15, V16, V17, V18, 
            V19, V20, V21, V22, V23, V24, V25, V26, V27,
            V28, V29, V30, V31, V32, V33, V34, V35, V36, V1]

X = [v[0] for v in VERTICES]
Y = [v[1] for v in VERTICES]

F1 = get_face_from_vertices([V1, V2, V3, V4, V5, V6, V7, V8, V9,
                             V10, V11, V12, V13, V14, V15, V16,
                             V17, V18])
F2 = get_face_from_vertices([V19, V20, V21, V22, V23, V24, V25,
                             V26, V27, V28, V29, V30, V31, V32,
                             V33, V34, V35, V36])
FACES = [F1, F2]

fig = plt.figure()
ax = fig.gca(projection='3d')

def cc(arg):
    return mcolors.to_rgba(arg, alpha=0.6)

def main(i, xs, ys, zs):
    colors = [cc('r'), cc('g'), cc('b'), cc('y')]
    # ax.plot_wireframe(face.get('x'), face.get('y'), face.get('z'), rstride=10, cstride=10)
    poly = LineCollection([list(zip(xs, ys))], facecolors=colors[i])
    poly.set_alpha(0.7)
    ax.add_collection3d(poly, zs=zs)
    c = [col for col in colors for _ in (0, 1)]
    # ax.scatter(xs, ys, zs, c=c)

# Plot object.
for face in FACES:
    main(1, face.get('x'), face.get('y'), face.get('z'))

# xs = np.arange(0, 10, 0.4)
# verts = []
# zs = [0.0, 1.0, 2.0, 3.0]
# for z in zs:
#     ys = np.random.rand(len(xs))
#     ys[0], ys[-1] = 0, 0
#     verts.append(list(zip(xs, ys)))
#     print(verts)

ax.set_xlabel('X')
ax.set_xlim3d(-4, 10)
ax.set_ylabel('Y')
ax.set_ylim3d(-4, 4)
ax.set_zlabel('Z')
ax.set_zlim3d(0, 1)

def plot_vertices(i):
    (x, y, z) = zip(VERTICES[i])
    ax.scatter(x, y, z)
ani = animation.FuncAnimation(fig, plot_vertices, interval=1000)
plt.show()