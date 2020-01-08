#! python3
# mcb2.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb2.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb2.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb2.pyw list - Loads all keywords to clipboard.
#        py.exe mcb2.pyw delete <keyword> - Deletes keyword entry.
#        py.exe mcb2.pyw deleteall - deletes all they keywords.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb2')

# Save clipboard content.
if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'delete':
        try:
            del mcbShelf[sys.argv[2]]
        except shelve.error:
            print('ERROR: {}'.format(err))
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1].lower() == 'deleteall':
        for shelvesCount in list(mcbShelf.keys()):
            del mcbShelf[shelvesCount]
        
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
        

mcbShelf.close()
