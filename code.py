import pandas as pd
import tkinter as tk
from tkinter import ttk, filedialog

file_path1 = "" # Global variable to store the file path of Excel Data 1
file_path2 = "" # Global variable to store the file path of Excel Data 2
refresh_time = 10

def import_csv_data1():
    global file_path1
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

if file_path:
    file_path1 = file_path
    refresh_data() # Refresh the data immediately
    
def import_csv_data2():
    global file_path2
    file_path = filedialog.askopenfilename(filetypes=[("XLS Files", "*.xls")])
    
if file_path:
    file_path2 = file_path
    refresh_data() # Refresh the data immediately
    
def load_data1():
    global file_path1, df1
    
if file_path1:
    df1 = pd.read_csv(file_path1, skiprows=range(1, 57),header=1)
    display_data(df1, "GRAPH TEC LIVE DATA", tree1)
    left_frame.pack_propagate(False) # Prevent left frame from resizing
    
def load_data2():
    global file_path2, df2
    
if file_path2:
    df2 = pd.read_csv(file_path2,header=1)
    display_data(df2, "ISO TECH LIVE DATA", tree2)
    right_frame.pack_propagate(False) # Prevent right frame from resizing
    
def display_data(df, label, tree):
    tree.delete(*tree.get_children())
    tree["columns"] = list(df.columns)
    tree.heading("#0", text=label)
    for column in df.columns:
        tree.column(column, width=100)
        tree.heading(column, text=column)
        for index, row in df.iterrows():
            values = list(row)
            tree.insert("", tk.END, text="", values=values)
            
def refresh_data():
    load_data1()
    load_data2()
    root.after(1000, refresh_data) # Refresh data every 1 second
    root = tk.Tk()
    root.title("AUTOMATION OF THERMAL CALIBRATION")
    left_frame = tk.Frame(root)# Create a frame for the left side
    left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    right_frame = tk.Frame(root)# Create a frame for the right side
    right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
    tree1 = ttk.Treeview(left_frame)# Create tree view for Excel Data 1 on the left side
    tree1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create a scrollbar for the first treeview
scrollbar1 = ttk.Scrollbar(left_frame, orient=tk.VERTICAL, command=tree1.yview)
scrollbar1.pack(side=tk.RIGHT, fill=tk.Y)
tree1.configure(yscrollcommand=scrollbar1.set)

# Create tree view for Excel Data 2 on the right side
tree2 = ttk.Treeview(right_frame)
tree2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create a scrollbar for the first treeview
scrollbar2 = ttk.Scrollbar(right_frame, orient=tk.VERTICAL, command=tree1.yview)
scrollbar2.pack(side=tk.RIGHT, fill=tk.Y)
tree2.configure(yscrollcommand=scrollbar1.set)

# Button to import Excel Data 1
button1 = tk.Button(left_frame, text="GRAPH TECH DATA ", command=import_csv_data1)
button1.pack(side=tk.TOP)

# Button to import Excel Data 2
button2 = tk.Button(right_frame, text="ISOTECH DATA", command=import_csv_data2)
button2.pack(side=tk.TOP)

# Refresh data every 1 second
root.after(1000, refresh_data)
root.mainloop()
