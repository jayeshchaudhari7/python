import mysql.connector
 
dataBase = mysql.connector.connect(
  host ="localhost",                
  user ="user",
  passwd ="password"
)

print(dataBase)
 
dataBase.close()