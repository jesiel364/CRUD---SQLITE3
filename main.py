from flask import Flask, render_template, request, redirect, flash, url_for
from markupsafe import escape
import sqlite3 as sql


app = Flask(__name__)


@app.route('/')
def index():
    conn = sql.connect('records.db')
    conn.row_factory=sql.Row
    cur = conn.cursor()
    cur.execute("select * from artist")
    data = cur.fetchall() 
	cur2 = conn.cursor()
	cur2.execute("select * from track")
    data2 = cur.fetchall()
    return render_template('home.html', data=data,data2=data2)

@app.route('/artist_info/<string:id>', methods=['POST', 'GET'])
def artist_info(id):
    conn = sql.connect('records.db')
    conn.row_factory=sql.Row
    cur = conn.cursor()
    cur.execute("select * from artist where artist_id=?", id)
    data = cur.fetchone()
    return data['artist_name']

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
