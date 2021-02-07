#
# Runner.py
# A program to identity and remove large duplicate files across various directories that can use up disk space
# usage:
# py Runner.py [-d] -f=mp4,ts "C:\Users\User1\Desktop\folder1" "C:\Users\User1\Desktop\folder2" "C:\Users\User1\Desktop\folder3"
# -d is optional (deletes the duplicate file)
# -f is mandatory - to define the file types for the program to scan, rather than scanning everything
#

from datetime import datetime
from Main import Main
import sys;

delete_setting = False;

start_time = datetime.now();

print("[INFO] Starting scan at " + str(start_time));
main = Main();

# check if the delete setting is on:
if "-d" in sys.argv:
    delete_setting = True;
    print("Delete setting is set to " +str(delete_setting))


for i in range(1, len(sys.argv)):
    if sys.argv[i] == "-d":
        continue;
    elif sys.argv[i].find("-f") != -1:
        # here, get the list of file extensions and put them in a list
        file_extensions = sys.argv[i].split("=")[1].split(",")

    else:
        main.__walk__(sys.argv[i], delete_setting, file_extensions);


end_time = datetime.now();

print("[INFO] Ending scan at" + str(end_time));
print("[INFO] Duration of scanning : "+str(end_time - start_time))
total_wasted_usage = sum(Main.file_sizes);
print("");
print("Total duplicate files : " + str(len(Main.file_sizes)));
print("Total wasted space = "+ str(total_wasted_usage) + " B/ " + str(total_wasted_usage/1000000) + " MB/ "+ str(total_wasted_usage/1000000000) + " GB");

# writing to file
main.__write_to_file__();