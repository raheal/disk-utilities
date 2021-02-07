import os;
import hashlib;
from os.path import isdir;
import sys;
import datetime;
from DuplicateFileHandler import DuplicateFileHandler;
from FileController import FileController;


class Main:
    dictMap = {};
    BLOCKSIZE = 65536;
    duplicate_counter = 0;
    file_sizes = [];

    def __walk__(self, dir_path, delete_setting, file_extensions):
        root_directory = dir_path;
        files = os.listdir(os.path.abspath(root_directory));
        for f in files:
            path = root_directory + "/" + f;
            if (isdir(path)):
                Main.__walk__(path, delete_setting, file_extensions);
            else:
                if len(file_extensions) != 0:
                    for f in file_extensions:
                        if str(path).endswith(f):
                            hasher = hashlib.md5();
                            with open(path, 'rb') as afile:
                                buf = afile.read(Main.BLOCKSIZE)
                                while len(buf) > 0:
                                    hasher.update(buf)
                                    buf = afile.read(Main.BLOCKSIZE)
                            result = hasher.hexdigest();
                            if result in Main.dictMap:
                                print("[INFO] Duplicate found : [" + path + "], original copy  = [" + Main.dictMap[
                                    result] + "]");
                                # here, try and add it to the duplicate file handler, which will write to the file
                                self.duplicateFileHandler.check_and_add_entry(Main.dictMap[result], path);
                                Main.file_sizes.append(os.path.getsize(path));
                                if delete_setting == True:
                                    # delete the file off the file system
                                    os.remove(path);
                            else:
                                Main.dictMap[result] = path;

    def __init__(self):
        print("Empty constructor");
        duplicateFileHandler = DuplicateFileHandler();
        self.duplicateFileHandler = duplicateFileHandler;

    def __write_to_file__(self):
        print("Writing to file....");
        file_controller = FileController();
        file_controller.write_to_file(DuplicateFileHandler.duplicate);
