import tkinter as tk


def callback(*event):
    print(s.get())


root = tk.Tk()
tk.Label(root, text="输入：").pack(side="left")
s = tk.StringVar(root)
ent = tk.Entry(root, textvariable=s)
ent.pack(side="left")
s.trace("w", callback)
root.mainloop()


