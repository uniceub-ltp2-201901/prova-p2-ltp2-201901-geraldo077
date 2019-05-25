def config(app):

    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
    app.config['MYSQL_DATABASE_DB'] =  'localhost_ly'

def get_db(mysql): 
    conn = mysql.connect()
    cursor = conn.cursor()

    return conn, cursor

def set_ai_key(cursor,conn):
    cursor.execute(f'ALTER TABLE localhost_ly.websites AUTO_INCREMENT=1001')
    conn.commit()

def exclude_formid(cursor, conn):
    cursor.execute(f'DELETE FROM `localhost_ly`.`websites` WHERE `link`="idlink"')
    conn.commit()

def generate_id(cursor, conn):
    cursor.execute(f'INSERT INTO `localhost_ly`.`websites` (`link`) VALUES ("idlink")')
    conn.commit()

def get_link(cursor, idnumber):
    cursor.execute(f'SELECT link FROM localhost_ly.websites WHERE idwebsites={idnumber}')
    link = cursor.fetchone()
    return link

def get_id(cursor):
    cursor.execute(f'SELECT idwebsites FROM localhost_ly.websites WHERE link="idlink"')
    idlink = cursor.fetchone()
    return idlink

def get_acesscount(cursor, idnumber):
    cursor.execute(f'SELECT acesscount FROM localhost_ly.websites WHERE idwebsites = {idnumber}')
    acesscount = cursor.fetchone()
    return acesscount

def update_link(cursor,conn, idnumber, link):
    cursor.execute(f'UPDATE localhost_ly.websites SET link = ("{link}") WHERE idwebsites = {idnumber}')
    conn.commit()

def update_acesscount(cursor,conn, idnumber, acesscount):
    cursor.execute(f'UPDATE localhost_ly.websites SET acesscount = {acesscount} WHERE idwebsites = {idnumber}')
    conn.commit()

