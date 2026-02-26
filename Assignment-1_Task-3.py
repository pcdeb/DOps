#file operations

import os

def write_to_file(file_name):
    with open(file_name,"+at") as f:
        f.write("\nNew content is being written")



if os.path.exists("demofile.txt"):
    write_to_file("demofile.txt")

else: 
    with open("demofile.txt","+x") as f:
        f.write("Created a new file")

    
f = open("demofile.txt","+r")
print(f.read())

f.close()
