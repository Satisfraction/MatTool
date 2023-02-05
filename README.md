# MatTool
This code provides a search interface for keywords, exceptions and methods of Python.


Usage Description (CLI):

This code is a tool that allows the user to search for keywords, exceptions, and methods in JSON files. The code first loads the keywords, exceptions, and methods data from the specified JSON files.

The user is prompted to enter a keyword, exception, method or 'list' to see all keywords. If the user enters 'list', the code will output a list of all keywords, exceptions, and methods. If the user enters a keyword or exception, they will be prompted to choose the category they want to search in (keywords, exceptions, methods). The code will then search for the entered term in the specified category and output the description if it is found, or return "Keyword not found", "Exception not found", or "Method not found" if it is not.

The code will continue to prompt the user for input until the user enters 'exit'.

------------------------------------------------------
Alphatest version of a GUI with kivy is now avaible.
(Only the 'Search' function is working yet. Means you can not list all the "keywords" from the 3 .json files!)

Needs kivy to work!

To install Kivy use:
'pip install kivy'

------------------------------------------------------

Disclaimer:
All files used to fill the JSON files were sourced from the link at "https://www.w3schools.com/python/python_ref_keywords.asp".
