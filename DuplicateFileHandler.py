class DuplicateFileHandler:

    duplicate = {};

    def __init__(self):
        print("empty constructor");

    def check_and_add_entry(self, original_file, duplicate_file):
        if original_file in DuplicateFileHandler.duplicate.keys():
            DuplicateFileHandler.duplicate.get(original_file).add(duplicate_file);
        else:
            DuplicateFileHandler.duplicate[original_file] = {duplicate_file};
