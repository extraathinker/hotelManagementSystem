
from tkinter import *
from tkinter import messagebox
import random

roomDict = {'basic':[101,102,103], 'average':[104,105,106], 'deluxe':[201,202,203],'kingsize':[204,205,206]}
visitorDict = {}
hotelDict = {'unoccupied':[101,102,103,104,105,106,201,202,203,204,205,206], 'occupied':[]}
sum = 0

def launchWelcomeScreen():
    hotel = Tk()
    hotel.geometry('300x350')
    hotel.resizable(False,False)
    hotel.title('Welcome Screen')
    hotelName = Label(hotel, text='Welcome to hotel NAVYA', height= 5, width= 30)
    hotelName.pack()

    def checkIn():
        hotel.destroy()
        checkInForm = Tk()
        checkInForm.geometry('500x400')
        checkInForm.resizable(False,False)
        checkInForm.title('CHECK IN FORM')

        visitorDetails = Label(checkInForm, text='CHECK IN FORM', height= 5, width= 30)
        visitorDetails.pack()

        sex = IntVar()


        detailsframe = Frame(checkInForm)
        detailsframe.pack()

        visitorName = Label(detailsframe, text='Name :', height= 2, width= 30)
        visitorName.grid(row=1, column=1)

        entryName = Entry(detailsframe)
        entryName.grid(row=1, column=2)

        visitorSex = Label(detailsframe, text='Sex', height= 2, width= 30)
        visitorSex.grid(row=2, column=1)

        choiceSexM = Radiobutton(detailsframe, text= 'Male', value=1, variable=sex)
        choiceSexM.grid(row=2, column=2)
        choiceSexF = Radiobutton(detailsframe, text='Female', value=2, variable=sex)
        choiceSexF.grid(row=2, column=3)

        visitorAddress = Label(detailsframe, text='Address :', height= 2, width= 30)
        visitorAddress.grid(row=3, column=1)

        entryAddress = Entry(detailsframe)
        entryAddress.grid(row=3, column=2)

        visitorPhone = Label(detailsframe, text='Phone Number :', height= 2, width= 30)
        visitorPhone.grid(row=4, column=1)

        entryPhone = Entry(detailsframe)
        entryPhone.grid(row=4, column=2)

        visitorEmail = Label(detailsframe, text='email address :', height= 2, width= 30)
        visitorEmail.grid(row=5, column=1)

        entryEmail = Entry(detailsframe)
        entryEmail.grid(row=5, column=2)

        visitorRoom = Label(detailsframe, text='Room Number :', height= 2, width= 30)
        visitorRoom.grid(row=6, column=1)

        room = IntVar()

        roomList1 = Radiobutton(detailsframe, text='basic @ 500', value= 1, variable= room)
        roomList1.grid(row=6, column=2)
        roomList2 = Radiobutton(detailsframe, text='average @ 1000', value= 2, variable= room)
        roomList2.grid(row=6, column=3)
        roomList3 = Radiobutton(detailsframe, text='deluxe @ 1500', value= 3, variable=room)
        roomList3.grid(row=7, column=2)
        roomList4 = Radiobutton(detailsframe, text='kingsize @ 2000', value= 4, variable= room)
        roomList4.grid(row=7, column=3)

        visitorDays = Label(detailsframe, text='Days of Stay :', height= 2, width= 30)
        visitorDays.grid(row=8, column=1)

        entryDays = Entry(detailsframe)
        entryDays.grid(row=8, column=2)

        buttonFrame = Frame(checkInForm)
        buttonFrame.pack()

        def checkInSubmitForm():
            if entryName.get() == '':
                messagebox.showinfo('Error', 'Please enter valid name.')
            elif sex.get() not in [1,2]:
                messagebox.showinfo('Error','Please select any sex.')
            elif entryAddress.get() == '':
                messagebox.showinfo('Error', 'Please enter valid address.')
            elif entryPhone.get() == '':
                messagebox.showinfo('Error', 'Please enter valid phone number.')
            elif entryEmail.get() == '':
                messagebox.showinfo('Error', 'Please enter valid email id.')
            elif room.get() not in [1,2,3,4]:
                messagebox.showinfo('Error','Please select any room category.')
            elif entryDays.get() == '':
                messagebox.showinfo('Error', 'Please enter valid days.')
            else:
                if room.get() == 1:
                    if len(roomDict['basic']) == 0:
                        messagebox.showinfo('Error','Room full, please select another room.')
                    else:
                        roomGiven = random.choice(roomDict['basic'])
                        visitorIn = {'room':roomGiven,'sex': sex.get(),'address':entryAddress.get(),'phone':entryPhone.get(),'email':entryEmail.get(),'noOfDays':entryDays.get()}
                        visitorDict[entryName.get()] = visitorIn
                        roomDict['basic'].remove(roomGiven)
                        hotelDict['unoccupied'].remove(roomGiven)
                        hotelDict['occupied'].append(roomGiven)
                        messagebox.showinfo('Success','You have checked in. Your room number is ' + str(roomGiven))
                        checkInForm.destroy()
                        launchWelcomeScreen()
                elif room.get() == 2:
                    if len(roomDict['average']) == 0:
                        messagebox.showinfo('Error','Room full, please select another room.')
                    else:
                        roomGiven = random.choice(roomDict['average'])
                        visitorIn = {'room':roomGiven,'sex': sex.get(),'address':entryAddress.get(),'phone':entryPhone.get(),'email':entryEmail.get(),'noOfDays':entryDays.get()}
                        visitorDict[entryName.get()] = visitorIn
                        roomDict['average'].remove(roomGiven)
                        hotelDict['unoccupied'].remove(roomGiven)
                        hotelDict['occupied'].append(roomGiven)
                        messagebox.showinfo('Success','You have checked in. Your room number is ' + str(roomGiven))
                        checkInForm.destroy()
                        launchWelcomeScreen()
                elif room.get() == 3:
                    if len(roomDict['deluxe']) == 0:
                        messagebox.showinfo('Error','Room full, please select another room.')
                    else:
                        roomGiven = random.choice(roomDict['deluxe'])
                        visitorIn = {'room':roomGiven,'sex': sex.get(),'address':entryAddress.get(),'phone':entryPhone.get(),'email':entryEmail.get(),'noOfDays':entryDays.get()}
                        visitorDict[entryName.get()] = visitorIn
                        roomDict['deluxe'].remove(roomGiven)
                        hotelDict['unoccupied'].remove(roomGiven)
                        hotelDict['occupied'].append(roomGiven)
                        messagebox.showinfo('Success','You have checked in. Your room number is ' + str(roomGiven))
                        checkInForm.destroy()
                        launchWelcomeScreen()
                elif room.get() == 4:
                    if len(roomDict['kingsize']) == 0:
                        messagebox.showinfo('Error','Room full, please select another room.')
                    else:
                        roomGiven = random.choice(roomDict['kingsize'])
                        visitorIn = {'room':roomGiven,'sex': sex.get(),'address':entryAddress.get(),'phone':entryPhone.get(),'email':entryEmail.get(),'noOfDays':entryDays.get()}
                        visitorDict[entryName.get()] = visitorIn
                        roomDict['kingsize'].remove(roomGiven)
                        hotelDict['unoccupied'].remove(roomGiven)
                        hotelDict['occupied'].append(roomGiven)
                        messagebox.showinfo('Success','You have checked in. Your room number is ' + str(roomGiven))
                        checkInForm.destroy()
                        launchWelcomeScreen()
        

        checkInSubmit = Button(buttonFrame, text='Submit', command=checkInSubmitForm)
        checkInSubmit.grid(row=1, column=1)

        def checkInExit():
            checkInForm.destroy()
            launchWelcomeScreen()

        checkInExit = Button(buttonFrame, text='Exit', command=checkInExit)
        checkInExit.grid(row=1, column=2)

        checkInForm.mainloop()

    def checkOut():
        hotel.destroy()
        checkOutForm = Tk()
        checkOutForm.geometry('500x400')
        checkOutForm.resizable(False,False)
        checkOutForm.title('CHECK OUT FORM')

        visitorDetails = Label(checkOutForm, text='CHECK OUT FORM', height= 5, width= 30)
        visitorDetails.pack()

        detailsframe1 = Frame(checkOutForm)
        detailsframe1.pack()

        visitorName = Label(detailsframe1, text='Name :', height= 2, width= 30)
        visitorName.grid(row=1, column=1)

        entryName = Entry(detailsframe1)
        entryName.grid(row=1, column=2)

        visitorRoom = Label(detailsframe1, text='Room Number :', height= 2, width= 30)
        visitorRoom.grid(row=2, column=1)

        room = IntVar()

        roomList1 = Radiobutton(detailsframe1, text='basic @ 500', value= 1, variable= room)
        roomList1.grid(row=2, column=2)
        roomList2 = Radiobutton(detailsframe1, text='average @ 1000', value= 2, variable= room)
        roomList2.grid(row=2, column=3)
        roomList3 = Radiobutton(detailsframe1, text='deluxe @ 1500', value= 3, variable=room)
        roomList3.grid(row=3, column=2)
        roomList4 = Radiobutton(detailsframe1, text='kingsize @ 2000', value= 4, variable= room)
        roomList4.grid(row=3, column=3)

        detailsframe2 = Frame(checkOutForm)
        detailsframe2.pack()

        def checkOutSubmitForm():
            print('You have checked out.')
            checkOutForm.destroy()
            launchWelcomeScreen()
        

        checkOutSubmit = Button(detailsframe2, text='Submit', command=checkOutSubmitForm)
        checkOutSubmit.grid(row=1, column=1)

        def checkOutExit():
            checkOutForm.destroy()
            launchWelcomeScreen()

        checkOutExit = Button(detailsframe2, text='Exit', command=checkOutExit)
        checkOutExit.grid(row=1, column=2)

        checkOutForm.mainloop()

    def visitor():
        hotel.destroy()
        visitorDetail = Tk()
        visitorDetail.geometry('500x400')
        visitorDetail.resizable(False,False)
        visitorDetail.title('Search FORM')

        visitorDetails = Label(visitorDetail, text='SEARCH FORM', height= 5, width= 30)
        visitorDetails.pack()

        detailsframe1 = Frame(visitorDetail)
        detailsframe1.pack()

        visitorName = Label(detailsframe1, text='Name :', height= 2, width= 30)
        visitorName.grid(row=1, column=1)

        entryName = Entry(detailsframe1)
        entryName.grid(row=1, column=2)

        labelOr = Label(detailsframe1, text='OR', height= 5, width= 30)
        labelOr.grid(row=2,column=1)

        visitorRoom = Label(detailsframe1, text='Room Number :', height= 2, width= 30)
        visitorRoom.grid(row=3, column=1)

        room = IntVar()

        roomList1 = Radiobutton(detailsframe1, text='basic @ 500', value= 1, variable= room)
        roomList1.grid(row=3, column=2)
        roomList2 = Radiobutton(detailsframe1, text='average @ 1000', value= 2, variable= room)
        roomList2.grid(row=3, column=3)
        roomList3 = Radiobutton(detailsframe1, text='deluxe @ 1500', value= 3, variable=room)
        roomList3.grid(row=4, column=2)
        roomList4 = Radiobutton(detailsframe1, text='kingsize @ 2000', value= 4, variable= room)
        roomList4.grid(row=4, column=3)

        detailsframe2 = Frame(visitorDetail)
        detailsframe2.pack()

        def visitorDetailSubmitForm():
            print('You have checked out.')
            visitorDetail.destroy()
            launchWelcomeScreen()
        

        visitorDetailSubmit = Button(detailsframe2, text='Submit', command=visitorDetailSubmitForm)
        visitorDetailSubmit.grid(row=1, column=1)

        def visitorDetailExit():
            visitorDetail.destroy()
            launchWelcomeScreen()

        visitorDetailExit = Button(detailsframe2, text='Exit', command=visitorDetailExit)
        visitorDetailExit.grid(row=1, column=2)

        visitorDetail.mainloop()

    def visitorList():
        hotel.destroy()
        visitors = Tk()
        visitors.geometry('500x400')
        visitors.resizable(False,False)
        visitors.title('All Visitors')

        visitorDetails = Label(visitors, text='ALL VISITORS', height= 5, width= 30)
        visitorDetails.pack()

        allVisitors = Text(visitors, height= 17, width= 50)
        allVisitors.pack()

        def allVisitorsExit():
            visitors.destroy()
            launchWelcomeScreen()

        allVisitorsExit = Button(visitors, text='Exit', command=allVisitorsExit)
        allVisitorsExit.pack()
        visitors.mainloop()

    def orderFood():
        hotel.destroy()
        foodBill = Tk()
        foodBill.geometry('500x400')
        foodBill.resizable(False,False)
        foodBill.title('Ordering Food')

        def addFood():
            global sum
            n = entryQuantity.get()
            if n == '':
                messagebox.showinfo('Error', 'Please enter the quantity')
            else:
                if str(food.get()) == '1':
                    sum = sum + 40 * int(n)
                    showText.insert(END, "bevarage" + '--' + n + '\n')
                if str(food.get()) == '2':
                    sum = sum + 100 * int(n)
                    showText.insert(END, "breakfast" + '--' + n + '\n')
                if str(food.get()) == '3':
                    sum = sum + 150 * int(n)
                    showText.insert(END, "dinner" + '--' + n + '\n')
                if str(food.get()) == '4':
                    sum = sum + 50 * int(n)
                    showText.insert(END, "drink" + '--' + n + '\n')
                if str(food.get()) == '5':
                    sum = sum + 100 * int(n)
                    showText.insert(END, "supper" + '--' + n + '\n')
        
        def calculate():
            global sum
            messagebox.showinfo('Total Bill','Your total food bill is : ' + str(sum))
            sum = 0
            foodBill.destroy()
            launchWelcomeScreen()

        foodFrame = Frame(foodBill)
        foodFrame.pack()

        foodName = Label(foodFrame, text='Name of food :', height= 2, width= 30)
        foodName.grid(row=1, column=1)

        food = IntVar()

        foodList1 = Radiobutton(foodFrame, text='bevarage @ 40', value= 1, variable= food)
        foodList1.grid(row=1, column=2)
        foodList2 = Radiobutton(foodFrame, text='breakfast @ 100', value= 2, variable= food)
        foodList2.grid(row=2, column=2)
        foodList3 = Radiobutton(foodFrame, text='dinner @ 150', value= 3, variable=food)
        foodList3.grid(row=3, column=2)
        foodList4 = Radiobutton(foodFrame, text='drink @ 50', value= 4, variable= food)
        foodList4.grid(row=4, column=2)
        foodList5 = Radiobutton(foodFrame, text='supper @ 100', value= 5, variable=food)
        foodList5.grid(row=5, column=2)

        foodQuantity = Label(foodFrame, text='Quantity :', height= 2, width= 30)
        foodQuantity.grid(row=6, column=1)

        entryQuantity = Entry(foodFrame)
        entryQuantity.grid(row=6, column=2)

        showText = Text(foodBill, height= 10, width= 45)
        showText.pack()

        buttonFrame = Frame(foodBill)
        buttonFrame.pack()

        foodAdd = Button(buttonFrame, text='Add food', command=addFood)
        foodAdd.grid(row=1, column= 1)

        foodSubmit = Button(buttonFrame,text='Calculate', command=calculate)
        foodSubmit.grid(row=1, column= 2)

        def foodExit():
            foodBill.destroy()
            launchWelcomeScreen()

        foodExit = Button(buttonFrame, text='Exit', command=foodExit)
        foodExit.grid(row=1, column= 3)
        foodBill.mainloop()

    checkInButton = Button(hotel, text= 'CHECK IN', height= 2, width= 20, command = checkIn)
    checkInButton.pack()

    checkInButton = Button(hotel, text= 'CHECK OUT', height= 2, width= 20, command = checkOut)
    checkInButton.pack()

    checkInButton = Button(hotel, text= 'VISITOR DETAILS', height= 2, width= 20, command = visitor)
    checkInButton.pack()

    checkInButton = Button(hotel, text= 'ALL VISITORS', height= 2, width= 20, command = visitorList)
    checkInButton.pack()

    checkInButton = Button(hotel, text= 'FOOD ORDERING', height= 2, width= 20, command = orderFood)
    checkInButton.pack()

    checkInButton = Button(hotel, text= 'EXIT', height= 2, width= 20, command = exit)
    checkInButton.pack()
    hotel.mainloop()

launchWelcomeScreen()