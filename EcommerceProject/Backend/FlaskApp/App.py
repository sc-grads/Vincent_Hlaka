from flask import Flask, request, jsonify
from flask_cors import CORS
import pyodbc


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

@app.route('/customer/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    # Connect to the database
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    # Delete the customer from the database
    query = f"DELETE FROM customer WHERE customer_id = {customer_id}"
    cursor.execute(query)
    conn.commit()

    # Close the database connection
    cursor.close()
    conn.close()

    # Return success message to Angular
    return jsonify({'message': 'Customer deleted successfully'})


@app.route('/admin-products', methods=['GET'])
def get_products():
    # Connect to the database
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    # Fetch the products from the database
    cursor.execute("SELECT * FROM product")
    products = cursor.fetchall()

    # Close the database connection
    cursor.close()
    conn.close()

    # Return the products as JSON response
    return jsonify(products)

@app.route('/admin-products', methods=['POST'])
def add_product():
    # Get product details from the request body
    data = request.json
    product_name = data.get('product_name')
    product_description = data.get('product_description')
    image1 = data.get('image1')
    price = data.get('price')
    category_id = data.get('category_id')

    # Connect to the database
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    # Insert the new product into the database
    cursor.execute("INSERT INTO product (product_name, product_description, image1, price, category_id) VALUES (?, ?, ?, ?, ?)",
                   product_name, product_description, image1, price, category_id)
    conn.commit()

    # Fetch the generated product_id
    cursor.execute("SELECT SCOPE_IDENTITY()")
    product_id = cursor.fetchone()[0]

    # Close the database connection
    cursor.close()
    conn.close()

    # Return the newly added product as JSON response
    return jsonify({
        'product_id': product_id,
        'product_name': product_name,
        'product_description': product_description,
        'image1': image1,
        'price': price,
        'category_id': category_id
    })

@app.route('/admin-products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    # Connect to the database
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    # Delete the product from the database
    cursor.execute("DELETE FROM product WHERE product_id = ?", product_id)
    conn.commit()

    # Close the database connection
    cursor.close()
    conn.close()

    # Return success message as JSON response
    return jsonify({'message': 'Product deleted successfully'})

@app.route('/admin-products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    # Get product details from the request body
    data = request.json
    product_name = data.get('product_name')
    product_description = data.get('product_description')
    image1 = data.get('image1')
    price = data.get('price')
    category_id = data.get('category_id')

    # Connect to the database
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    # Update the product in the database
    cursor.execute("UPDATE product SET product_name = ?, product_description = ?, image1 = ?, price = ?, category_id = ? WHERE product_id = ?",
                   product_name, product_description, image1, price, category_id, product_id)
    conn.commit()

    # Close the database connection
    cursor.close()
    conn.close()

    # Return success message as JSON response
    return jsonify({'message':'Product updated successfully'})



if __name__ == "__main__":
    app.run(debug=True)
