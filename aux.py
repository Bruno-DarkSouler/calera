from sistema import *

ventana = TK.Tk()
ventana.geometry("700x550")
ventana.resizable(1, 1)

formulario = {
    "etiquetas":[
        TK.Label(ventana, text="Nombre"),
        TK.Label(ventana, text="Descripcion"),
        TK.Label(ventana, text="Fecha"),
    ],
    "entradas":[
        TK.Entry(ventana),
        TK.Entry(ventana),
        TK.Entry(ventana)
    ],
    "botones":[
        TK.Button(ventana, text="Enviar")
    ]
}

for i in range(3):
    formulario["etiquetas"][i].grid(column=0, row=i)
    formulario["entradas"][i].grid(column=1, row=i)
formulario["botones"][0].grid(column=0, row=3)


ventana.mainloop()