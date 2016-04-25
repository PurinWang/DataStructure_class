from Module import *

def htmlchecker(html):
    pre = html.count("<")
    pas = html.count("</")
    tail = html.count(">")
    while pre / 2 == pas and pre == tail:
        return True
    return False

print(htmlchecker("<html> <head> <title> Example </title> </head> <body> <h1>Hello, world</h1> </body> </html>"))

