import hashlib

from cachetools import LRUCache


def get_path(relative_path, go_up_by=-1):
    path = __file__.split("\\")
    path = "\\".join(path[:go_up_by])
    path += relative_path
    return path


def hash_dataframe(df):
    df_string = str(df.values)
    h = hashlib.sha256()
    h.update(df_string.encode('utf-8'))
    return h.hexdigest()


def get_a_cache():
    return LRUCache(maxsize=1)
