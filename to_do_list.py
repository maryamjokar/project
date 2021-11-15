import tkinter
from tkinter.constants import COMMAND
import tkinter.messagebox

root = tkinter.Tk()
root.title("to do list")

def add_task():
    task = entry_task.get()
    if task!=:
        Listbox_tasks.insert(tkinter.END ,task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="warning", message="You must enter a task.")


#create GUI
frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

Listbox_tasks=tkinter.Listbox(root,height=3, width=50)
Listbox_tasks.pack(side=tkinter.LEFT)

Scrollbar_task = tkinter.Scrollbar(frame_tasks)
Scrollbar_task.pack(side=tkinter.RIGHT, fill=tkinter.Y)

entry_task= tkinter.Entry(root,width=50)
entry_task.pack()

button_add_task= tkinter.Button(root, text="Add task",width=48, command = add_task)
button_add_task()

root.mainloop()