from tkinter import*


def incrementar():
	valor = int(lbl_valor['text'])
	lbl_valor['text']= f'{valor + 1}'

def decrementar():
	valor = int(lbl_valor['text'])
	lbl_valor['text']= f'{valor - 1}'



ventana = Tk()
ventana.title("Contador")
#ventana.iconobitmap("")
ventana.rowconfigure(0, minsize=100, weight=1)
ventana.columnconfigure([0,1,2], minsize=100, weight=1)


btn_decre = Button(ventana, text="-", command = decrementar)
btn_decre.grid(row=0, column=0, sticky="nsew")

lbl_valor = Label(ventana, text="0")
lbl_valor.grid(row=0, column=1)

btn_incre= Button(ventana, text="+", command= incrementar)
btn_incre.grid(row=0, column=2, sticky="nsew")

ventana.mainloop()