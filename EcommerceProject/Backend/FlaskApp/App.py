import pyodbc
from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app,origins=['http://localhost:4200'])
conn_str = 'Driver={SQL Server};Server=DESKTOP-PMFB2J2\SQLEXPRESS;Database=furniture;Trusted_Connection=yes;'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/signup', methods=['POST'])
def signup():
    # get registration details from request body
    data = request.json
    customer_email = data.get('customer_email')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    password = data.get('password')
    address = data.get('address')
    postcode = data.get('postcode')
    city = data.get('city')
    phone = data.get('phone')
    print(customer_email)
    print(first_name)
    print(last_name)
    print(password)
    print(address)
    print(postcode)
    print(city)
    print(phone)
    # connect to the database
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    # insert registration details into database
    query = f"INSERT INTO customer(customer_email,first_name,last_name,password,address,postcode,city,phone) VALUES ('{customer_email}', '{first_name}', '{last_name}', '{password}', '{address}', '{postcode}', '{city}', '{phone}')"
    cursor.execute(query)
    conn.commit()
    # close database connection
    cursor.close()
    conn.close()
    # return success message to Angular
    return jsonify({'message': 'Done'})


@app.route('/login', methods=['POST'])
def login():
    # get login details from request body
    data = request.json
    customer_email = data.get('customer_email')
    password = data.get('password')
    print(customer_email)
    print(password)

    # connect to the database
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    # check if customer exists in database
    query = f"SELECT * FROM customer WHERE customer_email='{customer_email}' AND password='{password}'"
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    # return response to Angular based on login status
    if len(rows) == 1:
        response_data = {'message': 'Login successful'}
        return jsonify(response_data)
    else:
        response_data = {'message': 'Login failed'}
        return jsonify(response_data)


if __name__ == "__main__":
    app.run(debug=True)
