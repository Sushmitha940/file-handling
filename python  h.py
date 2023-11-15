import os
while 1:
   a=input('enter the choice')
   def f():
      print("1.create the file")
      print("2.list the file")
      print("3.edit the file")
      print("4.delet the file")
      print("5.read the file")
      print("6.stop the program")
      a=input("enter the choice:")
   match a:
      case '1':
       name=input("enter the file name:")
       name=name+".txt"
       file=open(name,"w")
       print('-------------------')
       print("file created sucessfully")
       print('-------------------')
       f()
      case'2':
         print("reading the file:")
         name=input("enter the file name:")
         name=name+".txt"
         file=open(name,"r")
         print(file.read())
         f()
      case'3':
        path="D:/python.pro"
        files=os.listdir(path)
        for file in files:
            print(file)
        f()
      case'4':
        print("edit the file")
        name=input("enter the file name:")
        name=name+".txt"
        file=open(name,"a")
        (file.write("sushmitha"))
        print("-----------------")
        f()
      case'5':
        print("delete the file")
        name=input("enter the file name")
        name=name+".txt"
        os.remove(name)
        print("file",name,"\ndeleted successfully")
        print("---------------------")
        f()
      case'6':
        print("*****program end********")
   break
    
          
          
        
