#define ListBox
list1=Listbox(Window, height=6,width=45)
list1.grid(row=2,column=8,rowspan=6,columnspan=2)

#Atach scrollbar to the ListBox
sb1=Scrollbar(Window)
sb1.grid(row=2,column=8,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)
