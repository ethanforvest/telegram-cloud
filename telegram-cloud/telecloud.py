import os

mode = "upload"
name = "tele"
user_name = "me"

path = input("Enter the File Path: ")

list_os = os.listdir(path)

for x in list_os:
    whole_path = path + "\\" + x
    if os.path.isfile(whole_path):
        os.system(f"tgcloud -m {mode} -n {name} -u {user_name} -p {whole_path}")
