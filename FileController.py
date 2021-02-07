class FileController:

    def __init__(self):
        print("Empty constructor");

    def write_to_file(self, dict):
        f = open("output.json", "w");
        f.write("{\n")
        original_files_count = len(dict.keys());
        for k in dict.keys():
            original_files_count-=1;
            f.write("\t{\n")
            f.write('\t\t\"originalFile\": \"'+ k +'\",\n');
            f.write('\t\t\"duplicateFiles\": [ \n')
            duplicate_files_count = len(dict[k]);
            for v in dict[k]:
                duplicate_files_count -=1;
                f.write('\t\t\t\"' + v + "\"" +FileController.determine_comma_value(duplicate_files_count)+"\n");
            f.write('\t\t ]\n');
            f.write("\t} "+FileController.determine_comma_value(original_files_count)+"\n");
        f.write("}");
        f.close();

    @staticmethod
    def determine_comma_value(counter):
        if counter == 0:
            return ""
        return ",";