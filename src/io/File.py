import os
import struct
import shutil
import win32com.client

from src.config.Constant import ERROR_RED
from src.io.Console import out


def create_folder(path):
    if path_exists(path):
        return

    try:
        os.mkdir(path)
    except OSError:
        out('Folder creation failed ! path : {}'.format(path), ERROR_RED)
        exit(0)


def path_type(path):
    if os.path.isdir(path):
        return 'DIR'
    return 'FILE'


def path_exists(path):
    return os.path.exists(path)


def get_current_wd():
    return os.getcwd()


def get_home():
    return os.path.expanduser("~")


def get_file_name(path):
    return os.path.basename(path)


def get_file_path(f):
    return os.path.dirname(f)


def del_file(f):
    if os.path.exists(f) and path_type(f) == 'FILE':
        return os.remove(f)
    out('File path is not valid: \"{}\"'.format(f), ERROR_RED)
    exit(0)


def del_dir(p):
    if os.path.exists(p) and path_type(p) == 'DIR':
        return shutil.rmtree(p)
    out('Directory path is not valid: \"{}\"'.format(p), ERROR_RED)
    exit(0)


def list_dir(d):
    return os.listdir(d)


def file_join_path(p, f):
    return os.path.join(p, f)


def edit_file_time(p: str):
    return os.utime(p)


def get_lnk_file_target(p: str):
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(p)
    return shortcut.Targetpath


def get_lnk_file_target_old(p: str):
    target = ''

    with open(p, 'rb') as stream:
        content = stream.read()
        # skip first 20 bytes (HeaderSize and LinkCLSID)
        # read the LinkFlags structure (4 bytes)
        lflags = struct.unpack('I', content[0x14:0x18])[0]
        position = 0x18
        # if the HasLinkTargetIDList bit is set then skip the stored IDList
        # structure and header
        if (lflags & 0x01) == 1:
            position = struct.unpack('H', content[0x4C:0x4E])[0] + 0x4E
        last_pos = position
        position += 0x04
        # get how long the file information is (LinkInfoSize)
        length = struct.unpack('I', content[last_pos:position])[0]
        # skip 12 bytes (LinkInfoHeaderSize, LinkInfoFlags, and VolumeIDOffset)
        position += 0x0C
        # go to the LocalBasePath position
        lbpos = struct.unpack('I', content[position:position + 0x04])[0]
        position = last_pos + lbpos
        # read the string at the given position of the determined length
        size = (length + last_pos) - position - 0x02
        temp = struct.unpack('c' * size, content[position:position + size])
        target = ''.join([chr(ord(a)) for a in temp])

    return target
