import os

mode = "upload"
name = "tele"
user_name = "me"

path = input("Enter the File Path: ")

os.system(f"tgcloud -m {mode} -n {name} -u {user_name} -p {path}")
