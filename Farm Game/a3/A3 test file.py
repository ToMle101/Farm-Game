import tkinter as tk

def frame_click(event):
    print("Frame clicked!")

root = tk.Tk()

frame = tk.Frame(root, width=200, height=200, bg="blue")
frame.pack(fill=tk.BOTH, expand=True)

label = tk.Label(frame, text="Click me", bg="yellow")
label.pack()

label.bind("<Button-1>", frame_click)

frame.bind("<Button-1>", frame_click)

root.mainloop()











