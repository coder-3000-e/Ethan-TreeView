#Ethan Lourens
import pandas as pd #import pandas Library
from tkinter import ttk 
from tkinter import * #import tkinter Library
import csv #import csv Library

#Question 1: Display the contents of the CSV file in tabular format
def Question_1():
    dropDownListDisable() #call the dropDownListDisable() function to disable the dropdownlists
    tree = ttk.Treeview(frameDisplay, columns=('Province','Station','Category','2005-2006','2006-2007' # Create a TreeView to store csv data in
,'2007-2008','2008-2009','2009-2010','2010-2011','2011-2012', #Identify each column and heading in the csv file 
'2012-2013','2013-2014','2014-2015','2015-2016'), show='headings')
    tree.column('Province', minwidth=0, width=450)
    tree.column('Station', minwidth=0, width=450)
    tree.column('Category', minwidth=0, width=450)
    tree.column('2005-2006', minwidth=0, width=450)
    tree.column('2006-2007', minwidth=0, width=450)
    tree.column('2007-2008', minwidth=0, width=450)
    tree.column('2008-2009', minwidth=0, width=450)
    tree.column('2009-2010', minwidth=0, width=450)
    tree.column('2010-2011', minwidth=0, width=450)
    tree.column('2011-2012', minwidth=0, width=450)
    tree.column('2012-2013', minwidth=0, width=450)
    tree.column('2013-2014', minwidth=0, width=450)
    tree.column('2014-2015', minwidth=0, width=450)
    tree.column('2015-2016', minwidth=0, width=450)
    tree.heading('Province', text='Province')
    tree.heading('Station', text='Station')
    tree.heading('Category', text='Category')
    tree.heading('2005-2006', text='2005-2006')
    tree.heading('2006-2007', text='2006-2007')
    tree.heading('2007-2008', text='2007-2008')
    tree.heading('2008-2009', text='2008-2009')
    tree.heading('2009-2010', text='2009-2010')
    tree.heading('2010-2011', text='2010-2011')
    tree.heading('2011-2012', text='2011-2012')
    tree.heading('2012-2013', text='2012-2013')
    tree.heading('2013-2014', text='2013-2014')
    tree.heading('2014-2015', text='2014-2015')
    tree.heading('2015-2016', text='2015-2016')
    vertical_Scrollbar = Scrollbar(frameDisplay, orient="vertical", command=tree.yview) #Create a Vertical scrollbar: This will allow the user to scroll through the data easier
    vertical_Scrollbar.pack(side ='right', fill ='y') #Pack Scrollbar widget

    horizontal_Scrollbar = Scrollbar(frameDisplay, orient="horizontal", command=tree.xview)#Create a Horizontal scrollbar: This will allow the user to scroll through the data easier
    horizontal_Scrollbar.pack(side ='bottom', fill ='x')#Pack Scrollbar widget

    tree.configure(yscrollcommand=vertical_Scrollbar.set, xscrollcommand=horizontal_Scrollbar.set)#Configure the vertical and horizontal scrollbar to work with the treeview created
    for (a,b,c,d,e,f,g,h,i,j,k,l,m,n) in csvreader_list:
        tree.insert('', 'end', values=(a,b,c,d,e,f,g,h,i,j,k,l,m,n)) #Retrieve data from the csv file and insert the data into the rows
    tree.pack()#Pack TreeView widget

#Question 2: Report on the amount of crimes that occurred in a user specified province and period
def Question_2():
    cleardata()#Call the cleardata() function: This will clear the text widget
    dropDownListDisable()#call the dropDownListDisable() function to disable the dropdownlists
    period_dropDownList.configure(state="active")#Activate the Period dropdown list: The user will need to select a period in this function
    province_dropDownList.configure(state="active")#Activate the Province dropdown list: The user will need to select a province in this function
    province = optionListProvince_Var.get()#This will get the province that was selected in the province option menu
    period = optionListP_Var.get()#This will get the period that was selected in the period option menu
    databaseFile = df[["Province", period]][df.Province == province]#Perform a query on the data in the csv file
    total = databaseFile[period].sum()#This function gets the total sum for the specified period 
    output = ("Amount of crimes that occurred in {Province} between {Period} : {Total} crimes".format(Province = province,Period=period,Total=total))#Text for the user to view
    labelText.insert(END, output)#Insert the text into the text widget

