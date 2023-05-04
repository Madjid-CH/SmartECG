def get_path(relative_path, go_up_by=-1):
    path = __file__.split("\\")
    path = "\\".join(path[:go_up_by])
    path += relative_path
    return path
