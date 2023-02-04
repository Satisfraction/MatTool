import json

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

# Load keywords from a JSON file
def load_keywords(file_path):
    # Open the file and read the contents
    with open(file_path, 'r') as f:
        # Use the json.load() function to parse the contents of the file
        return json.load(f)

# Load the keyword, exception, and method keyword files
keywords = load_keywords('python_keywords.json')
exceptions = load_keywords('exception_keywords.json')
methods = load_keywords('method_keywords.json')

# Search for a keyword in the keyword list
def search_keywords(keywords, search_term):
    # Iterate through each keyword in the list
    for k in keywords:
        # If the keyword matches the search term, return its description
        if k["key"] == search_term:
            return k["description"]
    # If no match is found, return "Keyword not found"
    return "Keyword not found"

# Search for an exception in the exception list
def search_exceptions(exceptions, search_term):
    # Iterate through each exception in the list
    for e in exceptions:
        # If the exception matches the search term, return its description
        if e["exception"] == search_term:
            return e["description"]
    # If no match is found, return "Exception not found"
    return "Exception not found"

# Search for a method in the method list
def search_methods(methods, search_term):
    # Iterate through each method in the list
    for m in methods:
        # If the method matches the search term, return its description
        if m["method"] == search_term:
            return m["description"]
    # If no match is found, return "Method not found"
    return "Method not found"

# Get a list of keywords
def list_keywords(keywords):
    # Return a list of all the keyword names
    return [k["key"] for k in keywords]

# Get a list of exceptions
def list_exceptions(exceptions):
    # Return a list of all the exception names
    return [e["exception"] for e in exceptions]

# Get a list of methods
def list_methods(methods):
    # Return a list of all the method names
    return [m["method"] for m in methods]

class KeywordSearchApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.input_field = TextInput(hint_text='Enter a keyword, exception, method')
        self.result_label = Label(text='', font_size=20)
        layout.add_widget(self.input_field)
        layout.add_widget(Button(text='Search', on_press=self.search))
        layout.add_widget(self.result_label)
        return layout

    def search(self, instance):
        search_term = self.input_field.text
        result = search_keywords(keywords, search_term)
        if result == "Keyword not found":
            result = search_exceptions(exceptions, search_term)
            if result == "Exception not found":
                result = search_methods(methods, search_term)
        self.result_label.text = result

KeywordSearchApp().run()