#Question 3:Report on the total amount of crimes for a user specified station for period full period of 2004 to 2015
def Question_3():
    cleardata()#Call the cleardata() function: This will clear the text widget
    dropDownListDisable()#call the dropDownListDisable() function to disable the dropdownlists
    station_dropDownList.configure(state="active")
    station = optionListStation_Var.get()#This will get the station that was selected in the station option menu
    databaseFile = df[["Station","2005-2006","2006-2007","2007-2008","2008-2009","2009-2010","2010-2011","2011-2012","2012-2013","2013-2014","2014-2015", "2015-2016"]][df.Station == station]#Perform a query on the data in the csv file
    sum_column = databaseFile["2005-2006"]+databaseFile["2006-2007"]+databaseFile["2007-2008"]+databaseFile["2008-2009"]+databaseFile["2009-2010"]+databaseFile["2010-2011"]+databaseFile["2011-2012"]+databaseFile["2012-2013"]+databaseFile["2013-2014"]+databaseFile["2014-2015"]#This function gets the total amount of crimes for the specified station for the full period
    databaseFile["Total"] = sum_column#Add a new column and store the sum_column value in it
    total = databaseFile["Total"].sum()#Calculate the total sum for the column
    output = ("Amount of crimes at {Station} station for period 2005 to 2016 : {crimes} crimes".format(Station = station,crimes = total))#Text for the user to view
    labelText.insert(END, output)#Insert the text into the text widget

#Question 4: How many incidents involving truck hijacking were reported for the period 2010 - 2011?
def Question_4():
    cleardata()#Call the cleardata() function: This will clear the text widget
    dropDownListDisable()#call the dropDownListDisable() function to disable the dropdownlists
    crime = "Truck hijacking"#Specify the category
    databaseFile = df[["Category", "2010-2011"]][df.Category == crime]#Perform a query on the data in the csv file
    total = databaseFile["2010-2011"].sum()#Calculate the total sum for the column
    output = ("Number of incidents involving truck hijacking reported for the period 2010-2011 : {Total} incidents".format(Total=total))#Text for the user to view
    labelText.insert(END, output)#Insert the text into the text widget

#Question 5: How many “Arson” incidents occurred in Boitekong and Ngodwana in 2009 – 2010?
def Question_5():
    cleardata()#Call the cleardata() function: This will clear the text widget
    dropDownListDisable()#call the dropDownListDisable() function to disable the dropdownlists
    crime = "Arson"
    databaseFile = df[["Station","Category","2009-2010"]][(df.Category == crime) & ((df.Station == "Boitekong")|(df.Station == "Ngodwana"))]#Perform a query on the data in the csv file
    total = databaseFile["2009-2010"].sum()#Calculate the total sum for the column
    output = ("Number of Arson incidents occurred in Boitekong and Ngodwana in 2009 – 2010: {Total} incidents".format(Total=total))#Text for the user to view
    labelText.insert(END, output)#Insert the text into the text widget

#Question 6: Which type of crime had the highest number of incidents in the 2014 – 2015 period?
def Question_6():
    cleardata()#Call the cleardata() function: This will clear the text widget
    dropDownListDisable()#call the dropDownListDisable() function to disable the dropdownlists
    databaseFile = df[["Category","2005-2006"]]#Perform a query on the data in the csv file
    highestCrime = (databaseFile.groupby(["Category"]).sum().sort_values("2005-2006", ascending=False)).reset_index()#Get the highest number of incidents
    highestCrime = highestCrime["Category"].values[0]#Get the first value in the column
    output = ('"{Crime}" had the highest number of incidents in the 2014 – 2015 period'.format(Crime=highestCrime))#Text for the user to view
    labelText.insert(END, output)#Insert the text into the text widget

