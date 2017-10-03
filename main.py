#coding: utf-8

from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
from matplotlib.widgets import Button
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from Polygon import Polygon
import time

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

face_ani = animation.FuncAnimation(fig, plot_face, frames=len(polygon.faces),
                                   repeat=False, interval=1000)

flatten_vertices = [item for face in polygon.faces for item in face.get_vertices()]
def plot_vertices(i):
    (x, y, z) = flatten_vertices[i]
    ax.text(x, y, z, str((x, y, z)))
    ax.scatter(x, y, z, c='#ffffff')

vertice_ani = animation.FuncAnimation(fig, plot_vertices, interval=1000,
                                      frames=len(flatten_vertices), repeat=False)

def clean():
    face_ani.event_source.stop()
    vertice_ani.event_source.stop()
    ax.clear()

def restore_polygon(event):
    clean()
    polygon = Polygon()
    for i in range(len(polygon.faces)):
        plot_face(i)
    plt.draw()

def iso_proj(event):
    clean()
    polygon.iso_proj()
    for i in range(len(polygon.faces)):
        plot_face(i)
    plt.draw()

def obliq_proj(event):
    clean()
    polygon.obliq_proj()
    for i in range(len(polygon.faces)):
        plot_face(i)
    plt.draw()

def pers_proj(event):
    clean()
    polygon.pers_proj()
    for i in range(len(polygon.faces)):
        plot_face(i)
    plt.draw()

axobliqproj = plt.axes([0.7, 0.05, 0.1, 0.075])
axisoproj = plt.axes([0.5, 0.05, 0.15, 0.075])
axrestore = plt.axes([0.3, 0.05, 0.13, 0.075])
axpersproj = plt.axes([0.1, 0.05, 0.13, 0.075])
axobliqproj = Button(axobliqproj, 'Oblíqua')
axobliqproj.on_clicked(obliq_proj)
bisoproj = Button(axisoproj, 'Isométrica')
bisoproj.on_clicked(iso_proj)
axrestore = Button(axrestore, 'Restaurar')
axrestore.on_clicked(restore_polygon)
axpersproj = Button(axpersproj, 'Perspectiva')
axpersproj.on_clicked(pers_proj)

plt.subplots_adjust(bottom=0.2)
plt.show()
