import readchar
import os
import ast
import signal
from rich import inspect
from rich.console import Console
from rich.color import Color
from rich.columns import Columns
from rich.panel import Panel
from rich.markdown import Markdown

# Rich library text and tui examples
# console.print("hi")
# inspect("hello", methods=True)
# res = console.input(">>>")
# console.print(console.export_text())
#dataPanel3 = Panel.fit(Columns([dataPanel, dataPanel2]), title="3")

def main():

    def convertStackToString(stack):
        stack_string = ""
        for x in stack:
            stack_string += str(x) + "\n"
        return stack_string

    def tryOperation(command, data):
        try:
            result = eval(f"data{command}")
            return (data, result)
        except:
            return False

    commandBuffer = ""
    dataBuffer = ""
    command_stack = []
    data_stack = ["hello darling"]
    output_stack = []
    cursorPosition = [0]
    # vvv part of Rich library for Python
    console = Console(record=True)

    while True:
        os.system("clear")
        commandBuffer = ""
        #hanlde data differently if string vs if list, we want content not a list item for the string
        dataBuffer = data_stack[-1]

        #show the available operations for the current top of stack data item
        inspect(dataBuffer, methods=True)

        # make the data panels for the interface
        dataHistoryPanel = Panel.fit(convertStackToString(data_stack), title="Data History", width=30 )
        commandHistoryPanel = Panel.fit(convertStackToString(command_stack), title="Command History",  width=22)
        lastOutputPanel = Panel.fit(convertStackToString(output_stack), title="Last Output")

        console.print(Columns([dataHistoryPanel, commandHistoryPanel, lastOutputPanel], align="right", title="col title", column_first=False, padding=1))
        
        # get input then check if that's a legit operation
        commandBuffer = console.input(">>> ")
        newData = tryOperation(commandBuffer, dataBuffer)
        originalData = newData[0]
        returnedData = newData[1]
        if newData:
            #for now if its a string we are assuming its return we want, vs side effect result
            if isinstance(originalData, str):
                data_stack.append(returnedData)
            else:
                data_stack.append(originalData)

            command_stack.append(commandBuffer)
            output_stack.append(returnedData)



main()
    

# def main():

#     def printCommandAndCursor(commandBuffer):
#         os.system("clear")
#         print(commandBuffer)
#         for x in range(0,cursorPosition[0]):
#             print(" ", end="")
#         print("-")

#     def getInput():
#         return readchar.readkey()

#     def processInput(commandBuffer, keypress, cursorPosition):
#         # handle spaces
#         if keypress == " " and commandBuffer[cursorPosition[0]].isalpha:
#             commandBuffer = commandBuffer[:cursorPosition[0]] + " " + commandBuffer[cursorPosition[0]:]
#             printCommandAndCursor(commandBuffer)
#         # delete key
#         if keypress == '\x7f' and len(commandBuffer) > 0:
#             if cursorPosition[0] == len(commandBuffer):
#                 commandBuffer = commandBuffer[:-1]
#                 cursorPosition[0] -= 1
#                 printCommandAndCursor(commandBuffer)
#             else:
#                 cursorPosition[0] -= 1
#                 commandBuffer = commandBuffer[:cursorPosition[0]+1] + "" + commandBuffer[cursorPosition[0] + 2:]
#                 printCommandAndCursor(commandBuffer)
#         # enter key, so try to add to stack
#         elif keypress == '\n':
#             print(" ")
#             #TODO send to validation for stack adding
#             return ""
#         # move cursor right
#         elif keypress == "\x1b[C" and cursorPosition[0] < len(commandBuffer):
#             cursorPosition[0] += 1
#             printCommandAndCursor(commandBuffer)
#         # don't let cursor move right if already at right
#         elif keypress == "\x1b[C" and cursorPosition[0] == len(commandBuffer):
#             printCommandAndCursor(commandBuffer)
#         # move cursor left
#         elif keypress == "\x1b[D" and cursorPosition[0] > 0:
#             cursorPosition[0] -= 1
#             printCommandAndCursor(commandBuffer)
#         # don't let cursor move left if already at left
#         elif keypress == "\x1b[D" and cursorPosition[0] == 0:
#             printCommandAndCursor(commandBuffer)
#         # otherwise if normal ascii character
#         elif keypress.isascii():
#             #commandBuffer += keypress
#             commandBuffer = commandBuffer[:cursorPosition[0]] + keypress + commandBuffer[cursorPosition[0] + 1:]
#             if len(commandBuffer) == cursorPosition[0] + 1:
#                 cursorPosition[0] += 1
#                 printCommandAndCursor(commandBuffer)
#             else:
#                 printCommandAndCursor(commandBuffer)

#         # TODO have something that looks for up and down key to control which thing in stack is selected
#         return commandBuffer


#     commandBuffer = ""
#     command_stack = []
#     data_stack = ["test"]
#     cursorPosition = [0]
#     insertMode = False

#     preview_timeout = 1
#     command_valid = False
#     stack_valid = False

#     while True:
#         commandBuffer = processInput(commandBuffer, getInput(), cursorPosition)










    # while True:
       
    #     try:
    #         #eval(command)

    #         for operation in command_stack:
    #             temp = data_stack[-1]
    #             print("to be run: ",f"temp = temp{command_stack[-1]}")
    #             exec(f"temp = temp{command_stack[-1]}")
    #             data_stack[:-1] = temp

    #         os.system("clear")
    #         print(command)

    #     except:
    #         pass



        





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






# what if instead we structure the program the following way:

# have a stack of operations to be run, each time the user pushes enter they commit the current opereation to the stack
# live typing shows a preview of what the latest operation would do
# can use arrow keys to move through the stack and enable/disable, reorder, or remove them
# after users modify the state of the stack the code re-runs in the new correct order
# code should check if the new changes break things and show where / how
# maybe later incorperate live preview of how changes to the stack effect the rest of the stack

# current thing I'm working on right now is to get run command as its typed afer typing timeout
