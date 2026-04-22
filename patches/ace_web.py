import tkinter as tk
root = tk.Tk()
root.title("ad blocked!")
root.geometry("300x200")
def on_click():
    quit()
label = tk.Label(root, text="If you see this, we have successfully blocked the ad!")
label.pack(pady=20)
label2 = tk.Label(root, text="Enjoy your content!")
label2.pack(pady=10)
button = tk.Button(root, text="Quit", command=on_click)
button.pack()
root.mainloop()
