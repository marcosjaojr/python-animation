import vpython

V1 = vpython.vertex(pos=vpython.vec(0, 0, 1), color=vpython.color.yellow)
V2 = vpython.vertex(pos=vpython.vec(0, 0, 0), color=vpython.color.yellow)
V3 = vpython.vertex(pos=vpython.vec(1, 0, 0), color=vpython.color.yellow)
V4 = vpython.vertex(pos=vpython.vec(1, 0, 1), color=vpython.color.yellow)
V5 = vpython.vertex(pos=vpython.vec(0, 1, 1), color=vpython.color.yellow)
V6 = vpython.vertex(pos=vpython.vec(0, 1, 0), color=vpython.color.yellow)
V7 = vpython.vertex(pos=vpython.vec(1, 1, 0), color=vpython.color.yellow)
V8 = vpython.vertex(pos=vpython.vec(1, 1, 1), color=vpython.color.yellow)
V9 = vpython.vertex(pos=vpython.vec(-(2**(1.0/2.0))/2, 1.0/2.0, 1.0/2.0))
V10 = vpython.vertex(pos=vpython.vec(1+(2**(1.0/2.0))/2, 1.0/2.0, 1.0/2.0))
VERTICES = [V1, V2, V3, V4, V5, V6, V7, V8, V9, V10]

F1 = vpython.quad(vs=[V1, V2, V3, V4], bumpmap=vpython.bumpmaps.stucco)
F2 = vpython.quad(vs=[V1, V4, V8, V5], color=vpython.color.yellow)
F3 = vpython.quad(vs=[V8, V7, V6, V5], color=vpython.color.yellow)
F4 = vpython.quad(vs=[V2, V6, V7, V3], color=vpython.color.yellow)
F5 = vpython.triangle(vs=[V4, V10, V8], color=vpython.color.yellow)
F6 = vpython.triangle(vs=[V8, V10, V7], color=vpython.color.yellow)
F7 = vpython.triangle(vs=[V7, V10, V3], color=vpython.color.yellow)
F8 = vpython.triangle(vs=[V3, V10, V4], color=vpython.color.yellow)
F9 = vpython.triangle(vs=[V1, V9, V2], color=vpython.color.yellow)
F10 = vpython.triangle(vs=[V5, V9, V1], color=vpython.color.yellow)
F11 = vpython.triangle(vs=[V6, V9, V5], color=vpython.color.yellow)
F12 = vpython.triangle(vs=[V2, V9, V6], color=vpython.color.yellow)
FACES = [F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, F11, F12]

vpython.scene.title = "Faces example"
vpython.scene.width = 600
vpython.scene.height = 400
vpython.box(pos=vpython.vector(1,0,0), size=vpython.vector(0.0001,1,1), color=vpython.color.green) 