from tkinter import *
from tkinter import ttk

num1 = 0
num2 = 0
operacao = ""
resultado = 0

cor1 = '#3b3b3b'  
cor2 = '#feffff'
cor3 = '#38576b'
cor4 = '#eceff1'
cor5 = '#ffab40'

var_limpar_visor = False

#criando funçao 

def texto_visor (X):
    global var_limpar_visor
    if var_limpar_visor:
        label_visor.config(text="")
        var_limpar_visor = False


    label_visor.config(text=label_visor.cget("text") + X)


def salvar_operacao (x):
    global num1, operacao, var_limpar_visor, label_peq
    operacao = ""
    try : 
        num1 = int(label_visor.cget("text"))
    except  ValueError :
        num1 = float(label_visor.cget("text"))
    var_limpar_visor = True
    operacao = x 
    label_peq.config(text=label_visor.cget("text") + x)


def calcular ():
    global num2, operacao, resultado, label_visor, label_peq
    try : 
        num2 = int(label_visor.cget("text"))
    except  ValueError:
        num2 = float(label_visor. cget("text"))

    if operacao == '+' :
        resultado = num1 + num2
    elif operacao == '/' :
        resultado = num1 / num2
    elif operacao == 'x' :
        resultado = num1 * num2
    elif operacao == '-' :
        resultado = num1 - num2

      
    label_visor.config(text=str(resultado))
    label_peq.config (text="(" + label_peq.cget("text") + "= " + label_visor.cget("text") + ")" )

def limpar_visor ():
   global num1, num2, resultado, operacao, label_visor, label_peq
   label_visor.config(text="")
   label_peq.config(text="")
   num1, num2, resultado  = 0, 0, 0
   operacao=""


janela = Tk()
janela.title("calculadora")
janela.geometry("235x310")
janela.resizable(width=FALSE, height= FALSE)

#frame visor

frame_visor = Frame(janela, width=235, height=50, bg=cor3)
frame_visor.grid(row=0, column=0)


label_visor = Label(frame_visor, text="", width=16, height=2, padx=7, relief=FLAT,
                    anchor="e", justify=RIGHT, font=('Ivy 18'), bg=cor3, fg=cor2) 
label_visor.place(x=0, y=0)


label_peq= Label(frame_visor, text="", width=27, height=1, padx=7, relief=FLAT, 
                 anchor='e', justify=RIGHT, font=('Ivy 10'), bg=cor4, fg=cor1)
label_peq.place(x=0,y=55)

#frame corpo 

frame_corpo = Frame(janela, width=235, height=265, )
frame_corpo.grid(row=1, column=0)

#botoes

btn_limpar = Button(frame_corpo, command=limpar_visor, text='C', width=11, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_limpar.place(x=0, y=0)

btn_percent = Button(frame_corpo, command=lambda: texto_visor ('%'), text='%', width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_percent.place(x=118, y=0)


btn_1 = Button(frame_corpo, command=lambda: texto_visor ('1'), text='1', width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_1.place(x=0, y=156)


btn_2 = Button(frame_corpo, command=lambda: texto_visor ('2'), text='2', width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_2.place(x=59, y=156)


btn_3= Button(frame_corpo, command=lambda: texto_visor ('3'), text='3', width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_3.place(x=118, y=156)

btn_4= Button(frame_corpo, command=lambda: texto_visor ('4'), text='4', width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_4.place(x=0, y=104)

btn_5= Button(frame_corpo, command=lambda: texto_visor ('5'), text='5', width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_5.place(x=59, y=104) 

btn_6= Button(frame_corpo, command=lambda: texto_visor ('6'), text='6', width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_6.place(x=118, y=104)

btn_7= Button(frame_corpo, command=lambda: texto_visor ('7'), text='7', width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_7.place(x=0, y=52)

btn_8= Button(frame_corpo, command=lambda: texto_visor ('8'), text='8', width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_8.place(x=59, y=52)

btn_9= Button(frame_corpo, command=lambda: texto_visor ('9'), text='9', width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_9.place(x=118, y=52)

btn_0= Button(frame_corpo, command=lambda: texto_visor ('0'), text='0', width=11, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_0.place(x=0, y=208)


btn_somar= Button(frame_corpo,  command=lambda: salvar_operacao('+'), text= '+', width=5, height=2, bg=cor5, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_somar.place(x=175, y=52)

btn_subtrair= Button(frame_corpo,  command=lambda: salvar_operacao('-'), text= '-', width=5, height=2, bg=cor5, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_subtrair.place(x=175, y=104)

btn_dividir= Button(frame_corpo,  command=lambda: salvar_operacao('/'), text= '/', width=5, height=2, bg=cor5, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_dividir.place(x=175, y=0)

btn_multiplicar= Button(frame_corpo,  command=lambda: salvar_operacao('x'), text='x', width=5, height=2, bg=cor5, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_multiplicar.place(x=175, y=156)

btn_igual= Button(frame_corpo,command=calcular, text= '=', width=5, height=2, bg=cor5, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_igual.place(x=175, y=208)

btn_ponto = Button(frame_corpo,command=lambda: texto_visor('.'), text = ".", width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
btn_ponto.place(x=118, y=208)




janela.mainloop()
