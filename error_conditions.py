from mysql_connection import mydb

def company_exist(company_id):
    mycursor = mydb.cursor()
    
    query = "SELECT companyID FROM company WHERE companyID = %s"
    
    mycursor.execute(query, (int(company_id),))
    result = mycursor.fetchone()
    
    mycursor.close()
    
    if result == None:
        return False
    else:
        return True


def attendee_exist(attendee_id):
    mycursor = mydb.cursor()
    
    query = "SELECT attendeeID FROM attendee WHERE attendeeID = %s"
    
    mycursor.execute(query, (attendee_id,))
    result = mycursor.fetchone()
    
    if result == None:
        return False
    else:
        return True


def gender_exist(gender_input):
    genders = ['Male', 'Female']
    
    if gender_input in genders:
        return True
    else:
        return False
