from os import path, getcwd, listdir, makedirs
from exifread import process_file
from shutil import move
from time import sleep

# DIR IMPORT
dir_path = getcwd()


def img_passer(img_file):

    # OPEN & EXTRACTION
    with open(img_file, "rb") as img:
        metadata = process_file(img)

    date = str(metadata.get('EXIF DateTimeOriginal'))
    year = date[:4]
    month = date[5:7]

    if not date:
        pass

    # CREATE DIRECTORIES
    year_dir = path.join(dir_path, year)
    month_dir = path.join(year_dir, month)
    if not path.exists(year_dir):
        makedirs(year_dir)
    if not path.exists(month_dir):
        makedirs(month_dir)

    # HANDLING
    move_path = path.join(month_dir, path.basename(img_file))
    move(img_file, move_path)


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


# RETRIEVE FILES
file_list = listdir(dir_path)
file_count = 0
for file in file_list:
    file_count += 1
    if file.endswith(".py"):
        continue

    img_path = path.join(dir_path, file)

    if path.isfile(img_path):
        img_passer(img_path)

print(f"\n{file_count} files touched! Exiting program ...")
sleep(1)
exit()
