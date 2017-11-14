import sys
import re 
import os 
from argparse import ArgumentParser


############# THE FUNCTION MAIN DOESN'T Work up here because the other functions need be lodead first. #########################

                
def menu():
    line1 = "Apache Log Analyser - Main Menu"
    print(line1)
#for each word in the variable print = 
#end = '' will print it horizontally
    for letter in line1:
        print('=',end='')
    print("\n1) Successful Requests\n2) Failed Requests\nq) Quit")
    choice = input("Select an option [1-2] q to quit: ")
    
    if choice == "1":
        succes_menu()
    if choice == "2":
        fail_menu()
    if choice == "q":
        print("GoodBye!")
        exit
    else:
        menu()
        
def loadFiles():
    access_0 = open('access_log','r') # read file 
    line_0 = access_0.readlines() #readlines() reads the text line per line and converts it into a list
    access_0.close() # in order to work with files you need to close them. 
    return line_0 # returns the contents of the file.
    
    access_1 = open('access_log.1','r') # read file 
    line_1 = access_1.readlines() #readlines() reads the text line per line and converts it into a list
    access_1.close() # in order to work with files you need to close them.
    return line_1 # returns the contents of the file.
     
    access_2 = open('access_log.2','r') # read file 
    line_2 = access_2.readlines() #readlines() read the text line per line and converts it into a list
    access_2.close()    # in order to work with files you need to close them.
    return line_2 #returns the contents of the file
    
    access_3 = open('access_log.3','r') # read file 
    line_3 = access_3.readlines()   #readlines() read the text line per line and converts it into a list
    access_3.close()    # in order to work with files you need to close them.
    return line_3 # returns the contents of the file. 






######################## Successful #######################  
      
def succes_menu():
    line1 = "Apache Log Analyser - Successful Requests Menu"
#for each word in the variable print = 
#end = '' will print it horizontally
    print(line1)
    for letter in line1:
        print('=',end='')
        
    print("\n1) How many total requests (Code 200)\n2) How many requests from Seneca (IPs starting with 142.204)\n3) How many requests for isomaster-1.3.13.tar.bz2\nq) Return to Main Menu")
    
    choice = input("Select an option [1-3] q to quit:")
    
    if choice == "1":
        total_200()
    if choice == "2":
        senIP()
    if choice == "3":
        isoMaster()
    if choice == "q":
        exit
    else:
        succes_menu()
        
def total_200():
    load = loadFiles()     
    counter = 0 # set a counter to 0 
    for line in load: #for each line in load if the " 200 " is found add 1 to the counter and repeat until done. 
       if re.findall(r"\s\b200\b\s", line):
           counter += 1
    print("Total of (Status Code) 200 request:", counter)

def senIP():
    load = loadFiles()
    counter = 0 
    for line in load:
        if re.findall(r"\b142.204\b", line):
            counter += 1
    print("Total of Requests from 142.204:",counter)
    
def isoMaster():
    load = loadFiles()
    
    counter = 0 
    
    for line in load:
        if re.findall(r"\bisomaster-1.3.13.tar.bz2\b", line):
            counter += 1
    print("Total requests to isomaster-1.3.13.tar.bz2:",counter)
    
######################## Successful ####################### 

def fail_menu():
    line1 = "Apache Log Analyser - Failed Requests Menu"
    print(line1)
    for letter in line1:
        print('=',end='')
    print("\n1) How many total failed requests (Codes 404, 400, 500, 403, 405, 408, 416)\n2) How many invalid requests for wp-login.php\n3) List the filenames for failed requests for files in /apng/assembler/data\nq) Return to Main Menu")
    
    choice = input()
    if choice == "1":
        failed_Request()
    if choice == "2":
        invalid_WP()
    if choice == "3":
        invalid_Apng()
    if choice == "q":
        print("Returning to Main Menu")
        menu()
    else: 
        print("Invalid option")
        fail_menu()

######################## Failed #######################  

def failed_Request():
    load = loadFiles()
    counter_404 = 0
    counter_400 = 0 
    counter_500 = 0 
    counter_403 = 0 
    counter_405 = 0 
    counter_408 = 0 
    counter_416 = 0 
    
    for line in load:
        if re.findall(r"\s\b404\b\s", line):
        #if " 404 " in line:
            counter_404 += 1
        if re.findall(r"\s\b400\b\s", line):
        #if " 400 " in line:
            counter_400 += 1
        if re.findall(r"\s\b500\b\s", line):
        #if " 500 " in line:
            counter_500 += 1
        if re.findall(r"\s\b403\b\s", line):
        #if " 403 " in line:
            counter_403 += 1
        if re.findall(r"\s\b405\b\s", line):
        #if " 405 " in line:
            counter_405 += 1
        if re.findall(r"\s\b408\b\s", line):
        #if " 408 " in line:
            counter_408 += 1
        if re.findall(r"\s\b416\b\s", line):
        #if " 416 " in line: 
            counter_416 += 1
    print("Total 404 request: ", counter_404)
    print("Total 400 request: ", counter_400)    
    print("Total 500 request: ", counter_500)
    print("Total 403 request: ", counter_403)
    print("Total 405 request: ", counter_405)
    print("Total 408 request: ", counter_408)
    print("Total 416 request: ", counter_416)
    
def invalid_WP():
    load = loadFiles()
    counter = 0 #Start a counter at 0 
    for line in load:  # loop through each line in the files
        #check if regex is matched () = groups # . = Any number of matches
        #.* = any number of anything \s = space \bword\b = search word only avoids wording or words  
        if re.findall(r'(./wp-login.php).*(\s\b404\b\s)', line): 
            counter += 1 # add one to the counter if the match exist.             
    print("Total failed requests to wp-login.php: ", counter)

def invalid_Apng():
    load = loadFiles()
    counter = 0 #Start a counter at 0 
    for line in load:  # loop through each line in the files
        #check if regex is matched () = groups # . = Any number of matches
        #.* = any number of anything \s = space \bword\b = search word only avoids wording or words  
        if re.findall(r'(./apng/assembler/data).*(\s\b404\b\s)', line): 
            counter += 1 # add one to the counter if the match exist.             
    print("Total failed requests to /apng/assembler/data: ", counter)
    
    
def main():
        
    parser = ArgumentParser()
    parser.add_argument("-d", "--default", dest="myFile", help="Open specified file")
    args = parser.parse_args()
    myFile = args.myFile
    
    text = open(myFile)
    if len(sys.argv) == 1:
        menu()
        # Length of argument must be greater 2 or else print Usage and exit
    if len(sys.argv) < 2:
        print("Usage: Python3 " + sys.argv[0] + " <filename>")  
        sys.exit()
    if sys.argv[1].startswith('--'):
    # fetch sys.argv[1] but without the first two characters
        option = sys.argv[1][2:]
        if option =='default':
            total_200()
        else:
            print("-ERROR- Usage: " + sys.argv[0] + "--default or -d "+" <file name>")
    elif sys.argv[1].startswith('-'):
    # fetch sys.argv[1] but without the first character
        option = sys.argv[1][1:]
        if option == 'd':
            print("Skip to... How many total requests (Code 200)")            
        else:
            print("-ERROR- Usage: " + sys.argv[0] + "--default or -d "+" <file name>")


if __name__ == "__main__":
    main()
    #menu()
    
