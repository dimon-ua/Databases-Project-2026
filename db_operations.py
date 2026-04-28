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
