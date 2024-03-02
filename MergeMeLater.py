from tkinter import *
from tkPDFViewer import tkPDFViewer as pdf 

tk = Tk()
tk.geometry('800x600+40+40')

##################################################################################################################################<
#this section handles the creation and display of 'Listbox' and its content
#create a Listbox
selectExercise = Listbox(tk, width=30, cursor="hand1")
selectExercise.grid(row=0, column=0)

#add item to Listbox
temp = open("YOUR_FILE_PATH_BECAUSE_I_WONT_SHOW_MINE\module-info.txt").readlines()
mylist = [line[:-1] for line in temp]

#insert all elements from 'mylsit' into 'selectExercise'
for item in mylist:
    selectExercise.insert(END, item)
##################################################################################################################################>



##################################################################################################################################<
#this section creates the 'infoFrame' and acesses file data and processes it to be ready to use

displayCurrentSelectionFrame = LabelFrame(tk, text="Current selection", padx=5, pady=5, labelanchor='nw')
displayCurrentSelectionFrame.grid(row=1, column=0,sticky='nw')


#create a displayCurrentSelectionLabel
displayCurrentSelection = Label(displayCurrentSelectionFrame, text='None slected')
displayCurrentSelection.grid(row=1, column=0, sticky='n')

#create infoFrame
infoFrame = LabelFrame(tk, text="Description", padx=5, pady=5, background='green', labelanchor='nw')
infoFrame.grid(row=0, column=1,sticky='n')

#create variable Info from file and match it to the curent selection
temp2 = open("YOUR_FILE_PATH_BECAUSE_I_WONT_SHOW_MINE\moduleDescription.txt").readlines()
DescriptionInfo = [line[:-1] for line in temp2]

#create the info label
InfoLabel = Label(infoFrame, text='DescriptionInfo', width=30, height=5, anchor='w', wraplength=200)
InfoLabel.grid(sticky='n', row=0, column=0)

##################################################################################################################################>



#get current selection
def clickEvent(s):
    displayCurrentSelection.config(text='Nr. ' + str(selectExercise.curselection()[0]))
    InfoLabel.config(text = DescriptionInfo[int(selectExercise.curselection()[0])])

#at selection execute a function on selection from 'selectExercise'
selectExercise.bind("<<ListboxSelect>>", clickEvent)



##################################################################################################################################<
#this section creates the UI of the frame 'Generator settings'

#create a GenFrame
GenFrame = LabelFrame(tk, text="Generator settings", padx=5, pady=5, labelanchor='nw')
GenFrame.grid(row=1, column=1,sticky='nw')

#create a PageCountLabel
PageCountLabel = Label(GenFrame, text='Page count: ', width=12, anchor='w')
PageCountLabel.grid(row=0, column=0, sticky='w')

#create a PageCountTextbox
PageCount = Text(GenFrame, width=4, height=1)
PageCount.grid(row=0, column=1, sticky='w')

#create a RowCountLabel
RowCountLabel = Label(GenFrame, text='rows: ', width=12, anchor='w')
RowCountLabel.grid(row=1, column=0, sticky='w')

#create a RowCountTextbox
RowCount = Text(GenFrame, width=4, height=1)
RowCount.grid(row=1, column=1, sticky='w')

#create a ColumnCountLabel
ColumnCountLabel = Label(GenFrame, text='columns: ', width=12, anchor='w')
ColumnCountLabel.grid(row=1, column=2, sticky='w')

#create a ColumnCount
ColumnCount = Text(GenFrame, width=4, height=1)
ColumnCount.grid(row=1, column=3, sticky='w')

#create a RowCountLabel
lowestNumLabel = Label(GenFrame, text='lowest number: ', width=12, anchor='w')
lowestNumLabel.grid(row=2, column=0, sticky='w')

#create a RowCountTextbox
lowestNum = Text(GenFrame, width=4, height=1)
lowestNum.grid(row=2, column=1, sticky='w')

#create a ColumnCountLabel
highestNumLabel = Label(GenFrame, text='highest number: ', width=12, anchor='w')
highestNumLabel.grid(row=2, column=2, sticky='w')

#create a ColumnCount
highestNum = Text(GenFrame, width=4, height=1)
highestNum.grid(row=2, column=3, sticky='w')

#create a Label for printCheck
printToggleLabel = Label(GenFrame, text='Print?', anchor='w')
printToggleLabel.grid(row=3, column=0, sticky='w')

#create printToggle
printToggle = Checkbutton(GenFrame, onvalue=1, offvalue=0, anchor='w')
printToggle.grid(row=3, column=1, sticky='w')

#create a ColumnCountLabel
pintPageCountLabel = Label(GenFrame, text='Number of copies: ', anchor='w')
pintPageCountLabel.grid(row=3, column=2, sticky='w')

#create a ColumnCount
pintPageCount = Text(GenFrame, width=4, height=1)
pintPageCount.grid(row=3, column=3, sticky='w')


##################################################################################################################################>
#button for GenNow
GenNow = Button(tk, text='Click to generate exercise', anchor='w')
GenNow.grid(row=3, column=1, sticky='w')


##################################################################################################################################<
# this section is dedicated for the management of the PDFViewer

v1 = pdf.ShowPdf() 
  
# Adding pdf location and width and height. 
v2 = v1.pdf_view(tk, pdf_location = r"YOUR_FILE_PATH_BECAUSE_I_WONT_SHOW_MINE/product.pdf", width = 50, height = 100, bar=False) 
  
# Placing Pdf in my gui. 
v2.grid() 

##################################################################################################################################>




tk.mainloop()