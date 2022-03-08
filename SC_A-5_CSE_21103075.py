#QUESTION1

from tkinter import*
import tkinter
def find_gst():
    og_cost=int(og_priceField.get())
    net_cost=int(net_priceField.get())
    gst_rate=((net_cost - og_cost) * 100) / og_cost
    print("the original cost is: ",og_cost)
    print("the net cost is : ",net_cost)
    print("the gst rate is : ",gst_rate)
    gst_rateField.insert(12, str(gst_rate) + "%")

# Clearing all the enteries
def clear_all():
    og_priceField.delete(0,END)
    net_priceField.delete(0,END)
    gst_rateField.delete(0,END)

# Driver code
win= Tk()
win.configure(background='lime')
win.geometry('500x500')
win.title("****GST RATE FINDER****")
lbl_1=Label(win,text='Enter Original Price',bg='gold',relief='ridge',padx=3,pady=3,bd=3,font=('arial',14,'bold','underline'))
lbl_1.grid(row=1,column=1,padx=10,pady=10)
lbl_2=Label(win,text="Enter Net Price",bg='gold',relief='ridge',padx=3,pady=3,bd=3,font=('arial',14,'bold','underline'))
lbl_2.grid(row=2,column=1,padx=10,pady=10)
but_1=Button(win,text="Calculate",padx=3,pady=3,bg='light grey',relief='sunken',bd=3,font=('arial',14),command=find_gst,activebackground='red')
but_1.grid(row=3,column=2,padx=10,pady=10)
lbl_3=Label(win,text="GST RATE IS",bg='gold',relief='ridge',padx=3,pady=3,bd=3,font=('arial',14,'bold','underline'))
lbl_3.grid(row=4,column=1,padx=10,pady=10)
but_2=Button(win,text="Clear",padx=3,pady=3,bg='light grey',relief='sunken',bd=3,font=('arial',14),command=clear_all,activebackground='red')
but_2.grid(row=5,column=2,padx=10,pady=10)
og_priceField=Entry(win)
og_priceField.grid(row=1,column=2,padx=10,pady=10)
net_priceField=Entry(win)
net_priceField.grid(row=2,column=2,padx=10,pady=10)
gst_rateField=Entry(win)
gst_rateField.grid(row=4,column=2,padx=10,pady=10)
win.mainloop()


#QUESTION2

from tkinter import *
import calendar
# Function for showing the calendar of the given year
def showCal() :

	# Create a GUI window
	new_gui = Tk()
	
	# Set the background colour of GUI window
	new_gui.configure(background = "white")

	# set the name of tkinter GUI window
	new_gui.title("CALENDAR")

	# Set the configuration of GUI window
	new_gui.geometry("500x500")

	# get method returns current text as string
	fetch_year = int(year_field.get())
	cal_content = calendar.calendar(fetch_year)

	# Creating a label to show the contents of the calendar
	cal_year = Label(new_gui, text = cal_content, font = "Consolas 10 bold")
	cal_year.grid(row = 5, column = 1, padx = 20)
	
	# start the GUI
	new_gui.mainloop()

	
# Driver Code
if __name__ == "__main__" :

	gui = Tk()
	
	# Set the background colour of GUI window
	gui.config(background = "aqua")

	# set the name of tkinter GUI window
	gui.title("CALENDAR")

	# Set the configuration of GUI window
	gui.geometry("600x400")

	# Create a CALENDAR : label with specified font and size
	cal = Label(gui, text = "CALENDAR", bg = "gold",font = ("times", 40, 'bold'),padx=5,pady=5)
    

	# Create a Enter Year : label
	year = Label(gui, text = "Enter Year:", bg = "lime",font = ("helvetica", 10, 'underline'),padx=5,pady=5)
	
	# Create a text entry box for filling or typing the information.
	year_field = Entry(gui)

	# Create a Show Calendar Button and attached to showCal function
	Show = Button(gui, text = "Show Calendar", fg = "Black",bg = "dimgray", command = showCal)

	# Create a Exit Button and attached to exit function
	Exit = Button(gui, text = "Exit", fg = "Black", bg = "dimgray", command = exit)
	
	# grid method is used for placing
	# the widgets at respective positions
	# in table like structure.
	cal.grid(row = 1, column = 1,padx=140,pady=10)

	year.grid(row = 2, column = 1,padx=140,pady=0)

	year_field.grid(row = 3, column = 1,pady=5)

	Show.grid(row = 4, column = 1)

	Exit.grid(row = 6, column = 1)
	
	# start the GUI
	gui.mainloop()
 
 
#QUESTION 3

from cgitb import text
from tkinter import *
expression = ""

# Function to update expression
# in the text entry box
def press(num):
	global expression
	expression = expression + str(num)
	equation.set(expression)

# Function to evaluate the final expression
def equalpress():
	# Try and except statement is used
	try:
		global expression
		# eval function evaluate the expression
		# and str function convert the result
		# into string
		total = str(eval(expression))

		equation.set(total)
		expression = ""
	# if error is generate then handle
	# by the except block
	except:
		equation.set(" error ")
		expression = ""
