# Python program to explain os.system() method
	
# importing os module
import os

#1. Create new directory:
repo_name = input("Please input directory name: ")
os.mkdir(f"{repo_name}")

#2. Changing directory:
new_path = os.getcwd() + "/" + f"{repo_name}"
os.chdir(f"{new_path}")

# Optional : Use the following to check current directory #
# cwd = os.getcwd()
# print("current :" , cwd)

#3. Make GIT environment staging:
# Note : git init is only used  when needed to create a new repository
os.system(f"git init")

#4. Create GIT command file to run later:
os.system(f"touch commands.txt")
with open("commands.txt","w") as f:
    f.write("git status\n")
    f.write("git add .\n")
    f.write("git log") 

#5. Create intended file and input info(as desired):
create_file = input("Please input your file name and extension type: ")
os.system(f"touch {create_file}")

with open(create_file,"w") as file:
    file.write(input("Please key in intended message"))
    
#6. Run command.txt file:
with open('commands.txt') as f:
    text = f.read()
os.system(text)

#7. Save new file content (commit) created:
message = input("Please key in the message you will like to display: ")
os.system(f"git commit -m '{message}'")

#8. Check if all is in order before "pushing" to Github:
os.system(f"git log")