from src.config.Constant import *
from src.io.File import list_dir, path_type, file_join_path, get_file_name, get_home


def get_dirs_r(root):
    arr = []
    get_dirs(root, arr)
    return arr


def get_dirs(root, paths):
    for element in list_dir(root):
        path = file_join_path(root, element)

        if path_type(path) == 'FILE':
            paths.append(path)
        else:
            get_dirs(path, paths)


def look_for_in(filters, paths):
    final_paths = []
    for file in paths:
        for flt in filters:
            file_name = get_file_name(file).lower().split('.')[0]
            filter_name = get_file_name(flt).replace('_', ' ').lower().split('.')[0]
            if file_name in filter_name:
                final_paths.append(dict(icon_path=flt, lnk_path=file))
    return final_paths


def get_filtered_list(search_for, search_in):
    paths = []
    for path in search_in:
        if HOME_DIR in path:
            path = path.replace(HOME_DIR, get_home())
        get_dirs(path, paths)

    filters = []
    get_dirs(search_for, filters)

    return look_for_in(filters, paths)
