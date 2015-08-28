import db_handler

obj = db_handler.db_handler()
flag=True

while flag:
    chk = input('i(insert)or s(select)or e(exit)\n>>')

    if chk == "i":
        name=input("name>>")
        age=input("age>>")
        obj.__insert__(name, age)

    elif chk =="s":
        obj.__select__()

    elif chk == "e":
        obj.__close__()
        flag=False
                
