import os

arr = []

while True:
    main_file = open("ELG.txt", "r", encoding='UTF8')
    lines = main_file.readlines()
    if not arr: break
    arr.append(lines)
    main_file.close()
    
#print(lines)
print(arr)
'''
file_route = input("경로를 입력하세요: ")
print(os.listdir(file_route))   # 해당 경로에 있는 파일들의 이름이 리스트의 형태로 출력됨
file = input("파일 이름을 입력하세요(확장자까지 모두 입력): ")
file_name, file_Extension = os.path.splitext(file)


for item in arr:
    filename, fileExtension = os.path.splitext(item)
    print('파일명 : ' + filename + '  확장자명 : ' + fileExtension)
    '''