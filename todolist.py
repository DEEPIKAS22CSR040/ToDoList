import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3 as sql

# adding task to list and database
def add_task():
    task_string=task_field.get()
    if(len(task_string)==0):
        messagebox.showinfo('Error','The Field is empty')
    else:
        task.append(task_string)
        the_cursor.execute('insert into tasks values(?)',(task_string,))
        list_update()
        task_field.delete(0,'end')
def list_update():
    clear_list()
    for t in task:
        task_listbox.insert('end',t)
def delete_task():
    try:
      value=tastk_listbox.get(task_listbox.curselection())
      if value in task:
         task.remove(value)
         list_update()
         the_cursor.execute('delete from tasks where title=?',(value,))
    except:
        messagebox.showinfo('Error','No taks selected cannot delete')
        
def delete_all_task():
    mb=messagebox.askyesno('Delete All','Are you sure')
    if mb==True:
      if(len(task)!=0):
         task.pop()
    the_cursor.execute('delete from tasks')
    list_update()
def clear_list():
    task_listbox.delete(0,'end')
def close():
    print(task)
    guiWindow.destroy()
def retrieve_database():
    while(len(task)!=0):
        task.pop()
    for row in the_cursor.execute('select title from tasks'):
        task.append(row[0])
        
if __name__=="__main__":
    guiWindow=tk.Tk()
    guiWindow.title("To-Do List Application")  
    screen_width = guiWindow.winfo_screenwidth()
    screen_height = guiWindow.winfo_screenheight()
    guiWindow.geometry("{}x{}+0+0".format(screen_width, screen_height))
    guiWindow.resizable(True,True)
    guiWindow.configure(bg = "#e1ad21") 
    
    the_connection=sql.connect('listOfTask.db')
    the_cursor=the_connection.cursor()
    the_cursor.execute('create table if not exists tasks (title text)')  
    
    task=[]
    
    header_frame = tk.Frame(guiWindow, bg = "#6495ED")  
    functions_frame = tk.Frame(guiWindow, bg = "#6495ED")  
    listbox_frame = tk.Frame(guiWindow, bg = "#6495ED")  
    
    header_frame.pack(fill = "both")  
    functions_frame.pack(side = "left", expand = True, fill = "both")  
    listbox_frame.pack(side = "right", expand = True, fill = "both")  
    
    header_label = ttk.Label(  
        header_frame,  
        text = "To-Do List",  
        font = ("Arial", "30"),  
          
        foreground = "#8B4513"  
    )  
    
    header_label.pack(padx = 20, pady = 20)
    
    task_label = ttk.Label(  
        functions_frame,  
        text = "Enter the Task:",  
        font = ("Consolas", "15", "bold"),  
          
        foreground = "#000000"  
    ) 
    task_label.place(x = 30, y = 40)  
    
    task_field = ttk.Entry(  
        functions_frame,  
        font = ("Consolas", "12"),  
        width = 20,  
        background = "#F0FFF0",  
        foreground = "#A52A2A"  
    )  
    task_field.place(x = 30, y = 80)  
    
    add_button = ttk.Button(  
        functions_frame,  
        text = "Add Task",  
        width = 24,  
        command = add_task  
    )  
    del_button = ttk.Button(  
        functions_frame,  
        text = "Delete Task",  
        width = 24,  
        command = delete_task  
    )  
    del_all_button = ttk.Button(  
        functions_frame,  
        text = "Delete All Tasks",  
        width = 24,  
        command = delete_all_task  
    )  
    exit_button = ttk.Button(  
        functions_frame,  
        text = "Exit",  
        width = 24,  
        command = close  
    )  
    
    add_button.place(x = 30, y = 120)  
    del_button.place(x = 30, y = 160)  
    del_all_button.place(x = 30, y = 200)  
    exit_button.place(x = 30, y = 240)  
  
    
    task_listbox = tk.Listbox(  
        listbox_frame,  
        width = 40,  
        height = 20,  
        selectmode = 'SINGLE',  
        background = "#F0FFFF",  
        foreground = "#000000",  
        selectbackground = "#CD853F",  
        selectforeground = "#FFFFFF"  
    )  
   
    task_listbox.place(x = 10, y = 20) 
    
    retrieve_database()  
    list_update()  
     
    guiWindow.mainloop()  
     
    the_connection.commit()  
    the_cursor.close()
        
        
        
        
        

    
    