import sqlite3
import time
import datetime

def insertData(searchText,pref,name,url):#daten in SQL Datenbank einfügen

    conn=sqlite3.connect("ChefKochRec.db")
    c=conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS search_req(timestamp integer, date text, searched text, preferences text, recipe text, recipe_url text)""")

    timestamp=int(time.time())#aktuelle Zeit

    date=datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')#unix Zeit in lesbares Datum umwandeln

    c.execute("INSERT INTO search_req VALUES (:timestamp,:date,:searched,:preferences,:recipe,:recipe_url)",{
        'timestamp':timestamp,
        'date':date,
        'searched':searchText,
        'preferences':pref,
        'recipe':name,
        'recipe_url':url})#in SQL Datenbank einfügen

    conn.commit()
    
    

def viewData():#SQL Datenbank anzeigen
    conn=sqlite3.connect("ChefKochRec.db")
    c=conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS search_req(timestamp integer, date text, searched text, preferences text, recipe text, recipe_url text)""")
    
    c.execute("SELECT * FROM search_req")
    list1=c.fetchall()
    print(*list1,sep="\n")#printed liste aber nach jedem komma beginnt eine neue Zeile -> Liste wird ordenlich ausgegeben 

    conn.commit()

def deleteData():#Tabelle löschen
    conn=sqlite3.connect("ChefKochRec.db")
    c=conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS search_req(timestamp integer, date text, searched text, preferences text, recipe text, recipe_url text)""")
    
    c.execute("DELETE from search_req")#" WHERE searched='tomate' OR searched='Gurke'")
    conn.commit()
    
# =============================================================================
# def dorpDataBase():
#     conn=sqlite3.connect("ChefKochRec.db")
#     c=conn.cursor()
#     c.execute("""DROP TABLE search_req""")
#     
# =============================================================================



    #c.execute("INSERT INTO search_req VALUES (?,?,?,?)",(timestamp,date,"tomate","vegan"))#add the generated values to sql
    #conn.commit()

