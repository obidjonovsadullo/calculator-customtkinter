#Calculator

import customtkinter as ctk

app = ctk.CTk()

app.title("Calculator")
app.geometry("300x450")
app.resizable(False,False)

#Natija oynachasi

entry = ctk.CTkEntry(app,width=280, height=60,font=("Arial",25),justify="right") 
entry.pack(pady=20)
#tugmalar funksiyasi
OPS = {"+", "-", "*", "/", "%"}

def button_click(value):
    text = entry.get()

    if value == "C":
        entry.delete(0, "end")
        return

    if value == "⌫":
        if text:
            entry.delete(len(text) - 1, "end")
        return

    elif value == "=":
        try:
            expr = entry.get().replace("%", "/100")
            result = eval(expr)
            entry.delete(0, "end")
            entry.insert("end", str(result))
        except:
            entry.delete(0, "end")
            entry.insert("end", "Error")


    # ====== QOIDALAR ======

    # Operatorlar: + - * / %
    if value in OPS:
        # bo‘sh joyga operator qo‘ymaymiz
        if not text:
            return
        # oxiri operator bo‘lsa yana qo‘shmaymiz
        if text[-1] in OPS or text[-1] == ".":
            return
        entry.insert("end", value)
        return

    # Nuqta (.) ketma-ket bo‘lmasin va bitta son ichida 2ta nuqta bo‘lmasin
    if value == ".":
        if not text:
            entry.insert("end", "0.")
            return
        if text[-1] == "." or text[-1] in OPS:
            return
        # oxirgi operatorlardan keyingi qismda nuqta bor-yo‘qligini tekshiramiz
        last_part = text
        for op in OPS:
            last_part = last_part.replace(op, " ")
        last_num = last_part.split()[-1] if last_part.split() else ""
        if "." in last_num:
            return
        entry.insert("end", ".")
        return

    # Oddiy raqamlar (00 ham shu yerga tushadi)
    entry.insert("end", value)



#numbers with keyboard

def key_event(event):
    key = event.keysym

    if key in "0123456789":
        button_click(key)

    elif key in ["plus", "KP_Add"]:
        button_click("+")

    elif key in ["minus", "KP_Subtract"]:
        button_click("-")

    elif key in ["asterisk", "KP_Multiply"]:
        button_click("*")

    elif key in ["slash", "KP_Divide"]:
        button_click("/")

    elif key in ["period", "KP_Decimal"]:
        button_click(".")

    elif key in ["Return", "KP_Enter"]:
        button_click("=")

    elif key == "BackSpace":
        button_click("⌫")

    elif key == "Escape":
        button_click("C")


#tugmalar ro'yxati

buttons = [
    ["C", "⌫", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["00", "0", ".", "="]
]

frame =ctk.CTkFrame(app)
frame.pack()


for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        if text in ["+", "-", "*","/","=","%","⌫"]:
            color = ("#f1c440f","#f39c12")
            text_color = "black"
        elif text in ["C"]: 
           color = ("#e74c3c", "#c0392b")
           text_color = "white"
        else:
            color = ("#2c3e50","#34495e")
            text_color = "white"

        btn = ctk.CTkButton(frame, text=text,width=60,height=60,font=("Arial",15),
                             fg_color=color,
                             text_color= text_color,
                            hover_color="#95a5a6",
                            command=lambda t=text:button_click(t))
        btn.grid(row=i,column=j , padx=5, pady=5)  

app.bind("<Key>", key_event)
app.mainloop()