#Question 7: For which period did Nongoma in KwaZulu Natal have the lowest amount of murder cases?
def Question_7():
    cleardata()#Call the cleardata() function: This will clear the text widget
    dropDownListDisable()#call the dropDownListDisable() function to disable the dropdownlists
    crime = "Murder" #Specify the category
    station = "Nongoma"#Specify the station
    databaseFile = df[["2005-2006",
"2006-2007",
"2007-2008",
"2008-2009",
"2009-2010",
"2010-2011",
"2011-2012",
"2012-2013",
"2013-2014",
"2014-2015",
"2015-2016"]][(df.Station == station)&(df.Category == crime)]#Perform a query on the data in the csv file
    databaseFile["lowestAmount"] = databaseFile.idxmin(axis=1)#Store all the values into a new column
    period = databaseFile["lowestAmount"].values[0]#Get the first period in the column
    output = ("Nongoma in KwaZulu Natal had the lowest amount of murder cases during the following period: {Period}".format(Period=period))#Text for the user to view
    labelText.insert(END, output)#Insert the text into the text widget

#Question 8: Which stations in the North West province has 0 cases for Attempted murder for the period 2008 – 2009?
def Question_8():
    cleardata()#Call the cleardata() function: This will clear the text widget
    dropDownListDisable()#call the dropDownListDisable() function to disable the dropdownlists
    crime = "Attempted murder"#Specify Category
    province = "North West"#Specify Province
    databaseFile = df[["Province","Station","Category","2008-2009"]][(df.Province == province) & (df.Category == crime) & (df["2008-2009"] == 0)]#Perform a query on the data in the csv file
    stationsN = list(databaseFile["Station"].unique())#Avoid duplicates
    stationsN =  ', '.join([str(listVal) for listVal in stationsN])#Join all the province into one string
    output = ("The following stations in the North West province had 0 cases for Attempted murder for the period 2008 – 2009: {stations}".format(stations=stationsN))#Text for the user to view
    labelText.insert(END, output)#Insert the text into the text widget

#Question 10: Which province had the most to the least crimes for a user specified period
def Question_10():
    cleardata()#Call the cleardata() function: This will clear the text widget
    dropDownListDisable()#call the dropDownListDisable() function to disable the dropdownlists
    period_dropDownList.configure(state="active")#Activate the Period dropdown list: The user will need to select a period in this function
    period = optionListP_Var.get()#This will get the period that was selected in the period option menu
    databaseFile = df[["Province",period]]#Perform a query on the data in the csv file
    crimeInProv = (databaseFile.groupby(["Province"]).sum().sort_values(period, ascending=False)).reset_index()#Sort which province had the most crime
    crimeInProv = crimeInProv.applymap(str)#Convert the output into a string
    output = ("Number of crimes that occurred in {Period} \n {crimesProv}").format(Period=period,crimesProv=crimeInProv)#Text for the user to view
    labelText.insert(END, output)#Insert the text into the text widget

#This function clears the text displayed in the text widget
def cleardata():
    labelText.delete("1.0",END)#Clear the text widget

def dropDownListDisable():
    period_dropDownList.configure(state="disabled")#Disable the period option list
    province_dropDownList.configure(state="disabled")#Disable the province option list
    station_dropDownList.configure(state="disabled")#Disable the station option list

root = Tk()#Create root window
root.title("3949753")#Set the title of the window
root.geometry("900x700")#Set the size of the window

filename = (r'SouthAfricaCrimeStats_v2.csv') #Locate the csv file
df = pd.read_csv(filename)#Read the csv file

file = open(filename, 'r')#Open the csv file
csvReader = csv.reader(file,)#Read in all the data in the csv file
csvreader_list = list(csvReader)#Create a list with all the data in the csv file

