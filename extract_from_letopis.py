# -*- coding: utf-8 -*-
#Script that can open a file (UTF-8, Cyrillic and Latin characters, integers),
#search each line for multiple keywords, save line to a new txt file if it has the keyword,
#move on to next line.

#Prompt entry of file names.
#Original file
x = raw_input('Enter file name:')

#Output file
newfile = raw_input('Enter name for output file:')

#Open file
searchfile = open(x, "r")

#How to state encoding?

#Search and print lines to newfile
for line in searchfile:
#    if "Iunost" - followed by either ", ", ". " or " " + four integers in line (regex?):
        f = open(newfile, 'w')
        f.write(line) #This too will be in cyrillic. Is that a problem?
        f.close()
        break
#repeat operation for "Знамя," "Дружба народов," "Октябрь", "Наш современник", "Молодая гвардия", "Новый мир"

searchfile.close()