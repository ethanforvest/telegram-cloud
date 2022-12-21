import os

mode = "upload"
name = "tele"
user_name = "me"

total_size = 0

while True:
    path_input = input("Enter the File Path: ")
    count = 0
    if os.path.isfile(path_input):
        # os.system(f"tgcloud -m {mode} -n {name} -u {user_name} -p {path_input}")
        file_size = os.path.getsize(path_input)
        total_size += file_size
        count += 1
    else:   
        list_os = os.listdir(path_input)
        for x in list_os:
            whole_path = path_input + "\\" + x
            if os.path.isfile(whole_path):
                # os.system(f"tgcloud -m {mode} -n {name} -u {user_name} -p \"{whole_path}\"")
                file_size = os.path.getsize(whole_path)
                total_size += file_size
                count += 1
                
    total_size_kb = total_size / 1024   
    total_size_mb = total_size_kb / 1024   
    if total_size_mb < 1:
        total_size = f"{total_size_kb} KB"
    elif total_size_mb > 1:
        total_size = f"{total_size_mb} MB" 
    print(f"Total Uploads: {count} | Total Size: {total_size}")
    total_size = 0         