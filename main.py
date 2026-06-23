import mlx
print([name for name in dir(mlx) if "window" in name.lower() or "loop" in name.lower() or "init" in name.lower()])

