#############################################################importing libs##########################################################
from tkinter import*
from tkinter import ttk
from pathlib import Path
###############################
#main window
win = Tk()
win.title("Calculator")
win.resizable(False,False)
win.geometry("700x750")          #window size
win.config(bg = "black")         #main window back ground color
###############################
c = Canvas(win,width = 350,height = 110,bg = "pink")       #output canvas
c.place(relx = 0.3,rely = 0.02)  #placing output canvas
path = r"numbers/" 
##################################################################################
live_label_text = StringVar()
live_label = Label(win,textvariable = live_label_text,fg = "black",bg = "pink",font = ("mitra",40,"bold") )
result_label_text = StringVar()
result_label = Label(win,textvariable = result_label_text , fg = "black" , bg ="pink",font = ("mitra",40,"bold"))
p = []  #process
status = []
result_status = []
#functions
try:
    def result():
    
        process = ""
        for a in p:
            process += a
        result = eval(process)
        result_label_text.set("= " + str(result))
        live_label_text.set("")
        live_label.place(relx =0.328 ,rely = 0.053)
        result_label.place(relx =0.328 ,rely = 0.053)
        status.append("True")
        result_status.append("True")


    def result_deleter():
        if "True" in status:
            result_label_text.set("")
            for member in range(len(status)):
                status.remove(status[0])


    def list_reseter():
        if "True" in result_status:
            for x in range(len(p)):
                p.remove(p[0])

            for member in range(len(result_status)):
                result_status.remove(result_status[0])

except:
   result_label_text.set("Error")
   result_label.place(relx =0.328 ,rely = 0.053)
            

def one():
    list_reseter()
    p.append("1")
    a = live_label_text.get()
    live_label_text.set(str(a) + "1")
    live_label.place(relx =0.328 ,rely = 0.053)
    result_deleter()
    
def two():
    list_reseter()
    p.append("2")
    a = live_label_text.get()
    live_label_text.set(str(a) + "2")
    live_label.place(relx =0.328 ,rely = 0.053)
    result_deleter()
    
def three():
    list_reseter()
    p.append("3")
    a = live_label_text.get()
    live_label_text.set(str(a) + "3")
    live_label.place(relx =0.328 ,rely = 0.053)
    result_deleter()
    
def four():
    p.append("4")
    a = live_label_text.get()
    live_label_text.set(str(a) + "4")
    live_label.place(relx =0.328 ,rely = 0.053)
    result_deleter()
    
def five():
    list_reseter()
    p.append("5")
    a = live_label_text.get()
    live_label_text.set(str(a) + "5")
    live_label.place(relx =0.328 ,rely = 0.053)
    result_deleter()
    
def six():
    list_reseter()
    p.append("6")
    a = live_label_text.get()
    live_label_text.set(str(a) + "6")
    live_label.place(relx =0.328 ,rely = 0.053)
    result_deleter()
    
def seven():
    list_reseter()
    p.append("7")
    a = live_label_text.get()
    live_label_text.set(str(a) + "7")
    live_label.place(relx =0.328 ,rely = 0.053)
    result_deleter()
    
def eight():
    list_reseter()
    p.append("8")
    a = live_label_text.get()
    live_label_text.set(str(a) + "8")
    live_label.place(relx =0.328 ,rely = 0.053)
    result_deleter()
    
def nine():
    list_reseter()
    p.append("9")
    a = live_label_text.get()
    live_label_text.set(str(a) + "9")
    live_label.place(relx =0.328 ,rely = 0.053)
    result_deleter()
    

def plus():
    list_reseter()
    p.append("+")
    a = live_label_text.get()
    live_label_text.set(str(a) + "+")
    live_label.place(relx =0.328 ,rely = 0.053)
    result_deleter()
    
def minese():
    list_reseter()
    p.append("-")
    a = live_label_text.get()
    live_label_text.set(str(a) + "-")
    live_label.place(relx =0.328 ,rely = 0.053)
    result_deleter()
    
def devide():
    list_reseter()
    p.append("/")
    a = live_label_text.get()
    live_label_text.set(str(a) + "/")
    live_label.place(relx =0.328 ,rely = 0.053)
    result_deleter()
    
def multiply():
    list_reseter()
    p.append("*")
    a = live_label_text.get()
    live_label_text.set(str(a) + "X")
    live_label.place(relx =0.328 ,rely = 0.053)
    result_deleter()

def ob():
    list_reseter()
    p.append("(")
    a = live_label_text.get()
    live_label_text.set(str(a) + "(")
    live_label.place(relx =0.328 ,rely = 0.053)
    result_deleter()

