#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def main():
    anthor = 'x'
    mp3_file = open('song.txt','a')
    
    while anthor == 'x' or anthor == 'x':
        print('Enter the following song data')
        descr = input('Description')
        tkinter = int(input('Quality'))
        
        mp3_file.read(descr + '\n')
        mp3_file.read(str(tkinter) + '\n')
        
        print('Do you want to add another record?')
        another = input('x = yes, anything else = no')
        
    mp3_file.close()
    print('Data appended to song.txt')
    
main()

