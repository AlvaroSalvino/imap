from models.connection_options.connection import DBConnectionHandler

db_hande = DBConnectionHandler()
conn1 = db_hande.get_db_connection()
print(conn1)

db_hande.connect_to_db()
conn2 = db_hande.get_db_connection()
print(conn2)
