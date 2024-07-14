from tkinter import *

expression =''

def press(userInput): 
       global expression
       expression = expression + str(userInput)

       equation.set(expression)

def equalPress():
    try:
        global expression
        result = str(eval(expression))
        equation.set(result)
        expression = ''
    except:
        equation.set('Error')
    
def clear():
    global expression
    expression = ''
    equation.set('')    



gui =Tk()

gui.title("Calculator")
gui.geometry("420x400") 
titleLabel = Label(gui , text ="Simple calculator" , font =('Arial', 15 , 'bold') , fg='gray')
titleLabel.grid(columnspan=4 ,pady=20 , padx=50)

equation = StringVar()

expressionField = Entry(gui ,textvariable=equation , width=22 , font=('Arial', 15 , 'bold') , bd=5 , insertwidth=4 , bg='powder blue' , justify='center')
expressionField.grid(columnspan=4 ,padx=19 ,ipadx=55)

btn1 = Button(gui ,command=lambda : press(1), text='1' , font=('Arial', 15 , 'bold') , height=1 , width=7 )
btn1.grid(row=2 , column=0 , padx=5 , pady=5)

btn2 = Button(gui ,command=lambda : press(2), text='2' , font=('Arial', 15 , 'bold') , height=1 , width=7 )
btn2.grid(row=2 , column=1 , padx=5 , pady=5)

btn3 = Button(gui ,command=lambda : press(3), text='3' , font=('Arial', 15 , 'bold') , height=1 , width=7 )
btn3.grid(row=2 , column=2 , padx=5 , pady=5)

btn4 = Button(gui ,command=lambda : press(4), text='4' , font=('Arial', 15 , 'bold') , height=1 , width=7 )
btn4.grid(row=3 , column=0 , padx=5 , pady=5)

btn5 = Button(gui ,command=lambda : press(5), text='5' , font=('Arial', 15 , 'bold') , height=1 , width=7 )
btn5.grid(row=3 , column=1 , padx=5 , pady=5)

btn6 = Button(gui ,command=lambda : press(6), text='6' , font=('Arial', 15 , 'bold') , height=1 , width=7 )
btn6.grid(row=3 , column=2 , padx=5 , pady=5)

btn7 = Button(gui,command=lambda : press(7) , text='7' , font=('Arial', 15 , 'bold') , height=1 , width=7 )
btn7.grid(row=4 , column=0 , padx=5 , pady=5)

btn8 = Button(gui ,command=lambda : press(8), text='8' , font=('Arial', 15 , 'bold') , height=1 , width=7 )
btn8.grid(row=4 , column=1 , padx=5 , pady=5)

btn9 = Button(gui ,command=lambda : press(9), text='9' , font=('Arial', 15 , 'bold') , height=1 , width=7 )
btn9.grid(row=4 , column=2 , padx=5 , pady=5)

btn0 = Button(gui ,command=lambda : press(0), text='0' , font=('Arial', 15 , 'bold') , height=1 , width=7 )
btn0.grid(row=5 , column=0 , padx=5 , pady=5)

dotBtn= Button(gui ,command=lambda : press('.'), text='.' , font=('Arial', 15 , 'bold') , height=1 , width=7 )
dotBtn.grid(row=5 , column=1 , padx=5 , pady=5)

eqBtn= Button(gui , command=equalPress,text='=' , font=('Arial', 15 , 'bold') , height=1 , width=7 , bg='powder blue' , fg='black')
eqBtn.grid(row=5 , column=2 , padx=5 , pady=5)

addBtn= Button(gui ,command=lambda : press('+'), text='+' , font=('Arial', 15 , 'bold') , height=1 , width=7 )
addBtn.grid(row=2 , column=3 , padx=5 , pady=5)

minusBtn= Button(gui ,command=lambda : press('-'), text='-' , font=('Arial', 15 , 'bold') , height=1 , width=7 )
minusBtn.grid(row=3 , column=3 , padx=5 , pady=5)

multBtn= Button(gui ,command=lambda : press('*'), text='*' , font=('Arial', 15 , 'bold') , height=1 , width=7 )
multBtn.grid(row=4 , column=3 , padx=5 , pady=5)

divBtn= Button(gui ,command=lambda : press('/'), text='/' , font=('Arial', 15 , 'bold') , height=1 , width=7 )
divBtn.grid(row=5 , column=3 , padx=5 , pady=5)

clearBtn= Button(gui ,command=clear, text='C' , font=('Arial', 15 , 'bold') , height=1 , width=7 )
clearBtn.grid(row=6 , column=0 , padx=5 , pady=5)

gui.mainloop()