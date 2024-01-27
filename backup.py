import os
import datetime
import time
import shutil
import schedule

destination_folder = "C:Users/Joe/Desktop/backups"
source_folder = "C:/Users/Joe/Pictures/Screenshots"

def copy_folder_to_directory(source, destination):
    today = datetime.date.today()
    dest_folder = os.path.join(destination,str(today))

    try:
        shutil.copytree(source,dest_folder)
        print(f"folder has been copied to: {dest_folder}")
    except FileExistsError:
        print(f"Folder already exsists inside: {destination}")

schedule.every().day.at("18:55").do(lambda: copy_folder_to_directory(source_folder, destination_folder))

while True:
    schedule.run_pending()
    time.sleep(60)
