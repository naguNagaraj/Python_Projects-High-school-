






#     clock.after(200,get_time)
#     clock.config(text=timeVar)
#     timeVar = time.strftime("%I:%M:%S %p")
# clock = Label(master, font=('Arial',100), bg = "Green", fg = "Red")
# clock.pack()
# def get_time():
# from tkinter import Label
# from tkinter import Tk
# get_time()
# import sys
# import time
# Label(master,font=("Arial",30),text="Remeshante Clock",fg = "Red", bg = "Green").pack()
# master = Tk()
# master.mainloop()
# master.title("Python Clock")

# x = [i for i in "hellow"]
# a,b,c,d,e,f = x
# print(a,b,c,d)
# x = 0
# ayne = 7
# x = 4 if ayne > 6 else 0
# if x == None:
#     x = "potte"
# print(x)



# list_1 = [1,2,3,4,5]
# list_2 = ["ayne","nee","ehta","da","mwone"]
# list_3 = [100,200,300,400,500]
# for list_1, list_2, list_3 in zip(list_1, list_2, list_3):
#     if list_3 >= 300:
#         print(list_1)


def ayne(a,b,c):
    print(a*3)
    print(b+3)
    print(c-5)
test_list = []
x = int(input("Enter the 1st number : "))
y = int(input("Enter the 2nd numeber : "))
z = int(input("Enter the 3rd number : "))
test_list.append(x)
test_list.append(y)
test_list.append(z)
ayne(*test_list)
