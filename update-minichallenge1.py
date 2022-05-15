# Aim: Combining git commands and python script to clone git repository, create new file and pushing to repository.
	
# importing os module
import os

#1. Cloning exiting git repository:
url = input("Please input repository url: ")
repo_url = "git clone " + url
os.system(repo_url)

#2. Changing into the file directory:
repo_name = input("Please input repository name per github page: ")
new_path = os.getcwd() + "/" + f"{repo_name}"
os.chdir(f"{new_path}")

#3.
#(a)Ask if user will like to check on current git repository status
#(b)If no, a "command.txt" will be automatically be created.
#(c)If yes, commands such as git status / git log and git branch will be asked. 
def question():
    check_status = input("Will you like to check status on current git repository? (yes/no): ")
    if check_status == "no":
        os.system(f"touch commands.txt")
        with open("commands.txt","w") as f:
            f.write("git add .\n")
            f.write("git status\n")
    else:
        status = input("What will you like to check? (git status , git log or git branch): ") 
        if status == "git status":
            os.system(f"git status")
        elif status == "git log":
            os.system (f"git log")
        elif status == "git branch":
            os.system (f"git branch")
question()

#Instead of creating an additional text file to run script, using function:
def add():
    os.system("git add .")
    os.system("git status")

#4. Does the user want to create a new directory within the current repository?:
#(a) If no, user can create new file automatically
#(b) If yes, have to key in new repo name and create new file at the same time.
create_repo = input("Do you wish to create a new directory? (yes/no): ")

if create_repo == "no":
    create_file = input("Please input your file name and extension type: ")
    os.system(f"touch {create_file}")
    with open(create_file,"w") as file:
        file.write(input("Please key in intended message: "))
else:
    make_new = input("Please input new directory name: ")
    os.mkdir(f"{make_new}")
    new_path = os.getcwd() + "/" + f"{make_new}"
    os.chdir(f"{new_path}")
    create_file = input("Please input your file name and extension type: ")
    os.system(f"touch {create_file}")
    with open(create_file,"w") as file:
        file.write(input("Please key in intended message: "))

#5. Ask user if they require to check on current git status
question()

#6. Save new file content (commit) and push to git repository:
add()
saving = input("Will you like to proceed with 'git commit' & 'git push'? (yes/no): ")

if saving == "no":
    print("No further action done.")
else:
    message = input("Please key in the message you will like to display at 'commit stage': ")
    os.system(f"git commit -m '{message}'")
    os.system(f"git push")
    print("Successfully commited and pushed to git repository")