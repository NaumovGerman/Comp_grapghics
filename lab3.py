import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import TextBox, Button

cstride = 1
qw = 0.9

def PlotCylinderWithHyperbolicBase(a, b, height, num_points):
    num_points += 1
    phi = []
    z = []

    dPhi = 2 * np.pi / (num_points - 1)
    dZ = height / (num_points - 1)

    for i in range(num_points):
        phi.append(i * dPhi)
        z.append(i * dZ)

    ##
    phi, z = np.meshgrid(phi, z)

    x = a * np.cosh(z / height) * np.cos(phi)
    y = b * np.cosh(z / height) * np.sin(phi)

    ##
    ax.clear()
    ax.plot_surface(x, y, z, alpha=qw, cstride=cstride)

    # Добавление меток на осях ординат
    ax.set_zticks(np.arange(0, 1.5 * height, 5))

    # Добавление стрелочек к осям X, Y и Z
    ax.quiver(0, 0, 0, 0, -(b + 2), 0, color='r', label='x')
    ax.quiver(0, 0, 0, a + 2, 0, 0, color='g', label='Y')
    ax.quiver(0, 0, 0, 0, 0, height + 5, color='b', label='Z')

    ax.legend()

    plt.show()


def AxisInstallation():
    ax.set_xlim([-a - 0.5, a + 0.5])
    ax.set_ylim([-b - 0.5, b + 0.5])
    ax.set_zlim([0, 1.5 * height])


def ChangePrecision(input):
    ax.clear()
    AxisInstallation()
    PlotCylinderWithHyperbolicBase(a, b, height, int(input))


a = 20  # Полуось a
b = 3  # Полуось b
height = 10  # Высота цилиндра

f = plt.figure()
ax = f.add_subplot(111, projection='3d')


def on_key(event):
    if event.key == 'left':
        ax.view_init(elev=ax.elev, azim=ax.azim - 10)
    elif event.key == 'right':
        ax.view_init(elev=ax.elev, azim=ax.azim + 10)
    elif event.key == 'up':
        ax.view_init(elev=ax.elev + 10, azim=ax.azim)
    elif event.key == 'down':
        ax.view_init(elev=ax.elev - 10, azim=ax.azim)
    elif event.key == '+':
        ax.dist = ax.dist * 0.9
    elif event.key == '-':
        ax.dist = ax.dist * 1.1
    f.canvas.draw()


def toggleCstride(event):
    global cstride
    global qw
    if cstride > 1:
        cstride = 1
        qw = 0.9
    else:
        cstride = 3
        qw = 1
    PlotCylinderWithHyperbolicBase(a, b, height, 50)


f.canvas.mpl_connect('key_press_event', on_key)

AxisInstallation()
precisionField = plt.axes([0.5, 0.05, 0.1, 0.05])
precisionTextBox = TextBox(precisionField, 'Precision: ', '50')
precisionTextBox.on_submit(ChangePrecision)

cstrideButtonAx = plt.axes([0.7, 0.01, 0.2, 0.04])
cstrideButton = Button(cstrideButtonAx, 'Hide lines', color='lightgoldenrodyellow')
cstrideButton.on_clicked(toggleCstride)

PlotCylinderWithHyperbolicBase(a, b, height, 50)
