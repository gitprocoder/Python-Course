import os
directory_path = "."
try:
    contents = os.listdir(directory_path)
    print(f"Contents of '{directory_path}':\n")
    
    for item in contents:
        print(item)

except FileNotFoundError:
    print("The specified directory does not exist.")
except PermissionError:
    print("You do not have permission to access this directory.")
