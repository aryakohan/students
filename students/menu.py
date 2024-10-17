
import student_operations as st

while True:
    st.clear()
    print(40*"-")
    print("press A to add a student ")
    print("press F to find student")
    print("press D to delete or move a student ")
    print("press C to change courses")
    print("press L to list students")
    print("press S to save students")
    print("press Q to quit")
    print(40*"-")
    choice=input("enter your choice: ").upper()

    if choice == "A":
        st.add_student()
    elif choice == "F":
        st.find_student()
    elif choice == "D":
        st.remove_student()
    elif choice == "C":
        st.change_courses()
    elif choice == "L":
        st.list_students()
    elif choice == "S":
        st.save_students()
    elif choice == "Q":
        check_save = input("\ndo you want to save?(y/n)").upper()
        if check_save == 'Y' :
            st.save_students()
        break
    else :
        input("\nWrong Choice! press Enter to back to menu ")