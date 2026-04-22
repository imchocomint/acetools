import os
import subprocess
from search import get_data
import tkinter as tk
from tkinter import messagebox, scrolledtext
from checkrun import checkrun
runningFrom = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
runState = 0
root = tk.Tk()
root.title("acetools")
root.geometry("800x600")

queryTopic = tk.StringVar()
# Search frame
search_frame = tk.Frame(root, bg="lightgray", pady=10)
search_frame.pack(fill=tk.X, padx=10, pady=10)

search_label = tk.Label(search_frame, text='Keywords', font=('calibre', 10, 'bold'), bg="lightgray")
search_label.pack(side=tk.LEFT, padx=5)

search_entry = tk.Entry(search_frame, textvariable=queryTopic, font=('calibre', 10, 'normal'), width=40)
search_entry.pack(side=tk.LEFT, padx=5)


# Results frame
results_label = tk.Label(root, text='Results', font=('calibre', 10, 'bold'))
results_label.pack(anchor=tk.W, padx=10, pady=(10, 0))

results_text = scrolledtext.ScrolledText(root, font=('calibre', 10), height=25, state=tk.DISABLED)
results_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)


def gui_search():
    query = queryTopic.get()
    if not query.strip():
        messagebox.showwarning("Warning", "Please enter a search query")
        return
    
    # Clear previous results
    results_text.config(state=tk.NORMAL)
    results_text.delete("1.0", tk.END)
    
    try:
        results = get_data(query)
        
        if isinstance(results, str) and results.startswith("Error"):
            results_text.insert(tk.END, results)
        elif results:
            for res in results:
                results_text.insert(tk.END, f"Stream: {res['name']}\n")
                results_text.insert(tk.END, f"Link:   {res['link']}\n\n")
        else:
            results_text.insert(tk.END, "No streams found.")
    except Exception as e:
        results_text.insert(tk.END, f"Error: {e}")
    
    results_text.config(state=tk.DISABLED)

def killace():
    try:
        if os.name == 'nt':
            subprocess.Popen([os.path.join(runningFrom, "ace-engine", "kill-service.bat")], creationflags=subprocess.CREATE_NEW_CONSOLE)
            root.after(1000, update_status)
        else:
            print("Running on Linux yet to be supported")
        messagebox.showinfo("Success", "Acestream processes have been terminated.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to kill Acestream processes: {e}")

sub_btn = tk.Button(search_frame, text='Submit', command=gui_search, bg='blue', fg='white', padx=20)
sub_btn.pack(side=tk.LEFT, padx=5)
kill_btn = tk.Button(search_frame, text='Kill Acestream', command=killace, bg='red', fg='white', padx=20)
kill_btn.pack(side=tk.LEFT, padx=5)

status_label = tk.Label(root, text="", font=('calibre', 10))
status_label.pack(side=tk.TOP, pady=10)

def update_status():
    if checkrun("ace_console"):
        status_label.config(text="Acestream services are currently running", fg="green")
    else:
        status_label.config(text="Acestream services are currently off", fg="red")
def startace():
    try:
        if os.name == 'nt':
            subprocess.Popen([os.path.join(runningFrom, "ace-engine", "start-engine.bat")], creationflags=subprocess.CREATE_NEW_CONSOLE)
            root.after(20, update_status)
        else:
            print("Running on Linux yet to be supported")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to start Acestream processes: {e}")

start_btn = tk.Button(search_frame, text='Start Acestream', command=startace, bg='green', fg='white', padx=20)
start_btn.pack(side=tk.LEFT, padx=5)

update_status()

root.mainloop()