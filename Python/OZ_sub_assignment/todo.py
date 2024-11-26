import json
import os

TASK_FILE ='tasks.jason'

def load_task():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'r', encoding='utf-8') as file:
            return json.load(file)
    return []

def save_task(tasks):
    with open(TASK_FILE, 'w', encoding='utf=8')as file:
        json.dump(tasks, file, indent=4, ensure_ascii= False)

def add_task(task_name):
    tasks = load_task()
    task = {'name': task_name, 'completed':False}
    tasks.append(task)
    save_task(tasks)

def view_task():
    pass

def complete_task(task_number):
    pass

def delete_task(task_num):
    pass

def show_menu(): #메뉴를 보여주는 함수
    print("작업 관리 애플리케이션")
    print('1. 할 일 추가')
    print('2. 할 일 목록보기')
    print('3. 할 일 완료')
    print('4. 할 일 삭제')
    print('5. 종료')

def main():
    while True:
        show_menu()
        choice = input('원하는 작업을 선택하세요(1~5): ')

        if choice == '1' :
            task_name = input('추가할 작업을 입력해주세요')
            add_task(task_name)

        elif choice == '2':
            view_task()

        elif choice == '3':
            task_number = int(input('완료를 원하는 작업의 번호를 입력해주세요'))
            complete_task(task_number)
        elif choice == '4':
            task_number = int(input('삭제를 원하는 작업의 번호를 입력해주세요'))
            delete_task(task_number)
        elif choice == '5':
            print('시스템을 종료합니다.')
            break
        else:
            print('잘못 입력하셨습니다. 1~5번까지의 기능 중 하나를 선택해주세요.')
main()