def cb():
    list_reseter()
    p.append(")")
    a = live_label_text.get()
    live_label_text.set(str(a) + ")")
    live_label.place(relx =0.328 ,rely = 0.053)
    result_deleter()

def dot():
    list_reseter()
    p.append(".")
    a = live_label_text.get()
    live_label_text.set(str(a) + ".")
    live_label.place(relx =0.328 ,rely = 0.053)
    result_deleter()

def reset():
    result_deleter()
    list_reseter()


    
    
###############################
#buttons
#1
b1 = Button(win,command = one,activebackground = "purple")
b1_img = PhotoImage(file = path + r"\1.png" )
b1.config(image = b1_img)
b1.place(relx = 0.3 ,rely =0.2)

#2
b2 = Button(win , command = two,activebackground = "purple")
b2_img = PhotoImage(file = path + r"\2.png")
b2.config(image = b2_img)
b2.place(relx = 0.5 ,rely =0.2)

#3

b3 = Button(win , command = three,activebackground = "purple")
b3_img = PhotoImage(file = path + r"\3.png")
b3.config(image = b3_img)
b3.place(relx = 0.7 ,rely =0.2)

#4
b4 = Button(win , command = four,activebackground= "purple")
b4_img = PhotoImage(file = path + r"\4.png")
b4.config(image = b4_img)
b4.place(relx = 0.3 ,rely =0.4)

#5
b5 = Button(win , command = five,activebackground = "purple")
b5_img = PhotoImage(file = path + r"\5.png")
b5.config(image = b5_img)
b5.place(relx = 0.5 ,rely =0.4)

#6
b6 = Button(win , command = six,activebackground = "purple")
b6_img = PhotoImage(file = path + r"\6.png")
b6.config(image = b6_img)
b6.place(relx = 0.7 ,rely =0.4)

#7
b7 = Button(win , command = seven,activebackground = "purple")
b7_img = PhotoImage(file = path + r"\7.png")
b7.config(image = b7_img)
b7.place(relx = 0.3 ,rely =0.6)

#8
b8 = Button(win , command = eight,activebackground = "purple")
b8_img = PhotoImage(file = path + r"\8.png")
b8.config(image = b8_img)
b8.place(relx = 0.5 ,rely =0.6)

#9
b9 = Button(win , command = nine,activebackground = "purple")
b9_img = PhotoImage(file = path + r"\9.png")
b9.config(image = b9_img)
b9.place(relx = 0.7 ,rely =0.6)

#devide
b_devide = Button(win ,command = devide,activebackground = "purple")
b_devide_img = PhotoImage(file = path + r"\devide.png")
b_devide.config(image = b_devide_img)
b_devide.place(relx = 0.06 ,rely =0.6)

#equal
b_equal = Button(win ,command = result,activebackground = "purple")
b_equal_img = PhotoImage(file = path + r"\equal.png")
b_equal.config(image = b_equal_img)
b_equal.place(relx = 0.06 ,rely =0.8)

#reset
b_reset = Button(win ,command = reset,activebackground = "purple")
b_reset_img = PhotoImage(file = path + r"\reset.png")
b_reset.config(image = b_reset_img)
b_reset.place(relx = 0.7 ,rely =0.8)

#close bracket
b_cb = Button(win ,command = cb,activebackground= "purple")
b_cb_img = PhotoImage(file = path + r"\close bracket.png")
b_cb.config(image = b_cb_img)
b_cb.place(relx = 0.5 ,rely =0.8)

#open bracket

b_ob = Button(win ,command = ob,activebackground = "purple")
b_ob_img = PhotoImage(file = path + r"\open bracket.png")
b_ob.config(image = b_ob_img)
b_ob.place(relx = 0.3 ,rely =0.8)

#plus
b_plus = Button(win , command = plus,activebackground = "purple")
b_plus_img = PhotoImage(file =path + r"\plus.png")
b_plus.config(image = b_plus_img)
b_plus.place(relx = 0.06 ,rely =0.2)

#minese
b_minese = Button(win , command = minese,activebackground = "purple")
b_minese_img = PhotoImage(file = path + r"\minese.png")
b_minese.config(image = b_minese_img)
b_minese.place(relx = 0.06 ,rely =0.4)

#multiply
b_multiply = Button(win , command = multiply,activebackground = "purple")
b_multiply_img = PhotoImage(file = path + r"\multiply.png")
b_multiply.config(image = b_multiply_img)
b_multiply.place(relx = 0.06 ,rely =0.01)

#dot
b_d = Button(win , command = dot,activebackground = "purple",activeforeground = "purple")
b_d_img = PhotoImage(file = path + r"\dot.png")
b_d.config(image = b_d_img)
b_d.place(relx = 0.83 ,rely =0.02)
####################################
win.mainloop()
