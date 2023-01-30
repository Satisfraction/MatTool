import json
import time

def load_keywords(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

keywords = load_keywords('MatTool\ExceptionKeywords.json')
exceptions = load_keywords('MatTool\ExceptionKeywords.json')
methods = load_keywords('MatTool\MethodKeywords.json')

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

while True:
    time.sleep(1.5)
    user_input = input("Enter a keyword, exception, method (or 'exit' to quit, 'list' to see all keywords): ")
    if user_input.lower() == "exit":
        break
    elif user_input == "list":
        print("Keywords:", list_keywords(keywords))
        print("Exceptions:", list_exceptions(exceptions))
        print("Methods:", list_methods(methods))
    elif user_input == "":
        print("Please enter a keyword or 'list'")
    else:
        category = input("Which category would you like to search in? (keywords, exceptions, methods): ")
        if category.lower() == "keywords":
            result = search_keywords(keywords, user_input)
        elif category.lower() == "exceptions":
            result = search_exceptions(exceptions, user_input)
        elif category.lower() == "methods":
            result = search_methods(methods, user_input)
        else:
            result = "Invalid category"
        print("Result:", result)
