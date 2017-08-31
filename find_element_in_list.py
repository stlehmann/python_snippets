"""
This snippet shows how to filter a list by properties of items and retrieve 
the first element which passes the filter. If no element was found the
result will be None.

"""

class Item:
    def __init__(self, name):
        self.name = name
    
items = [Item('Klaus'), Item('Günther'), Item('Detlef')]

def find_item(name):
    return next((item for item in items if item.name == name), None)

# another way would be to use the try except syntax

def find_item(name):
    try:
        return next((item for item in items if item.name == name))
    except StopIteration:
        return
