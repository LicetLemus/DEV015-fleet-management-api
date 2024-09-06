# from sqlalchemy import create_engine, text


# DATABASE_URL = "" # The URL of the database   

# engine = create_engine(DATABASE_URL) # create_engine: is used to create a new database connection


# try:
#     connection = engine.connect() # engine.connect: is used to connect to the database
#     print("Connected to database")
#     print(connection)
    
#     #connection.execute: is used for execute a SQL query in the database, in this case, we are using the text function to pass the query as a string
#     # text: is used to create a new plain-text SQL expression
#     # SELECT table_name FROM information_schema.tables WHERE table_schema = 'public': is a query to get the table names in the public schema    
#     # return a ResultProxy object: example: <sqlalchemy.engine.result.ResultProxy object at 0x7f8b1c1b3d90> if the query is successful
    
#     result = connection.execute(text("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'"))
#     print(result)
    
#     # print of the table names
#     print("Tablas en la base de datos:")
#     for row in result:
#         print(row[0])  # row[0] is the first row of the result
    
# except Exception as e:
#     print("Error al conectar con la base de datos ", e)


# For close the connection: connection.close()