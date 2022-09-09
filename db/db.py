import  psycopg2
conn = psycopg2.connect(
    host="127.0.0.1",
    database="dvdrental", # database name
    user="postgres", # database user
    password="1234" # database  password
    ) 
# create a cursor
cur = conn.cursor()
        
# execute a statement
print('PostgreSQL database version:')
cur.execute('SELECT version()')
# display the PostgreSQL database server version
db_version = cur.fetchone()
print(db_version)

# create sample table
table = """ CREATE TABLE parts (
                part_id SERIAL PRIMARY KEY,
                part_name VARCHAR(255) NOT NULL
                )
        """
tb = cur.execute(table)
print(tb)

cur.close()
conn.commit()