# Function to clear the contents
# of text entry box
def clear():
	global expression
	expression = ""
	equation.set("")

# Driver code
if __name__ == "__main__":
	gui = Tk()
	gui.configure(background="dimgray")
	gui.title("****Simple Calculator****")
	gui.geometry("320x300")
	equation = StringVar()
	expression_field = Entry(gui, textvariable=equation,bg='snow')
	expression_field.grid(columnspan=20, ipadx=70)
	button1 = Button(gui, text=' 1 ', fg='snow', bg='black',
					command=lambda: press(1), height=1, width=7)
	button1.grid(row=2, column=0,padx=10,pady=10)

	button2 = Button(gui, text=' 2 ', fg='snow', bg='black',
					command=lambda: press(2), height=1, width=7)
	button2.grid(row=2, column=1,padx=10,pady=10)

	button3 = Button(gui, text=' 3 ', fg='snow', bg='black',
					command=lambda: press(3), height=1, width=7)
	button3.grid(row=2, column=2,padx=10,pady=10)

	button4 = Button(gui, text=' 4 ', fg='snow', bg='black',
					command=lambda: press(4), height=1, width=7)
	button4.grid(row=3, column=0,padx=10,pady=10)

	button5 = Button(gui, text=' 5 ', fg='snow', bg='black',
					command=lambda: press(5), height=1, width=7)
	button5.grid(row=3, column=1,padx=10,pady=10)

	button6 = Button(gui, text=' 6 ', fg='snow', bg='black',
					command=lambda: press(6), height=1, width=7)
	button6.grid(row=3, column=2,padx=10,pady=10)

	button7 = Button(gui, text=' 7 ', fg='snow', bg='black',
					command=lambda: press(7), height=1, width=7)
	button7.grid(row=4, column=0,padx=10,pady=10)

	button8 = Button(gui, text=' 8 ', fg='snow', bg='black',
					command=lambda: press(8), height=1, width=7)
	button8.grid(row=4, column=1,padx=10,pady=10)

	button9 = Button(gui, text=' 9 ', fg='snow', bg='black',
					command=lambda: press(9), height=1, width=7)
	button9.grid(row=4, column=2,padx=10,pady=10)

	button0 = Button(gui, text=' 0 ', fg='snow', bg='black',
					command=lambda: press(0), height=1, width=7)
	button0.grid(row=5, column=0,padx=10,pady=10)

	plus = Button(gui, text=' + ', fg='snow', bg='black',
				command=lambda: press("+"), height=1, width=7)
	plus.grid(row=2, column=3,padx=10,pady=10)

	minus = Button(gui, text=' - ', fg='snow', bg='black',
				command=lambda: press("-"), height=1, width=7)
	minus.grid(row=3, column=3,padx=10,pady=10)

	multiply = Button(gui, text=' * ', fg='snow', bg='black',
					command=lambda: press("*"), height=1, width=7)
	multiply.grid(row=4, column=3,padx=10,pady=10)

	divide = Button(gui, text=' / ', fg='snow', bg='black',
					command=lambda: press("/"), height=1, width=7)
	divide.grid(row=5, column=3,padx=10,pady=10)

	equal = Button(gui, text=' = ', fg='snow', bg='black',
				command=equalpress, height=1, width=7)
	equal.grid(row=5, column=2,padx=10,pady=10)

	clear = Button(gui, text='Clear', fg='snow', bg='black',
				command=clear, height=1, width=7)
	clear.grid(row=5, column='1',padx=10,pady=10)

	Decimal= Button(gui, text='.', fg='snow', bg='black',
					command=lambda: press('.'), height=1, width=7)
	Decimal.grid(row=6, column=0)
	# Starting the GUI
	gui.mainloop()


#QUESTION4

def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


n = int(input())
li = list(map(int, input().strip().split()))
quickSort(li, 0, n - 1)
print("Sorted array is: ", li)
print("\n\n")


#QUESTION5

n = int(input())
li = list(map(int, input().strip().split()))

# a-part

li.sort()
print("Sorted array is:", li)

# b-part

flag = False
low = 0
high = n
count = 0
ind = -1
to_find = int(input())
while(low < high):
    mid = low + (high - low) // 2
    if(int(li[mid]) == to_find):
        flag = True
        ind = mid
        print("Value is at index:", mid)
        break
    elif li[mid] > to_find:
        high = mid - 1
    else:
        low = mid + 1
if flag == False:
    print("Error")

# c-part

if(ind == -1):
    print("No element\n")
else:
    i = mid
    j = mid
    count = 0
    for k in range(0, max(i, n - j)):
        if(i >= 0 and li[i] == to_find):
            count += 1
            i -= 1
        if(j < n and li[j] == to_find):
            count += 1
            j += 1
    print("Total number of occurances is:", count - 1)