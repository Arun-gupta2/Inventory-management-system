import sqlite3
def create_db():
    con=sqlite3.connect("./Database/store.db")
    cur=con.cursor()

    cur.execute( "CREATE TABLE IF NOT EXISTS supplier(sup_id varchar(10) PRIMARY KEY, name varchar(10) , contact_num varchar(15) , description varchar(15)  )")
    con.commit()

    #cur.execute( "CREATE TABLE IF NOT EXISTS category(cid INTEGER PRIMARY KEY AUTOINCREMENT ,name text )")
    #con.commit()

    #cur.execute( "CREATE TABLE IF NOT EXISTS product(pid INTEGER PRIMARY KEY AUTOINCREMENT ,Supplier text, Category text , Name text , Price text , qty text , Status text )" )
    #con.commit()

    
create_db()    
