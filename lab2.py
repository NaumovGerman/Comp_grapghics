import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from mpl_toolkits.mplot3d.proj3d import proj_transform
from matplotlib.widgets import Button

# Создаем трехмерную сцену
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Задаем вершины и грани для вашей усеченной пирамиды
vertices = np.array([[2, 2, -2],
                     [2, -2, -2],
                     [-2, -2, -2],
                     [-2, 2, -2],
                     [1, 1, 3],
                     [1, -1, 3],
                     [-1, -1, 3],
                     [-1, 1, 3]])

faces = np.array([
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [0, 1, 5, 4],
    [1, 2, 6, 5],
    [2, 3, 7, 6],
    [3, 0, 4, 7]
])

# Функция для отображения/скрытия невидимых линий
def toggle_hidden_lines(event):
    alpha = 0.5 if miracle[0].get_alpha() == 1 else 1
    miracle[0].set_alpha(alpha)
    fig.canvas.draw()

# Создаем кнопку для отображения/скрытия невидимых линий
ax_button = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(ax_button, 'Show')
button.on_clicked(toggle_hidden_lines)

# Отображаем усеченную пирамиду с удалением невидимых линий
miracle = [Poly3DCollection([vertices[face] for face in faces], alpha=0.5, facecolor='orange', edgecolor='k')]
ax.add_collection3d(miracle[0])

# Функция для обработки событий клавишами
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
    fig.canvas.draw()

fig.canvas.mpl_connect('key_press_event', on_key)
ax.auto_scale_xyz([-3, 3], [-3, 3], [-3, 3])

# Отображаем сцену
plt.show()
