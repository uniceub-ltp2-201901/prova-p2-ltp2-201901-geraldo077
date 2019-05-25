'''
Nome: Geraldo Pereira de Castro Junior
RA: 2180259601

'''


from flask import Flask, render_template, request, redirect, url_for
from flaskext.mysql import MySQL
from db import *


app = Flask(__name__)

mysql = MySQL()
mysql.init_app(app)
config(app)

@app.route('/')
def index():
    conn, cursor = get_db(mysql)

    set_ai_key(cursor,  conn)
    generate_id(cursor, conn)
    idnumber = get_id(cursor)


    cursor.close()
    conn.close()

    return render_template('index.html', idnumber=idnumber)

@app.route('/salvar')
def update():

        link = request.args.get('url')
        idnumber = request.args.get('idnumber')


        conn, cursor = get_db(mysql)

        update_link(cursor,conn, idnumber, link)

        cursor.close()
        conn.close()

        return render_template('encurtado.html', link=link)



@app.route('/<idnumber>')
def link_encurtado(idnumber):
    conn, cursor = get_db(mysql)

    link = get_link(cursor, idnumber)[0]
    if link == None:
        return render_template('index.html', error_msg="Id não registrado. Cadastre seu site agora")
    acesscount = get_acesscount(cursor, idnumber)[0]
    acesscount = acesscount + 1
    update_acesscount(cursor, conn, idnumber, acesscount)

    cursor.close()
    conn.close()

    return render_template('encurtado.html', link=link)

if __name__ == '__main__':
    app.run(debug=True)