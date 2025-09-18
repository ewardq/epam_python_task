"""
 - - - - - - - - - - - - - - - - - - - - T A S K  - - - - - - - - - - - - - - - - - - - -
In this kata, your job is to create a class Dictionary which you can add words to and 
their entries. Example:

>>> d = Dictionary()

>>> d.newentry('Apple', 'A fruit that grows on trees')

>>> print(d.look('Apple'))
A fruit that grows on trees

>>> print(d.look('Banana'))
Can't find entry for Banana
 - - - - - - - - - - - - - - - - - - - - T A S K  - - - - - - - - - - - - - - - - - - - -
"""

class Dictionary:
    def __init__(self):
        self.matrix = []
    
    def newentry(self, key, value):
        # Add value to new key entry in dictionary.
        # If key is already present, replace value
        for keyv_entry in self.matrix:
            if keyv_entry[0] == key:
                keyv_entry[1] = value
                return
        
        # Not found. Append new key-value pair.
        self.matrix.append([key, value])

    def look(self, key):
        # Find value stored in provided key.
        # If found, return it.
        # If not found, return error msg.
        for key_entry, value in self.matrix:
            if key_entry == key:
                return value
        return f"Can't find entry for {key}"

def main():
    d = Dictionary()
    d.newentry('Apple', 'A fruit that grows on trees')

    print(d.look('Apple'))   # A fruit that grows on trees
    print(d.look('Banana'))  # Can't find entry for Banana

if __name__ == "__main__":      # pragma: no cover
    main()