from os import path, getcwd, listdir, makedirs
from exifread import process_file
from shutil import move
from time import sleep, strftime, localtime

'''
.log Codes:

000 - Successful operation

E01 - Invalid Format. KwikSort does not support the file format. File must be any of the following formats:
            [jpg, jpeg, png, gif, bmp, tiff, webp, mp4, mov, avi, mkv, wmv, flv, webm, mpeg.]
                        
E02 - Duplicate file. A file in the target directory already exists
'''

# DIR IMPORT
dir_path = getcwd()
log = "".join(dir_path + "\\_logs")


def img_passer(img_file):
    if not path.exists(log):
        makedirs(log)

    with open(f"{log}\\{strftime('%Y%m%d')}.log", "a") as logfile:
        logfile.write(f"{strftime('\n%H:%M:%S | ')}")

        try:
            # OPEN & EXTRACTION
            with open(img_file, "rb") as img:
                metadata = process_file(img)

            date = metadata.get("EXIF DateTimeOriginal")

            if not date:
                mod_time = path.getmtime(img_file)
                mod_date = strftime("%Y:%m", localtime(mod_time))
                year, month = mod_date[:4], mod_date[5:7]
            else:
                date = str(date)
                year, month = date[:4], date[5:7]

            # CREATE DIRECTORIES
            year_dir = path.join(dir_path, year)
            month_dir = path.join(year_dir, month)

            if not path.exists(year_dir):
                makedirs(year_dir)
            if not path.exists(month_dir):
                makedirs(month_dir)

            # HANDLING
            move_path = path.join(month_dir, path.basename(img_file))

            if path.isfile(move_path):
                logfile.write(f"E02 | '{path.basename(img_file)}' cannot move to {move_path}. File already exists\n")
            else:
                move(img_file, move_path)
                logfile.write(f"000 | '{path.basename(img_file)}' moved to {move_path}\n")

        # USED TO PASS 'CORRUPT' FILES
        except Exception as e:
            logfile.write(f"File Unreadable: {img_file} - Error: {str(e)}\n")
            pass


print(
    "!!! IMPORTANT !!!\n\n"
    "KWIKSORT is to be used at your own risk.\nThough I have done everything in my best effort to ensure"
    " there is zero chance of corruption to your files, \nI cannot guarantee or be held liable"
    " for any loss of data that may arise from using this tool, and any\nresponsibility lies on you, the user,"
    "to use this tool appropriately and understand the risks.\n"
    "Having said that, I hope you enjoy this neat little tool :-)\n"
)

while True:
    match input("(RETURN) RUN KWIKSORT NOW | (E) EXIT \n>>> "):
        case "":
            break
        case "e" | "E":
            print("\nExiting program ... ")
            sleep(1)
            exit()

# RETRIEVE FILES AND HANDLE FILE TYPES
file_list = listdir(dir_path)
file_count = 0
img_fmts = (".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp")
vid_fmts = (".mp4", ".mov", ".avi", ".mkv", ".wmv", ".flv", ".webm", ".mpeg")

for file in file_list:
    if not file.endswith(img_fmts + vid_fmts):
        if path.isdir(file) or file.endswith(".log"):
            continue
        with open(f"{strftime('%Y%m%d')}.log", "a") as logfile:
            logfile.write(f"\n{strftime('%H:%M:%S')} | E01 | Invalid format for '{path.basename(file)}'\n")
        continue

    img_path = path.join(dir_path, file)

    if path.isfile(img_path):
        img_passer(img_path)
        file_count += 1

print(f"\n{file_count} files sorted! Exiting program ...")
sleep(1)
exit()
