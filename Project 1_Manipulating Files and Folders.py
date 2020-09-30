'''
Maniulating Files Folders
-> How to create a new file?
-> How to update a file?
-> How to move a file?
-> How to rename a file?
-> how to delete a file?

Creating new files:open() function:opens a file and returns a file object.

'''
'''

#Create a file

#Steps->
        #Open a file 
        #give name+extension 

fo=open("D:\INS\\exm.txt","w")
fo.write("Hello I am Twinkle Vansjaliya....\n")

#to write multiple lines
#create a list of item..
line_list=["How are you?\n","How is the weather there?\n"]
fo.writelines(line_list)

#update a file

#steps->
#to update a file, we use same steps
#but open the file in append mode.

fo=open("D:\INS\\exm.txt",'a')
fo.write("Hello all.. Welcometo Isb..\n")

#to update with multiple lines
#create a list of item..
line_list=["It is really hot in Ahemedabad..\n","BTW How is your preparation for Gate?\n"]
fo.writelines(line_list)

# use case1
# one file has data for starting 15 days of a month
# other filehas data for next 15 days of a month
# you want to update the data in the older file..

#  Open the first file in append mode
ff=open("D:\INS\\example.txt","a")

#open the second filein read mode
sf=open("D:\INS\\exm.txt","r")
#read data from second file
info=sf.read()
##append the info data in the first file
ff.write(info)
#close both the files
ff.close()
sf.close()
'''
# moving a file
#steps->  # change the location of a file.

#importing useful library
import os#allows you to use operating system dependent functionality
import shutil#used for different operation on files and collections of files.

# new directory formation-> os.mkdir("new_directiry_path")
#os.mkdir("D:\INS\\Folder\\")
#os.mkdir("D:\INS\\Folder1\\")
#shutil.move("D:\INS\\Folder","D:\INS\\Folder1\\")

#to copya file or folder
#shutil.copy("D:\pythonlearn.pdf","D:\INS\\")

#to copy multiplefiles..
#steps
#for every file , copy it...
#file_list=["type all files"]
#for file in file_list:
        #shutil.copy(file,"enter Copy path")

#to rename a file
# change the location from oldyo new

#os.rename("D:\\pythonlearn.pdf","D:\\pythonlearn1.pdf") 

# use case 2
# for 2nd sem_res.jpeg and 3rd sem_res.jpeg rename it to 2nd semester Result.jpeg & 3rd semester Result.jpeg
# we need to make
   # sem_re.jpeg -> semester Result.jpeg
   #that means we need to make
   # D:\\2nd sem_res.jpeg -> D:\\3rd sem_res.jpeg
 #creating a list of the files
#re_files=["D:\\2nd sem_res.jpeg","D:\\3rd sem_res.jpeg"]
#for i in re_files:
          j=i.split(" ")#splitting across a space
          new_path=j[0] + " semester Result.jpeg"#concatenating to get the new path
          #print(new_path)
          os.rename(i,new_path)#renaming

#to delete a file
#seps->
   #make the location available.
os.remove("D:\\mani\\ABc")#File name with path

