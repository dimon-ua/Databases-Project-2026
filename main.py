import mysql_connection
from mysql_connection import mydb

mycursor = mydb.cursor()

sql = """
SELECT speakerName, sessionTitle, roomName 
FROM session
INNER JOIN room ON session.roomID = room.roomID
WHERE speakerName LIKE 'Dr.%'
"""

mycursor.execute(sql)

results = mycursor.fetchall()

print(results)

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
        if choice == 'x':
            break
        else:
            print(f"You selected {choice}")

if __name__ == "__main__":
    main()
    

#select speakername, sessiontitle, roomname from session
#inner join room
#	ON session.roomID = room.roomID
#where speakername like "Dr.%";

