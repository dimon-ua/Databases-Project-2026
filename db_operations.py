from mysql_connection import mydb
import mysql.connector
import error_conditions

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
    print(results)
    
    print("-"*95)
    
    if not results:
        print("No speakers found of that name")
    else:
        for row in results: 
            print(f"{row[0]:<35}  |  {row[1]:<35}  |  {row[2]:<35}")       
            
# -------------print("2. View Attendees by Company") ------------------------           
def attendees_by_company(company_id):
    mycursor = mydb.cursor()
    
    check_company_id = "SELECT companyName FROM company where companyID = %s"
    mycursor.execute(check_company_id,(company_id,))
    company = mycursor.fetchone()
    
    #print(company[0])    
    #print(type(company[0]))
    
    
    if company is None:
        print(f"Company with ID {company_id} doesn't exist")
    else:
        print(f"\n{company[0]} Attendees")
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
            print(f"No attendees found for {company[0]}")  
        else:                        
            for row in results:
                print(f"{row[0]:<15}  |  {row[1]}  |  {row[2]:<35}  |  {row[3]:<25}  |  {row[4]}  |  {row[5]:<25}")  
            

# -------------print("3. Add New Attendee") ------------------------    
def add_new_attendee(attendee_id, name, dob, gender, company_id):        
    if error_conditions.attendee_exist(attendee_id):
        print(f"\n[!] *** Error *** Attendee ID: {attendee_id} already exists.")
        return 
    
    if not error_conditions.company_exist(company_id):
        print(f"\n[!] *** Error *** Company ID: {company_id} does not exist")
        return
    
    if not error_conditions.gender_exist(gender):
        print(f"\n[!] *** Error *** Gender must beMale/Female.")
    
    
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