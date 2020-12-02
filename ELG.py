import os

arr = ['.doc', '.docx', '.hwp', '.pptx', '.ppt', '.xls', '.pdf', '.ai', '.psd', '.tx', '.bmp', '.gif', '.png', '.jpg', '.jpeg', '.raw', '.tiff', '.was', '.wma', '.mp3', '.mp4', '.mkv', '.avi', '.flv', '.mov', '.7z', '.aip', 'alz', '.egg', '.zip', '.py', '.c', '.cpp', '.java', '.class', '.html', '.ini', '.lnk', '.exe', '.ttf', '.sys', '.dat', 'jar']
forChange = []
link = 'C:\\Users\\Ebaman\\Desktop'
file_list = os.listdir(link)

def isFile(llist): #폴더인지 아닌지를 확인해서 폴더면 noChange에 넣고 확장자가있는 파일이면 forChange에 저장.
    noChange = []
    global forChange
    ffile_list = llist
    global link
    for i in range(0, len(ffile_list)): 
        for j in range(0, len(arr)):
            if ffile_list[i].find(arr[j]) >= 0:
                forChange.append(ffile_list[i])
                                        
    ffile_list_set = set(ffile_list)
    forChange_set = set(forChange)
    noChange_set = set(noChange)

    noChange_set = ffile_list_set - forChange_set
    noChange = list(noChange_set)
    if not len(noChange):
        return
    else:
        for i in range(0, len(noChange)):
            llink = link
            link += '\\' + noChange[i]
            ffile_list = os.listdir(link)
            isFile(ffile_list)
            link = llink
            
            

isFile(file_list)

print(forChange)

