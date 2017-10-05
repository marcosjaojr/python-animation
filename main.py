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

def plot_face(i, faces):
    face = faces[i]
    xs, ys, zs = face.get_xs(), face.get_ys(), face.get_zs()
    color = face.get_color()

    edges = Line3DCollection([list(zip(xs, ys, zs))], facecolors=color, linewidths=0)
    edges.set_alpha(0.7)
    ax.add_collection3d(edges)

def plot_all_faces(faces):
    for i in range(len(faces)):
        plot_face(i, faces)

def plot_vertice(i, vertices):
    (x, y, z) = vertices[i][0:3]
    ax.text(x, y, z, str((x, y, z)))
    ax.scatter(x, y, z, c='#ffffff')

def plot_all_vertices(vertices):
    for i in range(len(vertices)):
        plot_vertice(i, vertices)

def clean():
    face_ani.event_source.stop()
    vertice_ani.event_source.stop()
    ax.clear()

def animate(event):
    clean()
    face_ani.frame_seq = face_ani.new_frame_seq()
    face_ani.event_source.start()
    vertice_ani.frame_seq = vertice_ani.new_frame_seq()
    vertice_ani.event_source.start()

def restore_polygon(event):
    clean()
    polygon = Polygon()
    plot_all_faces(polygon.faces)
    plot_all_vertices(polygon.vertices)
    plt.draw()

def iso_proj(event):
    clean()
    polygon = Polygon()
    polygon.iso_proj()
    plot_all_faces(polygon.faces)
    plot_all_vertices(polygon.vertices)
    plt.draw()

def obliq_proj(event):
    clean()
    polygon = Polygon()
    polygon.obliq_proj()
    plot_all_faces(polygon.faces)
    plot_all_vertices(polygon.vertices)
    plt.draw()

def pers_proj(event):
    clean()
    polygon = Polygon()
    polygon.pers_proj()
    plot_all_faces(polygon.faces)
    plot_all_vertices(polygon.vertices)
    plt.draw()

axanimate = plt.axes([0.8, 0.05, 0.13, 0.075])
banimate = Button(axanimate, 'Animar')
banimate.on_clicked(animate)

axobliqproj = plt.axes([0.68, 0.05, 0.1, 0.075])
bobliqproj = Button(axobliqproj, 'Oblíqua')
bobliqproj.on_clicked(obliq_proj)

axisoproj = plt.axes([0.5, 0.05, 0.15, 0.075])
bisoproj = Button(axisoproj, 'Isométrica')
bisoproj.on_clicked(iso_proj)

axrestore = plt.axes([0.3, 0.05, 0.13, 0.075])
brestore = Button(axrestore, 'Restaurar')
brestore.on_clicked(restore_polygon)

axpersproj = plt.axes([0.1, 0.05, 0.13, 0.075])
bpersproj = Button(axpersproj, 'Perspectiva')
bpersproj.on_clicked(pers_proj)

face_ani = animation.FuncAnimation(fig, plot_face, frames=len(Polygon().faces),
                                   repeat=False, interval=1000, fargs=(Polygon().faces,))

vertice_ani = animation.FuncAnimation(fig, plot_vertice, interval=1000,
                                      frames=len(Polygon().get_ordered_vertices()),
                                      repeat=False, fargs=(Polygon().get_ordered_vertices(),))

plt.subplots_adjust(bottom=0.2)
plt.show()
