import json
from os import walk,path

def file_to_dict(fpath):
    return {
        'name': path.basename(fpath),
        'type': 'file',
        }

def folder_to_dict(rootpath):
    return {
            'name': path.basename(rootpath),
            'type': 'folder',
            'children': [],
            }

def tree_to_dict(rootpath):
    root_dict = folder_to_dict(rootpath)
    try:
        root, folders, files = next(walk(rootpath))
        root_dict['children'] = [file_to_dict(path.sep.join([root, fpath])) for fpath in files]
        root_dict['children'] += [tree_to_dict(path.sep.join([root, folder])) for folder in folders]
        return root_dict
    except:
        pass
    

def tree_to_json(rootdir):
    try:
        root,folders,files = next(walk(rootdir))
        root_dict = [tree_to_dict(path.sep.join([root, folder])) for folder in folders]
        root_dict += [file_to_dict(path.sep.join([root, fpath])) for fpath in files]
        return root_dict
    except:
        pass
    

