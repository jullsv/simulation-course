import matplotlib.animation as animation
import matplotlib.colors as colors
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider

SIZE = 50
center = SIZE // 2

EMPTY, SMALL_TREE, TREE, DEAD_TREE, FIRE, WATER = 0, 1, 2, 3, 4, 5

FLAMMABILITY = {
    SMALL_TREE: {"side": 0.8, "diag": 0.65},
    TREE: {"side": 0.7, "diag": 0.4},
    DEAD_TREE: {"side": 1.0, "diag": 0.9},
}

GROWTH_PROB = {"side": 0.1, "diag": 0.05}
GROW_UP_PROB = 0.1
DEATH_PROB = 0.002
DEATH_DEATH_PROB = 0.001

WIND_DIRECTION = np.random.randint(0, 360)
WIND_STRENGTH = 0.7
HUMIDITY = 0.5


def group_water(grid, i=3):
    result = grid.copy()

    for _ in range(i):
        new = result.copy()
        for y in range(1, SIZE - 1):
            for x in range(1, SIZE - 1):
                neighbors = result[y - 1 : y + 2, x - 1 : x + 2]
                water_count = np.sum(neighbors == WATER)
                if water_count > 4:
                    new[y, x] = WATER
                elif water_count < 2:
                    if result[y, x] == WATER:
                        new[y, x] = EMPTY
        result = new
    return result


grid = np.random.choice(
    [EMPTY, TREE, WATER, DEAD_TREE], SIZE * SIZE, p=[0.87, 0.02, 0.1, 0.01]
).reshape(SIZE, SIZE)
grid = group_water(grid)
grid[center - 3 : center + 3, center - 3 : center + 3] = TREE

fig, ax = plt.subplots()
colors_list = ["brown", "lightgreen", "green", "sandybrown", "red", "blue"]
cmap = colors.ListedColormap(colors_list)
bounds = [-0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5]
norm = colors.BoundaryNorm(bounds, cmap.N)
img = ax.imshow(grid, cmap=cmap, norm=norm, interpolation="nearest")
ax.axis("off")
wind_arrow = ax.quiver(
    5,
    5,
    np.cos(np.radians(WIND_DIRECTION)),
    -np.sin(np.radians(WIND_DIRECTION)),
    scale=9,
    color="black",
    edgecolors="black",
    width=0.02,
    headwidth=8,
    headlength=8,
    zorder=10,
)

ax_humidity = plt.axes([0.25, 0.02, 0.50, 0.04])

humidity_slider = Slider(
    ax=ax_humidity,
    label="Влажность",
    valmin=0.0,
    valmax=1.0,
    valinit=0.5,
)


def update_humidity(val):
    global HUMIDITY
    HUMIDITY = val


humidity_slider.on_changed(update_humidity)


def on_click(event):
    if event.inaxes != ax:
        return

    x = int(event.xdata)
    y = int(event.ydata)

    if x < 0 or x >= SIZE or y < 0 or y >= SIZE:
        return

    if grid[y, x] not in [TREE, SMALL_TREE, DEAD_TREE]:
        return

    grid[y, x] = FIRE


fig.canvas.mpl_connect("button_press_event", on_click)


def wind(dy, dx, wind_dir, wind_str):
    directions = {
        (0, 1): 0,
        (1, 0): 90,
        (0, -1): 180,
        (-1, 0): 270,
        (1, 1): 45,
        (1, -1): 135,
        (-1, -1): 225,
        (-1, 1): 315,
    }
    neighbor_angle = directions.get((dy, dx), 0)
    angle_diff = (neighbor_angle - wind_dir + 180) % 360 - 180
    alignment = np.cos(np.radians(angle_diff))
    return 1.0 + wind_str * alignment


def iterate(current_grid):
    new_grid = current_grid.copy()
    height, width = current_grid.shape

    for y in range(1, height - 1):
        for x in range(1, width - 1):
            cell = current_grid[y, x]

            if cell == WATER:
                new_grid[y, x] = WATER
                continue

            if cell == FIRE:
                new_grid[y, x] = EMPTY
                continue

            if cell in [SMALL_TREE, TREE, DEAD_TREE]:
                is_burn = False
                params = FLAMMABILITY[cell]
                base_neighbors = [
                    (-1, 0),
                    (1, 0),
                    (0, -1),
                    (0, 1),
                    (-1, -1),
                    (-1, 1),
                    (1, -1),
                    (1, 1),
                ]

                for dy, dx in base_neighbors:
                    if abs(dy) + abs(dx) == 1:
                        base_prob = params["side"]
                    else:
                        base_prob = params["diag"]

                    wind_mod = wind(-dy, -dx, WIND_DIRECTION, WIND_STRENGTH)
                    humidity_prob = 1.0 - HUMIDITY
                    final_prob = base_prob * wind_mod
                    final_prob = min(1.0, max(0.0, final_prob * humidity_prob))

                    if (
                        current_grid[y + dy, x + dx] == FIRE
                        and np.random.random() < final_prob
                    ):
                        is_burn = True
                        break

                if is_burn:
                    new_grid[y, x] = FIRE
                else:
                    if cell == TREE and np.random.random() < DEATH_PROB:
                        new_grid[y, x] = DEAD_TREE
                    elif cell == SMALL_TREE and np.random.random() < GROW_UP_PROB:
                        new_grid[y, x] = TREE
                    elif cell == DEAD_TREE and np.random.random() < DEATH_DEATH_PROB:
                        new_grid[y, x] = EMPTY
                    else:
                        new_grid[y, x] = cell
                continue

            if cell == EMPTY:
                grows = False
                all_trees = [SMALL_TREE, TREE, DEAD_TREE]
                for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    if current_grid[y + dy, x + dx] in all_trees:
                        if np.random.random() < GROWTH_PROB["side"]:
                            grows = True
                            break
                for dy, dx in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                    if current_grid[y + dy, x + dx] in all_trees:
                        if np.random.random() < GROWTH_PROB["diag"]:
                            grows = True
                            break

                new_grid[y, x] = SMALL_TREE if grows else EMPTY
                continue

    return new_grid


def update(frame):
    global grid, WIND_DIRECTION, HUMIDITY

    if frame % 100 == 0:
        WIND_DIRECTION = np.random.randint(0, 360)

    grid = iterate(grid)
    img.set_array(grid)

    wind_arrow.set_UVC(
        np.cos(np.radians(WIND_DIRECTION)), -np.sin(np.radians(WIND_DIRECTION))
    )
    return [img, wind_arrow]


ani = animation.FuncAnimation(fig, update, interval=10, blit=True)
plt.show()
