# Import tkinter
from tkinter import *      # import *: Importa o núcleo básico de widgets do tkinter. Isso inclui widgets simples como Button, Label, Entry, Frame, etc. É a base para construir uma interface gráfica básica.
from tkinter import ttk    # import ttk: Importa o módulo ttk (abreviação de Themed Tk), que oferece versões mais avançadas e estilizadas de alguns widgets, como Button, Label, Entry, Combobox, entre outros.

# cores 

cor1 = "#06070a" # Cor do frame da tela - Preto/black
cor2 = "#909899" # Cinza
cor3 = "#406ac9" # Azul Escuro
cor4 = "#d18d3b" # Laranja
cor5 = "#b2cfd1" # Azul
cor6 = "#ba7d9b" # Rosa
cor7 = "white"   # Branco

# Cria a janela principal
janela = Tk()
janela.title("CALCULADORA") # Titulo
janela.geometry("235x310") # (largura x comprimento)
janela.config(bg=cor1)

# Frame
frame_tela = Frame(janela, width=235, height=50, bg=cor1)  # width = largura / height = altura
frame_tela.grid(row=0, column=0) # row = linha / column = coluna  

# Corpo
frame_body = Frame(janela, width=235, height=268)  # width = largura / height = altura
frame_body.grid(row=1, column=0) # row = linha / column = coluna  

# Criando Label - Funções
valor_texto =  StringVar()

app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18 '), bg=cor2, fg=cor7)
app_label.place(x=0, y=0)   

# Funções

def entrar_valores(event):

    global todos_valores

    todos_valores = todos_valores + str(event)

    # Passando valor para tela  
    valor_texto.set(todos_valores) 

# Variável todos valores 

todos_valores = ''

# Função para calcular

def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))

# Função limpar Tela

def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")

# Botões

b_1 = Button(frame_body, command = limpar_tela, text="C", width=11, height=2, bg=cor5, fg="white", font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)     

b_2 = Button(frame_body, command = lambda: entrar_valores('%'), text="%", width=5, height=2, bg=cor5, fg="white", font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0) 

b_3 = Button(frame_body, command = lambda: entrar_valores('/'), text="/", width=5, height=2, bg=cor4, fg="white", font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0) 

# Linha 1 

b_4 = Button(frame_body, command = lambda: entrar_valores('7'), text="7", width=5, height=2, bg=cor5, fg="white", font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52) 

b_4 = Button(frame_body, command = lambda: entrar_valores('8'), text="8", width=5, height=2, bg=cor5, fg="white", font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=59, y=52)

b_4 = Button(frame_body, command = lambda: entrar_valores('9'), text="9", width=5, height=2, bg=cor5, fg="white", font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=118, y=52)

b_3 = Button(frame_body, command = lambda: entrar_valores('*'), text="*", width=5, height=2, bg=cor4, fg="white", font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=52) 

# Linha 2

b_4 = Button(frame_body, command = lambda: entrar_valores('4'), text="4", width=5, height=2, bg=cor5, fg="white", font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=104) 

b_4 = Button(frame_body, command = lambda: entrar_valores('5'), text="5", width=5, height=2, bg=cor5, fg="white", font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=59, y=104)

b_4 = Button(frame_body, command = lambda: entrar_valores('6'), text="6", width=5, height=2, bg=cor5, fg="white", font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=118, y=104)

b_3 = Button(frame_body, command = lambda: entrar_valores('-'), text="-", width=5, height=2, bg=cor4, fg="white", font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=104) 

# Linha 3 

b_4 = Button(frame_body, command = lambda: entrar_valores('1'), text="1", width=5, height=2, bg=cor5, fg="white", font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=156) 

b_4 = Button(frame_body, command = lambda: entrar_valores('2'), text="2", width=5, height=2, bg=cor5, fg="white", font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=59, y=156)

b_4 = Button(frame_body, command = lambda: entrar_valores('3'), text="3", width=5, height=2, bg=cor5, fg="white", font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=118, y=156)

b_3 = Button(frame_body, command = lambda: entrar_valores('+'), text="+", width=5, height=2, bg=cor4, fg="white", font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=156) 

# Linha 4 

b_1 = Button(frame_body, command = lambda: entrar_valores('0'), text="0", width=11, height=2, bg=cor5, fg="white", font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=208)

b_4 = Button(frame_body, command = lambda: entrar_valores('.'), text=".", width=5, height=2, bg=cor5, fg="white", font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=118, y=208)

b_3 = Button(frame_body, command= calcular, text="=", width=5, height=2, bg=cor4, fg="white", font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=208)

# DESENHO DA CALCULADORA FINALIZADO #


# relief: Define o estilo da borda normal do widget. 
# overrelief=RIDGE: Salta ao passar o mouse.

# Mostrar resultado

janela.mainloop()