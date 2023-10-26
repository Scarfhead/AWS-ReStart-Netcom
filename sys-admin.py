import os
import subprocess
import re

def new_user():
    confirm = "N"
    while confirm != "Y":
        username = input("Enter the name of the user to add: ")
        print("Use the username '" + username + "'? (Y/N)")
        confirm = input().upper()
    os.system("sudo adduser " + username)

def remove_user():
    confirm = "N"
    while confirm != "Y":
        username = input("Enter the name of the user to remove: ")
        print("Remove the user : '" + username + "'? (Y/N)")
        confirm = input().upper()
    os.system("sudo juserdel -r " + username) 

def install_or_remove_packages():
    iOrR = ""
    while iOrR != "I" and iOrR != "R":
        print("Would you like to install or remove packages? (I/R)")
        iOrR= input().upper()
    if iOrR == "I":
        iOrR= "install"
    elif iOrR == "R":
        iOrR= "remove"
    
def add_user_to_group():
    username = input("Enter the name of the user that you want to add to agroup: ")
    output = subprocess.Popen("groups", stdout=subprocess.PIPE).communicate()[0]
    print("Enter a list of groups to add the user to")
    print("The list should be separatedby spaces, for example:\r\ngroup1 group2 group3")
    print("The available groups are:\r\n ")
    print(output)
    chosenGroups = input("Groups: ")
    output = output.split(" ")
    chosenGroups = chosenGroups.split(" ")
    print("Add To:")
    found = True
    groupString = ""
    for grp in chosenGroups:
        for existingGrp in output:
            if grp == existingGrp:
                found = True
                print("-Existing Group : " + grp)
                groupString= groupString + grp + ","
        if found == False:
            print("-New Group : " + grp)
            groupString = groupString + grp + ","
        else:
            found = False
            #I'm unsure from here
            groupString = groupString[:-1] + " "
            confirm = ""
            while confirm != "Y" and confirm != "N" :
                print("Add user '" + username + "' to thesegroups? (Y/N)")
                confirm = input().upper()
                if confirm == "N":
                    print("User '" + username + "' not added")
                elif confirm == "Y":
                    os.system("sudo usermod -aG " + groupString + username)
                    print("User '" + username + "added")

