from mysql.connector import MySQLConnection, Error
import config
def insert_query(args):
    query = "INSERT INTO health.user_data(age,gender,bmi,children,smoker,region,prediction) VALUES(%s,%s,%s,%s,%s,%s,%s)"
    try:
        conn = MySQLConnection(**config.DB_PARAM)
        print(conn)
        print(f"connection created")
        cursor = conn.cursor()
        print(f"cursor created")

        print(f"record ={args}")
        cursor.execute(query,args)
        print(f"Cursor Excuted")
        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')

        conn.commit()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()
if __name__ == "__main__":
    insert_query((20,"Male",20,0,"No", "Southwest",7500.30))