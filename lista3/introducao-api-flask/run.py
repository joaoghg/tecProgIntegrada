from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

#Início api calculadora

@app.route('/adicao', methods=['POST'])
def adicao():
    data = request.json
    num1 = data['num1']
    num2 = data['num2']
    resultado = num1 + num2
    return jsonify({'resultado': resultado})

@app.route('/subtracao', methods=['POST'])
def subtracao():
    data = request.json
    num1 = data['num1']
    num2 = data['num2']
    resultado = num1 - num2
    return jsonify({'resultado': resultado})

@app.route('/multiplicacao', methods=['POST'])
def multiplicacao():
    data = request.json
    num1 = data['num1']
    num2 = data['num2']
    resultado = num1 * num2
    return jsonify({'resultado': resultado})

@app.route('/divisao', methods=['POST'])
def divisao():
    data = request.json
    num1 = data['num1']
    num2 = data['num2']
    if num2 == 0:
        return jsonify({'error': 'Divisão por zero não é permitida'})
    resultado = num1 / num2
    return jsonify({'resultado': resultado})

#Fim api calculadora

#Início api usuarios

USER_FILE = "users.json"

def load_users():
    if not os.path.exists(USER_FILE):
        with open(USER_FILE, 'w') as file:
            json.dump([], file)
    with open(USER_FILE, 'r') as file:
        return json.load(file)

def save_users(users):
    with open(USER_FILE, 'w') as file:
        json.dump(users, file)

@app.route('/users', methods=['GET'])
def get_users():
    users = load_users()
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    users = load_users()
    for user in users:
        if user['id'] == user_id:
            return jsonify(user)
    return jsonify({'erro': 'Usuário não encontrado'}), 404

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    users = load_users()
    user_ids = [user['id'] for user in users]
    new_user_id = max(user_ids) + 1 if user_ids else 1
    data['id'] = new_user_id
    users.append(data)
    save_users(users)
    return jsonify(data), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    users = load_users()
    for user in users:
        if user['id'] == user_id:
            user.update(data)
            save_users(users)
            return jsonify(user)
    return jsonify({'erro': 'Usuário não encontrado'}), 404

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    users = load_users()
    for user in users:
        if user['id'] == user_id:
            users.remove(user)
            save_users(users)
            return jsonify({'msg': 'Usuário excluído'})
    return jsonify({'erro': 'Usuário não encontrado'}), 404

#Fim api usuários

#Início api tarefas

TASK_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'w') as file:
            json.dump([], file)
    with open(TASK_FILE, 'r') as file:
        return json.load(file)

def save_tasks(tasks):
    with open(TASK_FILE, 'w') as file:
        json.dump(tasks, file)

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = load_tasks()
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.json
    tasks = load_tasks()
    data['completed'] = False
    tasks.append(data)
    save_tasks(tasks)
    return jsonify(data), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def complete_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            save_tasks(tasks)
            return jsonify(task)
    return jsonify({'erro': 'Tarefa não encontrada'}), 404

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            return jsonify({'msg': 'Tarefa excluída'})
    return jsonify({'erro': 'Tarefa não encontrada'}), 404

#Fim api tarefas

#Início api produtos

PRODUCTS_FILE = "products.json"
CART_FILE = "cart.json"

def load_products():
    if not os.path.exists(PRODUCTS_FILE):
        with open(PRODUCTS_FILE, 'w') as file:
            json.dump([], file)
    with open(PRODUCTS_FILE, 'r') as file:
        return json.load(file)

def save_products(products):
    with open(PRODUCTS_FILE, 'w') as file:
        json.dump(products, file)

def load_cart():
    if not os.path.exists(CART_FILE):
        with open(CART_FILE, 'w') as file:
            json.dump({}, file)
    with open(CART_FILE, 'r') as file:
        return json.load(file)

def save_cart(cart):
    with open(CART_FILE, 'w') as file:
        json.dump(cart, file)

@app.route('/products', methods=['GET'])
def get_products():
    products = load_products()
    return jsonify(products)

@app.route('/products', methods=['POST'])
def add_product():
    data = request.json
    products = load_products()
    data['id'] = len(products) + 1
    products.append(data)
    save_products(products)
    return jsonify(data), 201

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_stock(product_id):
    data = request.json
    products = load_products()
    for product in products:
        if product['id'] == product_id:
            product['stock'] = data['stock']
            save_products(products)
            return jsonify(product)
    return jsonify({'erro': 'Produto não encontrado'}), 404

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    products = load_products()
    for product in products:
        if product['id'] == product_id:
            products.remove(product)
            save_products(products)
            return jsonify({'msg': 'Produto excluído'})
    return jsonify({'erro': 'Produto não encontrado'}), 404

@app.route('/cart', methods=['GET'])
def get_cart():
    cart = load_cart()
    return jsonify(cart)

@app.route('/cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    cart = load_cart()
    products = load_products()
    for product in products:
        if product['id'] == product_id:
            if str(product_id) in cart:
                cart[str(product_id)] += 1
            else:
                cart[str(product_id)] = 1
            save_cart(cart)
            return jsonify({'msg': 'Produto adicionado ao carrinho'})
    return jsonify({'erro': 'Produto não encontrado'}), 404

@app.route('/cart/<int:product_id>', methods=['DELETE'])
def remove_from_cart(product_id):
    cart = load_cart()
    if str(product_id) in cart:
        del cart[str(product_id)]
        save_cart(cart)
        return jsonify({'msg': 'Produto removido do carrinho'})
    return jsonify({'erro': 'Produto não encontrado no carrinho'}), 404

#Fim api produtos

if __name__ == '__main__':
    app.run(debug=True)