import json
import tkinter as tk
from tkinter import messagebox

def load_keywords(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

keywords = load_keywords('PythonKeywords.json')
exceptions = load_keywords('ExceptionKeywords.json')
methods = load_keywords('MethodKeywords.json')

def search_keywords(keywords, search_term):
    for k in keywords:
        if k["key"] == search_term:
            return k["description"]
    return "Keyword not found"

def search_exceptions(exceptions, search_term):
    for e in exceptions:
        if e["exception"] == search_term:
            return e["description"]
    return "Exception not found"

def search_methods(methods, search_term):
    for m in methods:
        if m["method"] == search_term:
            return m["description"]
    return "Method not found"

def list_keywords(keywords):
    return [k["key"] for k in keywords]

def list_exceptions(exceptions):
    return [e["exception"] for e in exceptions]

def list_methods(methods):
    return [m["method"] for m in methods]

class KeywordSearchApp(tk.Tk):
    
    def __init__(self):
        super().__init__()

        self.title("MatTool for Python Keyword's")
        self.geometry("600x600")

        tk.Label(self, text="Enter a keyword, exception, method").pack()
        self.entry = tk.Entry(self)
        self.entry.pack()

        tk.Label(self, text="Which category would you like to search in?").pack()
        self.category = tk.StringVar()
        tk.Radiobutton(self, text="Keywords", variable=self.category, value="keywords").pack()
        tk.Radiobutton(self, text="Exceptions", variable=self.category, value="exceptions").pack()
        tk.Radiobutton(self, text="Methods", variable=self.category, value="methods").pack()

        tk.Button(self, text="Search", command=self.search).pack()
        tk.Button(self, text="List", command=self.list_keywords).pack()
        self.result_label = tk.Text(self)
        self.result_label.pack()

    def search(self):
        user_input = self.entry.get()
        category = self.category.get()

        if category == "Keywords":
            result = search_keywords(keywords, user_input)
        elif category == "Exceptions":
            result = search_exceptions(exceptions, user_input)
        elif category == "Methods":
            result = search_methods(methods, user_input)
        else:
            result = "Invalid category"

        self.result_label.delete(1.0, tk.END)
        self.result_label.insert(tk.END, result)


        self.result_label.config(text=result)

    def list_keywords(self):
        category = self.category.get()
        if category == "Keywords":
            result = "\n".join(list_keywords(keywords))
        elif category == "Exceptions":
            result = "\n".join(list_exceptions(exceptions))
        elif category == "Methods":
            result = "\n".join(list_methods(methods))
        else:
            result = "Invalid category"

        self.result_label.delete(1.0, tk.END)
        self.result_label.insert(tk.END, result)


        self.result_label.config(text=result)



app = KeywordSearchApp()
app.mainloop()

