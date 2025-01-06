# 과제 1 
def add_contact(name, phone, email=""):
    new_contact = {
        'name' : name,
        'phone' : phone,
        'email' : email
    }
    return new_contact

address_book = []

name = input("이름을 입력하세요: ")
phone = input("전화번호를 입력하세요: ")
email = input("이메일을 입력하세요: ")

new_contact = add_contact(name, phone, email)
address_book.append(new_contact)
print(f'연락처 {name}이(가) 추가되었습니다.')

# 과제 2
def view_contacts():
    if not address_book:
        print('저장된 연락처가 없습니다.')
    else:
        for contact in address_book:
            print(f'이름: {contact['name']}, 전화번호: {contact['phone']}, 이메일: {contact['email']}')
view_contacts()

# 과제 3
def search_contacts(keyword):
    found_contacts = []
    for contact in address_book:
        if keyword.lower() in contact['name'].lower():
            found_contacts.append(contact)

    if found_contacts:
        for contact in found_contacts:
            print(f"이름: {contact['name']}, 전화번호: {contact['phone']}, 이메일: {contact['email']}")
    else:
        print(f"'{keyword}'에 해당하는 연락처가 없습니다.")
keyword = input("검색할 이름을 입력하세요: ")
search_contacts(keyword)

# 과제 4
def delete_contact(name):
    for i in range(len(address_book) - 1, -1, -1):
        if address_book[i]['name'].lower() == name.lower():
            del address_book[i]
            print(f"{name}님의 연락처가 삭제되었습니다.")
            break
    else:
        print(f"{name}님의 연락처를 찾을 수 없습니다.")

    print("현재 주소록:")
    for contact in address_book:
        print(f"이름: {contact['name']}, 전화번호: {contact['phone']}, 이메일: {contact['email']}")
name = input("삭제할 이름을 입력하세요: ")
delete_contact(name)

# 과제 5
def sort_contacts():
    address_book.sort(key=lambda contact: contact['name'])
    print("연락처 목록이 이름 순으로 정렬되었습니다.")

    for contact in address_book:
        print(f"이름: {contact['name']}, 전화번호: {contact['phone']}, 이메일: {contact['email']}")

# 과제 6
def contact_generator():
    for contact in address_book:
        yield contact
contact_iter = contact_generator()

for contact in contact_iter:
    print(f"이름: {contact['name']}, 전화번호: {contact['phone']}")

while True:
    try:
        contact = next(contact_iter)
        print(contact)
    except StopIteration:
        break

# 과제 7
def main():
    address_book = []

    while True:
        print("1. 연락처 추가")
        print("2. 연락처 보기")
        print("3. 연락처 검색")
        print("4. 연락처 삭제")
        print("5. 연락처 정렬")
        print("6. 프로그램 종료")

        choice = input("원하는 기능을 선택하세요: ")

        if choice == '1':
            
            add_contact()
        elif choice == '2':
            
            view_contacts()
        elif choice == '3':
            
            keyword = input("검색할 이름을 입력하세요: ")
            search_contacts(keyword)
        elif choice == '4':
            
            name = input("삭제할 이름을 입력하세요: ")
            delete_contact(name)
        elif choice == '5':
            
            sort_contacts()
        elif choice == '6':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다.")

if __name__ == "__main__":
    main()