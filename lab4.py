import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
import numpy as np


def draw_hyperbolic_cylinder(a, b, height, num_points):
    vertices = []
    num_points += 1
    phi = np.linspace(0, 2 * np.pi, num_points)
    z = np.linspace(-height / 2.0, height / 2.0, num_points)

    for zi in z:
        for angle in phi:
            x = a * np.cosh(zi / height) * np.cos(angle)
            y = b * np.cosh(zi / height) * np.sin(angle)
            vertices.append([x, y, zi])

    glBegin(GL_QUADS)
    for i in range(len(vertices) - num_points):
        if (i + 1) % num_points == 0:
            continue
        glVertex3fv(vertices[i])
        glVertex3fv(vertices[i + 1])
        glVertex3fv(vertices[i + num_points + 1])
        glVertex3fv(vertices[i + num_points])
    glEnd()


def main():
    pygame.init()
    display = (1280, 720)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    glEnable(GL_LIGHTING)
    glEnable(GL_DEPTH_TEST)

    glLightfv(GL_LIGHT0, GL_POSITION, [0, 1, 0, 3])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1.0])
    glEnable(GL_LIGHT0)

    glMaterial(GL_FRONT, GL_DIFFUSE, [1.0, 0.0, 0.0, 1.0])

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_hyperbolic_cylinder(1, 2, 2, 32)  # Параметры a=1, b=2, height=2 и 32 сегмента
        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == "__main__":
    main()
