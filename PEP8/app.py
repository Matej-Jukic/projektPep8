import os
import sys
import tkinter as tk
from tkinter import filedialog
from FileParser import treeWalk
from BackupCreator import makeBackup
import argparse


parser = argparse.ArgumentParser(description="GUI/no GUI")
parser.add_argument('-n', '--no_GUI', type=str, help="no GUI")
args = parser.parse_args()

class DirectoryInputApp:
    def __init__(self, master):
        output = [""]
        self.master = master
        master.title("Directory Input App")
        master.geometry("400x400")

        self.label = tk.Label(
            master, 
            text="Enter Directory Path:", 
            font=("Helvetica", 16)
            )
        
        self.label.pack(pady=10)

        self.directory_path = tk.Entry(
            master, 
            font=("Helvetica", 14)
            )
        
        self.directory_path.pack(ipadx=100, ipady=10)

        self.submit_button = tk.Button(
            master, 
            text="Submit", 
            font=("Helvetica", 14), 
            command=self.submit
            )
        
        self.submit_button.pack(pady=20)
        
        self.output_box = tk.Text(
            master, 
            height=10, 
            font=("Helvetica", 14)
            )
        
        self.output_box.pack(
            pady=20, 
            fill=tk.BOTH, 
            expand=True
            )
        
        self.output_scrollbar = tk.Scrollbar(
            self.output_box, 
            width=24,
            cursor="hand2"
            )
        self.output_scrollbar.pack(
            side=tk.RIGHT, 
            fill=tk.Y)
        self.output_box.config(yscrollcommand=self.output_scrollbar.set)
        self.output_scrollbar.config(command=self.output_box.yview)

       

    def submit(self):
        directory_path = self.directory_path.get()        
        self.output = executeJobsOnFiles(directory_path)       
        self.update_slider(self.output)
        
    def update_slider(self, filesList):
        
        self.output_box.delete(1.0, tk.END)
        for element in filesList:
            self.output_box.insert(
                tk.END, 
                f"Edited file: {element}\n"
                )
        print("updated")
        

def executeJobsOnFiles(directory_path):

    makeBackup.createBackupFolder(directory_path)
    output = treeWalk.walkAndExecute(directory_path)
    return output

if args.no_GUI != None:
    output = executeJobsOnFiles(args.no_GUI)
    print(output)

else:
    root = tk.Tk()
    app = DirectoryInputApp(root)
    root.mainloop()
