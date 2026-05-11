from mysql_connection import mydb
import mysql.connector
import error_conditions
from config_neo4j import get_session

# -------------print("1. View Speakers & Sessions") ------------------------
def view_speakers_sessions(input_name):
    mycursor = mydb.cursor()
    
    sql = """
    SELECT speakerName, sessionTitle, roomName 
    FROM session
    INNER JOIN room ON session.roomID = room.roomID
    WHERE speakerName LIKE %s
    """
    
    formatted_search = f"%{input_name}%"
    mycursor.execute(sql, (formatted_search,))
    results = mycursor.fetchall()
    #print(results)
    
    print("-"*95)
    
    if not results:
        print("No speakers found of that name")
    else:
        for row in results: 
            print(f"{row[0]:<35}  |  {row[1]:<35}  |  {row[2]:<35}")       
    mycursor.close()
    
    
# -------------print("2. View Attendees by Company") ------------------------           
def attendees_by_company(company_id):
    mycursor = mydb.cursor()
    
    check_company_id = "SELECT companyName FROM company where companyID = %s"
    mycursor.execute(check_company_id,(company_id,))
    company = mycursor.fetchone()
    
    #print(company[0])    
    #print(type(company[0]))
    
    # Company doesnt exists
    if company is None:
        print(f"Company with ID {company_id} doesn't exist")
        mycursor.close()
        return False
    
    #Company exists
    company_name = company[0]    
    print(f"\n{company_name} Attendees")
        
    sql = """
            SELECT 
            attendee.attendeeName, 
            attendee.attendeeDOB, 
            session.sessionTitle, 
            session.speakerName,
            session.sessionDate,
            room.roomName
            FROM company
            JOIN attendee     ON company.companyID = attendee.attendeeCompanyID
            JOIN registration ON attendee.attendeeID = registration.attendeeID
            JOIN session      ON registration.sessionID = session.sessionID
            JOIN room         ON session.roomID = room.roomID
            WHERE company.companyID = %s
            order by attendee.attendeeName;
            """
                    
    mycursor.execute(sql, (company_id,))
    results = mycursor.fetchall()                
    
    if not results:
        print(f"No attendees found for {company_name}")  
    else:                        
        for row in results:
            print(f"{row[0]:<15}  |  {row[1]}  |  {row[2]:<35}  |  {row[3]:<25}  |  {row[4]}  |  {row[5]:<25}")  
    
    mycursor.close()
    return True       

# -------------print("3. Add New Attendee") ------------------------    
def add_new_attendee(attendee_id, name, dob, gender, company_id):  
    # First my error checks          
    if error_conditions.attendee_exist(attendee_id):
        print(f"\n[!] *** Error *** Attendee ID: {attendee_id} already exists.")
        return 
    
    if not error_conditions.company_exist(company_id):
        print(f"\n[!] *** Error *** Company ID: {company_id} does not exist")
        return
    
    if not error_conditions.gender_exist(gender):
        print(f"\n[!] *** Error *** Gender must be Male/Female.")
        return
    
    # Here MYSQL error checks
    try:    
        mycursor = mydb.cursor()
        
        sql_insert_new_attendee = """
            INSERT INTO attendee(attendeeID, attendeeName, attendeeDOB, attendeeGender, attendeeCompanyID)
            VALUES (%s, %s, %s, %s, %s)
        """
        values = (attendee_id, name, dob, gender, company_id)
            
        mycursor.execute(sql_insert_new_attendee, values)
        mydb.commit()
        
        print(f"\n[+] Attendee {name} successfully added.")
        mycursor.close()
    except mysql.connector.Error as err:
        print(f"*** ERROR *** {err}")
        
# -------------print("4. View Connected Attendees") ------------------------  

def view_connected_attendees(attendee_id):
    cursor = mydb.cursor()
    cursor.execute("SELECT attendeeName FROM attendee WHERE attendeeID = %s", (attendee_id,))
    result = cursor.fetchone()
    
    if result is None:
        print(f"*** ERROR *** Attendee does not exist")
        cursor.close()
        return
    
    #print(result)
    attendee_name = result[0]
    print(f"Attendee Name:  {attendee_name}")
    print("-" * 30)
    
    with get_session() as neo_session:
        query = """
        MATCH (a1:Attendee {AttendeeID: $id})-[:CONNECTED_TO]-(a2:Attendee)
        RETURN a2.AttendeeID AS id
        """
        
        results = neo_session.run(query, id=int(attendee_id))
        connections = list(results)

        if not connections:
            print("No connections")
        else:
            print("These attendees are connected:")
            for record in connections:
                cursor.execute("SELECT attendeeName FROM attendee WHERE attendeeID = %s", (record['id'],))
                name_row = cursor.fetchone()
                name = name_row[0] if name_row else "Unknown"
                print(f"{record['id']}  |  {name}")
    
    cursor.close()
    

# -------------print("5. Add Attendee Connection") ------------------------
def add_attendee_connection(id1, id2):
    cursor = mydb.cursor()
    cursor.execute("SELECT attendeeID FROM attendee WHERE attendeeID IN (%s, %s)", (id1, id2))
    found = cursor.fetchall()
    
    if len(found) < 2:
        print("*** ERROR *** One or both attendee IDs do not exist")
        return False
    
    str_id1 = str(id1)
    str_id2 = str(id2)
        
    with get_session() as session:
        check = "MATCH (a1:Attendee {AttendeeID: $id1})-[r:CONNECTED_TO]-(a2:Attendee {AttendeeID: $id2}) RETURN r"
        if session.run(check, id1=int(id1), id2=int(id2)).single():
            print("*** ERROR *** These attendees are already connected\n")
            return False
        
        query = """
            MERGE (a1:Attendee {AttendeeID: $id1})
            MERGE (a2:Attendee {AttendeeID: $id2})
            CREATE (a1)-[:CONNECTED_TO]->(a2)
            """
        session.run(query, id1=str_id1, id2=str_id2)
        print(f"Attendee {id1} is now connected to Attendee {id2}")
        return True
    
    #print()
    
# -------------print("6. View Rooms") ------------------------   
def view_rooms():
    cursor = mydb.cursor()
    
    cursor.execute("SELECT roomID, roomName, capacity FROM room ORDER BY roomID")
    rooms = cursor.fetchall()
    
    print("\nRoomID  |  RoomName  |  Capacity")
    print("-" * 20)
    for room in rooms:
        print(f"ID: {room[0]} | Name: {room[1]} | Capacity: {room[2]}")
    cursor.close() 