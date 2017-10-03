#coding: utf-8
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from Polygon import Polygon

fig = plt.figure()
ax = fig.gca(projection='3d', facecolor='#B2EBF2')
ax.set_xlabel('X')
ax.set_xlim3d(-2, 5)
ax.set_ylabel('Y')
ax.set_ylim3d(-4, 4)
ax.set_zlabel('Z')
ax.set_zlim3d(-2, 6)

polygon = Polygon()

def plot_face(i):
    face = polygon.faces[i]
    xs, ys, zs = face.get_xs(), face.get_ys(), face.get_zs()
    color = face.get_color()

    edges = Line3DCollection([list(zip(xs, ys, zs))], facecolors=color, linewidths=0)
    edges.set_alpha(0.7)
    ax.add_collection3d(edges)

face_ani = animation.FuncAnimation(fig, plot_face, interval=1000)

def plot_vertices(i):
    (x, y, z, label) = polygon.vertices[i]
    ax.text(x,y,z,label)
    ax.scatter(x, y, z, c='#ffffff')

vertice_ani = animation.FuncAnimation(fig, plot_vertices, interval=1000)
plt.show()