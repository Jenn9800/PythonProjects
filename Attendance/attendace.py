attendance_records = {}

def mark_attendance(name):
    if name in attendance_records:
        print(f'{name} has already been recorded')
    else:
        attendance_records[name] = 'present'
        print(f'{name} is marked present')

def view_record():
    print("Attendance Record:")
    for name, status in attendance_records.items():
        print(f'{name}: {status}')

def main():
    while True:
        print("\nAttendance Record")
        print("1. Mark Attendance")
        print("2. View Record")
        print("3. Exit")

        user_input = input("Enter your choice: ")

        if user_input == '1':
            name = input("Enter student name: ")
            mark_attendance(name)
        elif user_input == '2':
            view_record()
        elif user_input == '3':
            print('Exit')
            break
        else:
            print('Invalid input')

if __name__ == '__main__':
    main()
