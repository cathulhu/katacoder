import readchar
import os
import ast
import signal

#what if instead we structure the program the following way:

# have a stack of operations to be run, each time the user pushes enter they commit the current opereation to the stack
# live typing shows a preview of what the latest operation would do
# can use arrow keys to move through the stack and enable/disable, reorder, or remove them
# after users modify the state of the stack the code re-runs in the new correct order
# code should check if the new changes break things and show where / how
# maybe later incorperate live preview of how changes to the stack effect the rest of the stack

# current thing I'm working on right now is to get run command as its typed afer typing timeout

def addTest():
    return 4

def main():

    data_stack = ["test"]
    command_stack = []
    command = ""
    temp = ""
    keybuffer = ""

    preview_timeout = 1
    command_valid = False
    stack_valid = False

    while True:
        keybuffer = readchar.readkey()
        if keybuffer == '\x7f' and len(command) > 0:
            command = command[:-1]
        elif keybuffer == '\n':
            command_stack.append(command)
            command = ""
        elif keybuffer.isascii():
            command += keybuffer

        try:
            #eval(command)

            for operation in command_stack:
                temp = data_stack[-1]
                print("to be run: ",f"temp = temp{command_stack[-1]}")
                exec(f"temp = temp{command_stack[-1]}")
                data_stack[:-1] = temp

            os.system("clear")
            print(command)

        except:
            pass



        

#main()



# string = "some text"
# command = ""
# list = [1,3,5,2]
# timeout = 1
# valid = False
# command=""

# def print_status():
#     os.system("clear")
#     print("data:" , list, "         valid?  ", valid)
#     print("command: ", command)
    


# def hanlde(signum, stack):
#     global valid
#     try:
#         ast.parse(command)
#         valid = True
        
#         try: 
#             exec(command)
#             print_status()
#         except:
#             pass
#     except(SyntaxError) as err:
#         valid = False
#         print_status()
#         pass
        

# while True:
#     signal.signal(signal.SIGALRM, hanlde)
#     signal.alarm(timeout)
#     key = readchar.readkey()
#     if key == '\x7f':
#         command = command[:-1]
#     else:
#         if key.isascii:
#             command += key
#     #tree = ast.parse(command)
#     #print(command)
#     print_status()

