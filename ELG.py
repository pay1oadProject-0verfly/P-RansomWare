import os

arr = ['.doc', '.docx', '.hwp', '.pptx', '.ppt', '.xls', '.pdf', '.ai', '.psd', '.tx', '.bmp', '.gif', '.png', '.jpg', '.jpeg', '.raw', '.tiff', '.was', '.wma', '.mp3', '.mp4', '.mkv', '.avi', '.flv', '.mov', '.7z', '.aip', 'alz', '.egg', '.zip', 'py', 'c', 'cpp', 'java', 'class', 'html', '.ini', 'lnk']

forChange = []
noChange = []

#while True:

a = 'C:\\Users\\Ebaman\\Desktop\\
a += 'ELG.txt'

i = 0
j = 0

print(os.path.isfile(a))


path_dir = 'C:\\Users\\Ebaman\\Desktop'
 
file_list = os.listdir(path_dir)

def isFile(): #폴더인지 아닌지를 확인해서 폴더면 noChange에 넣고 확장자가있는 파일이면 forChange에 저장.
    for i in range(0, len(file_list)): 
        for j in range(0, len(arr)):
            if file_list[i].find(arr[j]) >= 0:
                forChange.append(file_list[i])
                
    file_list_set = set(file_list)
    forChange_set = set(forChange)
    noChange_set = set(noChange)

    noChange_set = file_list_set - forChange_set
    noChange = list(noChange_set)
    

print(forChange)
print("-----------------------------------------------------------------------------------")
print(noChange)


#print(len(file_list))
'''
    for file in os.listdir("C:\\Users\\Ebaman\\Desktop"):
        if file.endswith(".txt"):
            print(os.path.join("C:\\Users\\Ebaman\\Desktop", file))       '''
