import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

root.title("Tic Tac Toe")
root.geometry("600x600")

turn = 0

def button_pressed(event):
    global turn
    button = event.widget
    if button["text"] == " ":
        button["text"] = "X" if turn % 2 == 0 else "O"
        turn += 1

    check_winner()

    if turn == 9:
        for child in frame.winfo_children():
            child["text"] = " "
        turn = 0
        messagebox.showinfo("Game Over", "It's a draw!")

def check_winner():
    global turn

    buttons = frame.winfo_children()
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], 
        [0, 3, 6], [1, 4, 7], [2, 5, 8], 
        [0, 4, 8], [2, 4, 6]              
    ]

    for i in winning_combinations:
        if buttons[i[0]]["text"] == buttons[i[1]]["text"] == buttons[i[2]]["text"] != " ":
            winner = buttons[i[0]]["text"]
            messagebox.showinfo("Game Over", f"{winner} wins!")

            for child in frame.winfo_children():
                child["text"] = " "

            turn = 0
            
            break

frame = tk.Frame(root)

for i in range(3):
    for j in range(3):
        button = tk.Button(frame, text=" ", font=("Arial", 40), width=5, height=2)
        button.grid(row=i, column=j)
        button.bind("<Button-1>", button_pressed)

frame.pack(pady = 25)

root.mainloop()