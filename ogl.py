from OpenGL.GL import *
# from OpenGL.GLU import *
from OpenGL.GLUT import *

w, h = 500, 500
SQCOLOR = [1.0, 2.0, 3.0]


class Square:
    def __init__(self, size=100, x=100, y=100):
        self.size = size
        self.x = x
        self.y = y
        self.color = [1.0, 1.0, 1.0]

    def render(self):
        glColor3f(*self.color)
        glBegin(GL_QUADS)
        glVertex2f(self.x, self.y)
        glVertex2f(self.x + self.size, self.y)
        glVertex2f(self.x + self.size, self.y + self.size)
        glVertex2f(self.x, self.y + self.size)
        glEnd()


SCENE = [Square(100, 100, 100)]


# ---Section 1---
def square():
    glBegin(GL_QUADS)
    glVertex2f(100, 100)
    glVertex2f(200, 100)
    glVertex2f(200, 200)
    glVertex2f(100, 200)
    glEnd()


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def show_screen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    # glColor3f(*SQCOLOR)
    # square()
    for obj in SCENE:
        obj.render()
    glutSwapBuffers()


def keys(key_bytes, x, y):
    key = key_bytes.decode(encoding='utf-8')
    if key in ['q', 'Q', chr(27)]:
        glutDestroyWindow(WIND)
        exit()

    # global SQCOLOR
    if key == 'r':
        SCENE[0].color = [255.0, 0.0, 0.0]
    elif key == 'g':
        SCENE[0].color = [0.0, 255.0, 0.0]
    elif key == 'b':
        SCENE[0].color = [0.0, 0.0, 255.0]


WIND = 0


def main():
    glutInit()  # Initialize a glut instance which will allow us to customize our window
    glutInitDisplayMode(GLUT_RGBA)  # Set the display mode to be colored
    glutInitWindowSize(500, 500)  # Set the width and height of your window
    glutInitWindowPosition(0, 0)  # Set the position at which this windows should appear

    global WIND
    WIND = glutCreateWindow("OpenGL Coding Practice")  # Give your window a title

    glutDisplayFunc(show_screen)  # Tell OpenGL to call the showScreen method continuously
    glutIdleFunc(show_screen)  # Draw any graphics or shapes in the showScreen function at all times
    glutKeyboardFunc(keys)
    glutMainLoop()  # Keeps the window created above displaying/running in a loop


if __name__ == '__main__':
    main()
