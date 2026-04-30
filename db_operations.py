from mysql_connection import mydb


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
            
            
def attendees_by_company(company_name):
    mycursor = mydb.cursor()
    
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
            
    mycursor.execute(sql, (company_name,))
    results = mycursor.fetchall()    
    
    
    for row in results:
        print(f"{row[0]:<15}  |  {row[1]}  |  {row[2]:<35}  |  {row[3]:<25}  |  {row[4]}  |  {row[5]:<25}")  
    
        
attendees_by_company(2)