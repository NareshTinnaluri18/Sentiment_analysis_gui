import tkinter as tk
from tkinter import filedialog
import pandas as pd

class CSVViewer:
    def __init__(self, master):
        self.master = master
        master.title("CSV Viewer")
        master.geometry("800x600")

        self.label = tk.Label(master, text="Select a CSV file to view:")
        self.label.pack()

        self.button = tk.Button(master, text="Browse", command=self.browse_file)
        self.button.pack()

    def browse_file(self):
        filename = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if filename:
            self.data = pd.read_csv(filename, encoding='ISO-8859-1')
            self.responses = self.data['Text']
            self.file_label = tk.Label(self.master, text=f"File: {filename}")
            self.file_label.pack()
            self.table_frame = tk.Frame(self.master)
            self.table_frame.pack()
            for i, value in enumerate(self.responses.values):
                cell_label = tk.Label(self.table_frame, text=value, relief="solid", borderwidth=1)
                cell_label.grid(row=i, column=0)
                cell_label.bind("<Button-1>", lambda event, response=value: self.show_response(response))

    def show_response(self, response):
        response_window = tk.Toplevel(self.master)
        response_window.geometry("400x300")
        response_label = tk.Label(response_window, text=response)
        response_label.pack()

if __name__ == '__main__':
    root = tk.Tk()
    app = CSVViewer(root)
    root.mainloop()
