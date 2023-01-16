import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Lalit1306@",
  # database="mydatabasel"
  database="mydatabasel"
)

mycursor = mydb.cursor()

# mycursor.execute("USE mydatabase")
# mycursor.execute("CREATE TABLE BSE (Date VARCHAR(255), Open VARCHAR(255) ,High VARCHAR(255),Low VARCHAR(255),Close VARCHAR(255),AdjClose VARCHAR(255),Volume VARCHAR(255))")
# mycursor.execute("CREATE TABLE NSE (Date VARCHAR(255), Open VARCHAR(255) ,High VARCHAR(255),Low VARCHAR(255),Close VARCHAR(255),AdjClose VARCHAR(255),Volume VARCHAR(255))")
# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#   print(x)

# CREATE TABLE bse (Date VARCHAR(255), Open VARCHAR(255) ,High VARCHAR(255),Low VARCHAR(255),Close VARCHAR(255),AdjClose VARCHAR(255),Volume VARCHAR(255));
#     
# );
# mycursor.execute("CREATE TABLE ashoka (Date VARCHAR(255), Open VARCHAR(255) ,High VARCHAR(255),Low VARCHAR(255),Close VARCHAR(255),AdjClose VARCHAR(255),Volume VARCHAR(255))")
# import csv
 
# # opening the CSV file
# with open('ashoka.csv', mode ='r') as file:
#   # reading the CSV file
#   csvFile = csv.reader(file)
#   # displaying the contents of the CSV file
#   for lines in csvFile:
#     sql = "INSERT INTO ashoka (Date,Open, High,Low ,Close,AdjClose,Volume) VALUES (%s, %s, %s, %s, %s, %s, %s)"
#     val = (lines[0], lines[1], lines[2],lines[3],lines[4],lines[5],lines[6])
#     mycursor.execute(sql, val)

#     mydb.commit()
#     print(lines)