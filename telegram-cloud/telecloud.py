import os
import platform
import configparser
import time
import datetime

mode = "upload"
user_name = "me"

if not os.path.exists("config.ini"):
    config = configparser.ConfigParser()
    config["DEFAULT"] = {}
    
    unique_name = input("Enter the unique name: ")
    config["DEFAULT"]["UNIQUE_NAME"] = unique_name
    
    with open("config.ini", "w") as config_file:
        config.write(config_file)

config = configparser.ConfigParser()
config.read("config.ini")

UNIQUE_NAME = config["DEFAULT"]["UNIQUE_NAME"]  
    
total_size = 0

if platform.system() == "Windows":
    file_loc = "\\"
elif platform.system() == "Linux" or platform.system() == "Linux2":
    file_loc = "/"
    
while True:
    path_input = input("Enter the File/Folder Path: ")
    count = 0
    time_start = time.time()
    if os.path.isfile(path_input):
        os.system(f"tgcloud -m {mode} -n {UNIQUE_NAME} -u {user_name} -p {path_input}")
        file_size = os.path.getsize(path_input)
        total_size += file_size
        count += 1
    else:   
        list_os = os.listdir(path_input)
        for x in list_os:
            list_os_files = [file for file in list_os if os.path.isfile(path_input + file_loc + file)]
        list_os_files_len = len(list_os_files)
        for x in list_os:
            whole_path = path_input + file_loc + x
            if os.path.isfile(whole_path):
                print(f"Current Process --> {count + 1}/{list_os_files_len} \n")
                os.system(f"tgcloud -m {mode} -n {UNIQUE_NAME} -u {user_name} -p \"{whole_path}\"")
                file_size = os.path.getsize(whole_path)
                total_size += file_size
                count += 1
                print("\n")
    
    time_end = time.time()
    time_sec = time_end - time_start
    
    def sec_converter(sec):
        timedelta = str(datetime.timedelta(seconds=sec))
        return timedelta[5:7]

    def min_converter(sec):
        timedelta = str(datetime.timedelta(seconds=sec))
        return timedelta[2:4]
        
    def hr_converter(sec):
        timedelta = str(datetime.timedelta(seconds=sec))
        return timedelta[0]
        
    hr = hr_converter(time_sec)
    minu = min_converter(time_sec)
    sec = sec_converter(time_sec)
      
    total_size_kb = total_size / 1024   
    total_size_mb = total_size_kb / 1024   
    if total_size_mb < 1:
        total_size_kb = round(total_size_kb, 2)
        total_size = f"{total_size_kb} KB"
    elif total_size_mb > 1:
        total_size_mb = round(total_size_mb, 2)
        total_size = f"{total_size_mb} MB" 
    print(f"Total Uploads: {count} | Total Size: {total_size} | Runtime (H:M:S): {hr}:{minu}:{sec}")
    total_size = 0  
    print("\n")    
       