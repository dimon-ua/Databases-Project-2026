import mysql_connection
import db_operations 


def display_menu():
    print("Conference Management")
    print("---------------------")
    print("\n")
    print("MENU")
    print("====")
    print("1. View Speakers & Sessions")
    print("2. View Attendees by Company")
    print("3. Add New Attendee")
    print("4. View Connected Attendees")
    print("5. Add Attendee Connection")
    print("6. View Rooms")
    print("x. Exit")

def main():
    while True:
        display_menu()
        choice = input("Select an option: ")
        
        if choice == '1':
            print("\n")
            x = input("Enter speaker name : ")
            print(f"Session Details for : {x}")
            db_operations.view_speakers_sessions(x)
            
        if choice == '2':
            while True:
                company_id = input("Enter company ID : ")
                
                if company_id.isdigit() and int(company_id) > 0:
                    db_operations.attendees_by_company(company_id)   
                    break;
                else:
                    company_id = input("Enter company ID : ")                 
                
        if choice == 'x':
            break
        else:
            pass
            #print(f"You selected {choice}")

if __name__ == "__main__":
    main()
    
