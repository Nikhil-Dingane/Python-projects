import os

path=os.getcwd()
list1=os.listdir(path)



for i in range(0,len(list1)):
    print('Name: '+list1[i]+(' Size: '+str(os.path.getsize(os.path.join(path,list1[i])))+' bytes').rjust(40-len(list1[i])))
    
