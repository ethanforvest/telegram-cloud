import os

mode = "upload"
name = "tele"
user_name = "me"

while True:
    path_input = input("Enter the File Path: ")
    count = 0
    if os.path.isfile(path_input):
        os.system(f"tgcloud -m {mode} -n {name} -u {user_name} -p {path_input}")
        count += 1
    else:   
        list_os = os.listdir(path_input)
        for x in list_os:
            whole_path = path_input + "\\" + x
            if os.path.isfile(whole_path):
                os.system(f"tgcloud -m {mode} -n {name} -u {user_name} -p \"{whole_path}\"")
                count += 1
    print(f"Total uploads: {count}")                