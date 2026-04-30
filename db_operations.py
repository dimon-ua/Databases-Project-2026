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
    
        
