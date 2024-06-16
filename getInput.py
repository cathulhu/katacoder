import readchar
import os
import ast
import signal

string = "some text"
command = ""
list = [1,3,5,2]
timeout = 1
valid = False
command=""

def print_status():
    os.system("clear")
    print("data:" , list, "         valid?  ", valid)
    print("command: ", command)
    


def hanlde(signum, stack):
    global valid
    try:
        ast.parse(command)
        valid = True
        
        try: 
            exec(command)
            print_status()
        except:
            pass
    except(SyntaxError) as err:
        valid = False
        print_status()
        pass
        

while True:
    signal.signal(signal.SIGALRM, hanlde)
    signal.alarm(timeout)
    key = readchar.readkey()
    if key == '\x7f':
        command = command[:-1]
    else:
        if key.isascii:
            command += key
    #tree = ast.parse(command)
    #print(command)
    print_status()

