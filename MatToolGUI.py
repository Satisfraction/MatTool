import json
import tkinter as tk


def load_keywords(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

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
        self.geometry("500x500")

        tk.Label(self, text="Enter a keyword, exception, method").pack()
        self.entry = tk.Entry(self)
        self.entry.pack()
        
        self.keywords = load_keywords('python_keywords.json')
        self.exceptions = load_keywords('exception_keywords.json')
        self.methods = load_keywords('method_keywords.json')

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
            search_functions = {
                "keywords": search_keywords,
                "exceptions": search_exceptions,
                "methods": search_methods
            }
            result = search_functions.get(category, lambda x, y: "Invalid category")(eval(category), user_input)

            self.result_label.delete(1.0, tk.END)
            self.result_label.insert(tk.END, result)

        keywords_data = load_keywords('python_keywords.json' and 'exception_keywords.json' and 'method_keywords.json')
        #print(keywords_data)

        def list_keywords(keywords_data):
            return [k["key"] for k in keywords_data]
        
        def list_exceptions(exceptions):
            return [e["exception"] for e in exceptions]

        def list_methods(methods):
            return [m["method"] for m in methods]

        def list_keywords(self):
            category = self.category.get()
            result_text = ""
            if category == "Keywords":
                result_text = "\n".join(list_keywords(self.keywords))
            elif category == "Exceptions":
                result_text = "\n".join(list_exceptions(self.exceptions))
            elif category == "Methods":
                result_text = "\n".join(list_methods(self.methods))
            else:
                result_text = "Invalid category"

            self.result_label.delete(1.0, tk.END)
            self.result_label.insert(tk.END, result_text)


if __name__ == "__main__":       
    app = KeywordSearchApp()
    app.mainloop()