#define Entries
title_text=StringVar()
el=Entry(Window, textvariable=title_text)
el.grid(row=8,column=1)

Author_text=StringVar()
e2=Entry(Window, textvariable=Author_text)
e2.grid(row=8,column=3)

Year_text=StringVar()
e3=Entry(Window, textvariable=Year_text)
e3.grid(row=8,column=1)

ISBN_text=StringVar()
e4=Entry(Window, textvariable=ISBN_text)
e4.grid(row=8,column=1)
