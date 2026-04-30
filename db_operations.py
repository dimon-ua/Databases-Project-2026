from mysql_connection import mydb

def view_speakers_sessions():
    mycursor = mydb.cursor()
    
    sql = """
    SELECT speakerName, sessionTitle, roomName 
    FROM session
    INNER JOIN room ON session.roomID = room.roomID
    WHERE speakerName LIKE 'Dr.%'
    """

    mycursor.execute(sql)
    results = mycursor.fetchall()
    
    print("-"*95)
        
    for row in results: 
        print(f"{row[0]:<35}  |  {row[1]:<35}  |  {row[2]:<35}")
    
view_speakers_sessions()
