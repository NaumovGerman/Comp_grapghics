import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

def draw_hyperbolic_cylinder(radius, height, sides):
    angle_step = 360.0 / sides
    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(0, 0, height / 2.0)
    for i in range(sides + 1):
        angle = i * angle_step
        x = radius * math.cos(math.radians(angle))
        y = radius * math.sin(math.radians(angle))
        glVertex3f(x, y, height / 2.0)
    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(0, 0, -height / 2.0)
    for i in range(sides + 1):
        angle = i * angle_step
        x = radius * math.cos(math.radians(angle))
        y = radius * math.sin(math.radians(angle))
        glVertex3f(x, y, -height / 2.0)
    glEnd()

    glBegin(GL_QUAD_STRIP)
    for i in range(sides + 1):
        angle = i * angle_step
        x = radius * math.cos(math.radians(angle))
        y = radius * math.sin(math.radians(angle))
        glVertex3f(x, y, height / 2.0)
        glVertex3f(x, y, -height / 2.0)
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
        draw_hyperbolic_cylinder(1, 2, 32)  # Используем новую функцию для рисования цилиндра
        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == "__main__":
    main()
