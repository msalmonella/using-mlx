import sys
from mlx import Mlx

m = Mlx()
mlx_ptr = m.mlx_init()
window = m.mlx_new_window(mlx_ptr, 1280, 960, "Maze")

def on_close(param):
    m.mlx_loop_exit(mlx_ptr)

def on_key(keycode, param):
    if keycode == 65307:
        m.mlx_loop_exit(mlx_ptr)
    elif keycode == 32:
        m.mlx_loop_exit(mlx_ptr)

# m.mlx_string_put(mlx_ptr, window, 20, 20, 0xFFFFFFFF, "Hello MLX!")

for i in range(400):
    for j in range(400):
        m.mlx_pixel_put(mlx_ptr, window, i, j, 0xFFFF0000)

m.mlx_hook(window, 33, 0, on_close, None)
m.mlx_key_hook(window, on_key, None)


m.mlx_loop(mlx_ptr)
m.mlx_release(mlx_ptr)
