from termcolor import cprint
from fpdf import FPDF
#from tkinter import *

from addition import *
from additionAlt import *
from subtraction import *
from subtractionAlt import *
from multiplication import *
from division import *

#declare defaults
lowestnum = 2
highestnum = 11
cycles = 30
columns = 2

#ask to use defaults
cprint("the defaults are: lowest number of " + str(lowestnum) + ", highest number of " + str(highestnum-1) + " and " + str(cycles) + " row(s) as well as " + str(columns) + " column(s)", "white", attrs=["bold"])
cprint("do you want to use these defaults? y/n" , "white", attrs=["bold"])
selection = input("")

# selection
if selection == '' or selection == 'y' or selection == 'yes':
    pass
else:
    cprint("do you want to use previous settings? y/n" , "white", attrs=["bold"])
    selection = input("")
    if selection == '' or selection == 'y' or selection == 'yes':
        # read from file
        # and load the values
        raw = open("settings.txt", mode = "r")
        r = raw.readline()
        settings = r.split("/")
        lowestnum = int(settings[0])
        highestnum = int(settings[1])
        cycles = int(settings[2])
        columns = int(settings[3])

        pass
    else:
        # get custom values
        lowestnum = int(input("lowest number? "))
        highestnum = int(input("highest number? "))
        cycles = int(input("rows? "))
        columns = int(input("columns? "))

#write settings to file
with open("settings.txt", mode = "w") as f:
    f.write( str(lowestnum) + "/" + str(highestnum) + "/" + str(cycles) + "/" + str(columns))

#ask what operation to perform
cprint("select one of the following exercises by entering the corresponding number: " , "white", attrs=["bold"])

#Layout ('P', 'L')
#Unit ('mm', 'cm', 'in')
#format ('A3', 'A4' (total with of 210 => 105), 'A5', 'Letter', 'Legal', (x1,x2))
pdf = FPDF('P', 'mm', 'A4')

#add page
pdf.add_page()

#font ('times', 'courier', ...)
#fontstyle ('B' (bold), 'I' (italic), 'U' (underline), ''(regular), 'BU' (2 combined))
pdf.set_font('times', '', 16)

#print available modules
info = open("module-info.txt", "r")
for line in info:
    print(line)

#filter the selection and exectute appropriate file
cprint("your selection: " , "white", attrs=["bold"])
selectionvar = input("")

try:
    selectionvar = int(selectionvar)
except ValueError:
    print("Not a number, defaulting to 1")
    selectionvar = 1  # the default value

# change mode based on selection
x=0
while x < cycles:
    if selectionvar == 1:
        pdf.cell(105, 8.5, str(addition(lowestnum,highestnum)))
        pdf.cell(105, 8.5, str(addition(lowestnum,highestnum)), ln=1)
    elif selectionvar == 2:
        pdf.cell(105, 8.5, str(subtraction(lowestnum,highestnum)))
        pdf.cell(105, 8.5, str(subtraction(lowestnum,highestnum)), ln=1)
    elif selectionvar == 3:
        pdf.cell(105, 8.5, str(addition(lowestnum,highestnum)))
        pdf.cell(105, 8.5, str(subtraction(lowestnum,highestnum)), ln=1)
    elif selectionvar == 4:
        pdf.cell(105, 8.5, str(multiplication(lowestnum,highestnum)))
        pdf.cell(105, 8.5, str(multiplication(lowestnum,highestnum)), ln=1)
    elif selectionvar == 5:
        pdf.cell(105, 8.5, str(division(lowestnum,highestnum)))
        pdf.cell(105, 8.5, str(division(lowestnum,highestnum)), ln=1)
    elif selectionvar == 6:
        pdf.cell(105, 8.5, str(multiplication(lowestnum,highestnum)))
        pdf.cell(105, 8.5, str(division(lowestnum,highestnum)), ln=1)
    elif selectionvar == 7:
        pdf.cell(105, 8.5, str(additionAlt(lowestnum,highestnum)))
        pdf.cell(105, 8.5, str(additionAlt(lowestnum,highestnum)), ln=1)
    elif selectionvar == 8:
        pdf.cell(105, 8.5, str(subtractionAlt(lowestnum,highestnum)))
        pdf.cell(105, 8.5, str(subtractionAlt(lowestnum,highestnum)), ln=1)
    x+=1

# save file
pdf.output('product.pdf')

# ending message
cprint("Done! Thank you for using me!" , "green", attrs=["bold"])