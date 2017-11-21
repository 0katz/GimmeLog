import sys
import re 
import os 
from argparse import ArgumentParser

def menu():
    line1 = "\nApache Log Analyser - Main Menu"
    print(line1)
    for letter in line1: #for each word in the variable print = end = '' will print it horizontally
        print('=',end ='')
    print("\n1) Successful Requests\n2) Failed Requests\nq) Quit")
    choice = input("Select an option [1-2] q to quit: ")
    
    if choice == "1":
        succes_menu()
    if choice == "2":
        fail_menu()
    if choice == "q":
        print("GoodBye!")
        exit
    #if __name__ == "__main__": handles the "else" 
        
def loadFiles():
    access_0 = open('access_log','r') # read file 
    line_0 = access_0.readlines() #readlines() reads the text line per line and converts it into a list
    access_0.close() # in order to work with files you need to close them. 
    return line_0 # returns the contents of the file.
    
    access_1 = open('access_log.1','r')  
    line_1 = access_1.readlines() 
    access_1.close()
    return line_1 
     
    access_2 = open('access_log.2','r') 
    line_2 = access_2.readlines()
    access_2.close()    
    return line_2 
    
    access_3 = open('access_log.3','r')
    line_3 = access_3.readlines()   
    access_3.close()  
    return line_3

######################## Successful #######################  
      
def succes_menu():
    
    line1 = "\nApache Log Analyser - Successful Requests Menu\n"
    print(line1)
    for letter in line1: #for each word in the variable print =  end = '' will print it horizontally
        print('=',end='')      
    print("\n1) How many total requests (Code 200)\n2) How many requests from Seneca (IPs starting with 142.204)\n3) How many requests for isomaster-1.3.13.tar.bz2\nq) Return to Main Menu\n")
    
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
    load = loadFiles()   # Calls the function loadFiles and stores it in memory for that function and stores it into a variable. 
    counter = 0 # set a counter to 0 
    for line in load: #for each line in load if the " 200 " is found add 1 to the counter and repeat until done. 
       if re.findall(r"\s\b200\b\s", line):
           counter += 1
    print("\nTotal of (Status Code) 200 request:", counter)

def senIP():
    load = loadFiles()
    counter = 0 
    for line in load:
        if re.findall(r"\b142.204\b", line):
            counter += 1
    print("\nTotal of Requests from 142.204:",counter)
    
def isoMaster():
    load = loadFiles()
    counter = 0 #creates a counter to increment from starting from 0
    for line in load:
        if re.findall(r"\bisomaster-1.3.13.tar.bz2\b", line): #finds all the requests that contain what is inside \b \b it will not look further to the rest of strings.
            counter += 1 #increment counter by one each time the condition is met. 
    print("\nTotal requests to isomaster-1.3.13.tar.bz2:",counter)
    
######################## Successful ####################### 

def fail_menu():
    line1 = "Apache Log Analyser - Failed Requests Menu"
    print(line1)
    for letter in line1:
        print('=',end='')
    print("\n1) How many total failed requests (Codes 404, 400, 500, 403, 405, 408, 416)\n2) How many invalid requests for wp-login.php\n3) List the filenames for failed requests for files in /apng/assembler/data\nq) Return to Main Menu\n")
    
    choice = input("Select an option [1-3] q to go back:")
    if choice == "1":
        failed_Request()
    if choice == "2":
        invalid_WP()
    if choice == "3":
        invalid_Apng()
    if choice == "q":
        menu()
    else: 
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
    
    print("\n=====================================")
    print("Total 404 request: ", counter_404)
    print("Total 400 request: ", counter_400)    
    print("Total 500 request: ", counter_500)
    print("Total 403 request: ", counter_403)
    print("Total 405 request: ", counter_405)
    print("Total 408 request: ", counter_408)
    print("Total 416 request: ", counter_416)
    print("=====================================\n")

   
    
def invalid_WP():
    load = loadFiles()
    counter = 0 #Start a counter at 0 
    for line in load:  # loop through each line in the files
        #check if regex is matched () = groups # . = Any number of matches
        #.* = any number of anything \s = space \bword\b = search word only avoids wording or words  
        if re.findall(r'(./wp-login.php).*(\s\b404\b\s)', line): 
            counter += 1 # add one to the counter if the match exist.             
    print("\nTotal failed requests to wp-login.php: ", counter, "\n")

def invalid_Apng():
    load = loadFiles()
    counter = 0 #Start a counter at 0 
    for line in load:  # loop through each line in the files
        #check if regex is matched () = groups # . = Any number of matches
        #.* = any number of anything \s = space \bword\b = search word only avoids wording or words  
        if re.findall(r'(./apng/assembler/data).*(\s\b404\b\s)', line): 
            counter += 1 # add one to the counter if the match exist.             
    print("\nTotal failed requests to /apng/assembler/data: ", counter, "\n")
    
def main():
        
    parser = ArgumentParser()
    parser.add_argument("-d", "--default", dest="myFile", help="Open specified file")
    args = parser.parse_args()
    myFile = args.myFile
    
    if myFile:
        text = open(myFile)
        counter = 0 # set a counter to 0 
        for line in text: #for each line in text if the " 200 " is found add 1 to the counter and repeat until done. 
            if re.findall(r"\s\b200\b\s", line):
                counter += 1
        print("\nTotal of (Status Code) 200 request:", counter, "\n")
    else:
        menu()

if __name__ == "__main__":
    main()
    
    
