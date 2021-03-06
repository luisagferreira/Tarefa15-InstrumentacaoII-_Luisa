from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
import tkinter as tk

janela =Tk()
janela.title("Tarefa 15(Instrumentação II)_Luísa")
janela.geometry('400x600')
janela.configure(bg='magenta')

def seleciona():
    escolha = var.get()
    if escolha == 1:
        som = 'Miau!'
    elif escolha == 2:
        som = 'Au... au...'
    elif escolha == 3:
        som = 'Hi!Hi!Hi!'
    elif escolha == 4:
        som = 'Ssss!'
    elif escolha == 5:
        som = 'Ual!'
        pass

    return som

def submit():
    try:
        name = nome.get()
        som = seleciona()
        return messagebox.showinfo('Campanha de vacinação', f'{som} {name}, obrigada por responder ao formulário.')
    except Exception as ep:
        return messagebox.showwarning('Campanha de vacinação', 'Preencha os dados corretamente!')


def termsCheck():
    if cb.get() == 1:
        enviar['state'] = NORMAL
    else:
        enviar['state'] = DISABLED
        messagebox.showerror('Campanha de vacinação', 'É necessário confirmar a responsabilidade')


frame1 = Label(janela,background='cyan')
frame1.grid()
frame2 = LabelFrame(frame1, text='ANIMAL', padx=30, pady=10)

var =IntVar()
cb = IntVar()

Label(frame1, text='NOME',bg='pink').grid(row=1, column=0, padx=5, pady=5)
Label(frame1, text='FORMULÁRIO PARA REQUERIMENTO DE VACINAS',bg='pink',font=("Microsoft JhengHei UI", 8)).grid(row=0, column=0,columnspan=5, padx=5, pady=5)

Radiobutton(frame2, text='Gato', variable=var, value=1).pack()
Radiobutton(frame2, text='Cachorro', variable=var, value=2).pack(anchor=W)
Radiobutton(frame2, text='Roedor', variable=var, value=3).pack()
Radiobutton(frame2, text='Serpente', variable=var, value=4).pack()
Radiobutton(frame2, text='Outros', variable=var, value=5).pack()


nome = Entry(frame1)
nome.grid(row=1, column=2,padx=30,pady=30)

frame2.grid(row=3, columnspan=4,padx=20,pady=20)

cor=tk.Label(frame1,text="Selecione a cor do cartão de vacinação: ")
cor.grid(row=6,column=2,padx=25,pady=25)
unit=tk.StringVar()
cor_box=ttk.Combobox(frame1,width=23,textvariable=unit,state="readonly")
cor_box['values']=('Azul', 'Rosa','Cinza')
cor_box.current(0)
cor_box.grid(row=7,column=2, padx=10,pady=10)

Checkbutton(frame1, text='Confirmar reponsabilidade.', variable=cb, onvalue=1, offvalue=0,
            command=termsCheck,bg='cyan').grid(row=8,column=2, columnspan=3, pady=5)

enviar = Button(frame1, text="ENVIAR", command=submit, padx=50, pady=5, state=DISABLED,background='pink',cursor="heart")
enviar.grid(row=9, column=2, columnspan=3, pady=25)

def envia(unit):

    if unit=='Azul':
        k='azul'
        return k
    elif unit=='Rosa':
        k='rosa'
        return k
    elif unit=='Cinza':
        k='cinza'
        return k
        pass

def submit2():

    print("Cor {} selecionada!".format(unit.get()))

    pass

def close_window():
    janela.destroy()
    pass

ir=ttk.Button(frame1,text = "Ir", command =submit2,cursor="heart")
ir.grid(row=7,column=3, pady=10)

sair=ttk.Button(frame1,text = "Fechar janela", command = close_window,cursor="heart")
sair.grid(row=10,column=2, pady=10)

janela.mainloop()