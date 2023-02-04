import json
import time

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

# This is an infinite loop that continues until the user inputs "exit"
while True:
    # Pause the program for 1.5 seconds
    time.sleep(1.5)
    # Get the user's input
    user_input = input("Enter a keyword, exception, method (or 'exit' to quit, 'list' to see all keywords): ")
    # If the user inputs "exit", break out of the loop
    if user_input.lower() == "exit":
        # original creator :)
        print("Made by Satisfraction: https://github.com/Satisfraction")
        print("Thanks for using!")
        time.sleep(2)
        break
    # If the user inputs "list", print a list of all keywords, exceptions, and methods
    elif user_input == "list":
        print("Keywords:", list_keywords(keywords))
        print("Exceptions:", list_exceptions(exceptions))
        print("Methods:", list_methods(methods))
    # If the user inputs an empty string, print an error message
    elif user_input == "":
        print("Please enter a keyword or 'list'")
    # If the user inputs anything else, prompt them for the category to search in
    else:
        category = input("Which category would you like to search in? (keywords, exceptions, methods): ")
        # If the category is "keywords", search for the keyword in the `keywords` list
        if category.lower() == "keywords":
            result = search_keywords(keywords, user_input)
        # If the category is "exceptions", search for the exception in the `exceptions` list
        elif category.lower() == "exceptions":
            result = search_exceptions(exceptions, user_input)
        # If the category is "methods", search for the method in the `methods` list
        elif category.lower() == "methods":
            result = search_methods(methods, user_input)
        # If the category is anything else, print an error message
        else:
            result = "Invalid category"
        # Print the result of the search
        print("Result:", result)

