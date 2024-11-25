"""
This script defines a function `classify_file` that classifies a file based on its extension.
It demonstrates the use of string methods like `rfind()` and conditional statements to determine the file type.

Steps:
1. The function `classify_file(filename)`:
   - Uses `rfind('.')` to locate the last occurrence of the dot in the filename, which separates the file name from its extension.
   - If no dot is found (`rfind` returns `-1`), the function returns "Unknown file type."
   - Extracts the file extension using slicing and checks it against known extensions.
   - Returns a string indicating the type of file based on its extension.
"""
def classify_file(filename):
    dot_position = filename.rfind('.')
    
    if dot_position == -1:
        return "Unknown file type."
    
    extension = filename[dot_position:]
    
    if extension in ['.jpg', '.jpeg', '.png']:
        return "Image file"
    elif extension in ['.doc', '.docx']:
        return "Document file"
    elif extension == '.pdf':
        return "PDF file"
    elif extension == '.txt':
        return "Text file"
    else:
        return "Unknown file type."
    
result = classify_file('example.jpg')
print(result)