Button(root, text = 'Display the contents of the CSV file', bd = '5',font=("underline 10 bold"),fg="black",activebackground="red",bg="light blue",width=500, command = lambda: Question_1()).pack(ipady=2,ipadx=5)#Create a button for question 1
Button(root, text = 'Amount of crimes that occurred in a user specified province and period', bd = '5',font=("underline 10 bold"),fg="black",bg="green",activebackground="red",width=500, command = lambda: Question_2()).pack(ipady=2,ipadx=5)#Create a button for question 2
Button(root, text = 'Total amount of crimes for a user specified station for period full period of 2005 to 2016', bd = '5',font=("underline 10 bold"),fg="black",bg="blue",activebackground="red",width=500, command = lambda: Question_3()).pack(ipady=2,ipadx=5)#Create a button for question 3
Button(root, text = 'How many incidents involving truck hijacking were reported for the period 2010 - 2011', bd = '5',font=("underline 10 bold"),fg="black",bg="purple",activebackground="red",width=500, command = lambda: Question_4()).pack(ipady=2,ipadx=5)#Create a button for question 4
Button(root, text = 'How many “Arson” incidents occurred in Boitekong and Ngodwana in 2009 – 2010', bd = '5',font=("underline 10 bold"),fg="black",bg="pink",activebackground="red",width=500, command = lambda: Question_5()).pack(ipady=2,ipadx=5)#Create a button for question 5
Button(root, text = 'Which type of crime had the highest number of incidents in the 2014 – 2015 period', bd = '5',font=("underline 10 bold"),fg="black",bg="gray",activebackground="red",width=500, command = lambda: Question_6()).pack(ipady=2,ipadx=5)#Create a button for question 6
Button(root, text = ' Which period did Nongoma in KwaZulu Natal have the lowest amount of murder cases', bd = '5',font=("underline 10 bold"),fg="black",bg="orange",activebackground="red",width=500, command = lambda: Question_7()).pack(ipady=2,ipadx=5)#Create a button for question 7
Button(root, text = 'Which stations in the North West province has 0 cases for Attempted murder for the period 2008 – 2009', bd = '5',font=("underline 10 bold"),fg="black",bg="yellow",activebackground="red",width=500, command = lambda: Question_8()).pack(ipady=2,ipadx=5)#Create a button for question 8
Button(root, text = 'Which province had the most to the least crimes for a user specified period', bd = '5',font=("underline 10 bold"),fg="black",bg="light green",activebackground="red",width=500, command = lambda: Question_10()).pack(ipady=2,ipadx=5)#Create a button for question 10


frameDisplay = LabelFrame(bg="green", text="CSV Data")#Create a frame to display the csv data in

options_Period = [ #List  the period
"2005-2006",
"2006-2007",
"2007-2008",
"2008-2009",
"2009-2010",
"2010-2011",
"2011-2012",
"2012-2013",
"2013-2014",
"2014-2015",
"2015-2016"
]
#Create a option menu for the user to select a period
optionListP_Var = StringVar(root)
optionListP_Var.set(options_Period[0]) # default value
period_dropDownList = OptionMenu(root, optionListP_Var, *options_Period)
period_dropDownList.configure(fg="white",bg="black",width=50)
#Create a option menu for the user to select a Province
options_Province = df.sort_values("Province",ascending=True)
options_Province = list(df["Province"].unique())
optionListProvince_Var = StringVar(root)
optionListProvince_Var.set(options_Province[0]) # default value
province_dropDownList = OptionMenu(root, optionListProvince_Var, *options_Province)
province_dropDownList.configure(fg="white",bg="black",width=50)
#Create a option menu for the user to select a Station
stationSort = df.sort_values("Station",ascending=True)
values = list(stationSort["Station"].unique())
optionListStation_Var = StringVar(root)
optionListStation_Var.set(values[0]) # default value
station_dropDownList = OptionMenu(root, optionListStation_Var, *values)
station_dropDownList.configure(fg="white",bg="black",width=50)
#Create a Text widget to print the output, aswell a scrollbar to scrolll through the output
labelText = Text(root, height="3", width="100")
verticalScrollbar = Scrollbar(root, orient="vertical", wrap=None,command=labelText.yview)
verticalScrollbar.pack(side ='right', fill ='y')#Pack the vertical scrollbar

period_dropDownList.pack(ipadx=10)#Pack Option Menu widget
province_dropDownList.pack(ipadx=10)#Pack Option Menu widget
station_dropDownList.pack(ipadx=10)#Pack Option Menu widget

labelText.pack(pady=10,ipady=10,ipadx=10)#Pack the text widget
Button(root, text = 'Exit!', bd = '5',font=("underline 12 bold"),fg="white",bg="red",activebackground="red",width=500, command = root.destroy).pack(ipady=1,ipadx=5)#Create an exit button
frameDisplay.pack(fill="both") #Pack frame
dropDownListDisable()#Call the dropDownListDisable() function

root.mainloop()#Run the application