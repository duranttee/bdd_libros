from flask import Flask, render_template, request, jsonify, redirect, url_for
import database as dbase  
from product import Product

db = dbase.dbConnection()

app = Flask(__name__)

# Rutas de la aplicación
@app.route('/')
def home():
    products = db['products']
    productsReceived = products.find()
    return render_template('index.html', products=productsReceived)

# Método POST
@app.route('/products', methods=['POST'])
def addProduct():
    products = db['products']
    name = request.form['name']
    author = request.form['author']
    date = request.form['date']
    product_id = request.form['id']

    if name and author and product_id:
        # Comprobar si el ID ya existe en la base de datos
        existing_product = products.find_one({'id': product_id})
        if existing_product:
            return jsonify({'message': 'El ID ya está en uso.'}), 400

        product = Product(product_id, name, author, date)
        products.insert_one(product.toDBCollection())
        return redirect(url_for('home'))
    else:
        return notFound()

# Método DELETE
@app.route('/delete/<string:product_id>')
def delete(product_id):
    products = db['products']
    products.delete_one({'id': product_id})
    return redirect(url_for('home'))

# Método PUT
@app.route('/edit/<string:product_id>', methods=['POST'])
def edit(product_id):
    products = db['products']
    name = request.form['name']
    author = request.form['author']
    date = request.form['date']

    if name and author:
        products.update_one({'id': product_id}, {'$set': {'name': name, 'author': author, 'date': date}})
        return redirect(url_for('home'))
    else:
        return notFound()

@app.errorhandler(404)
def notFound(error=None):
    message = {
        'message': 'No encontrado ' + request.url,
        'status': '404 Not Found'
    }
    response = jsonify(message)
    response.status_code = 404
    return response

if __name__ == '__main__':
    app.run(debug=True, port=5000)
