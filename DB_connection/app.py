
# Creating the REST API which can fetch and post the data from MySql data base


from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# creating database connections

def db_conn():
    conn = mysql.connector.connect(
        host = '127.0.0.1',
        database = 'practice_db',
        user = 'root',
        password = 'admin'
    )
    return conn

# creating the routes for url or also called as methods
@app.route('/table4', methods=['GET'])
def product_list():
    conn = db_conn()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM table4')
    city = cursor.fetchall()
    conn.close()
    
    return jsonify(city)

@app.route('/table4', methods=['POST'])
def product_new_list():
    conn = db_conn()
    adding_rows = request.json
    col1 = adding_rows['col1']
    col2 = adding_rows['col2']
    cursor = conn.cursor(dictionary=True)
    cursor.execute(f'INSERT INTO table4(col1, col2) values ({col1}, "{col2}") ;')
    conn.commit()
    conn.close()
    
    return jsonify({"message": "added rows succefully"}), 201

if __name__ == "__main__":
    app.run(debug=True)
