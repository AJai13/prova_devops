from flask import Flask, jsonify
import redis
import requests
import mysql.connector

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

@app.route('/pedido')
def create_pedido():
    cached = cache.get('produto')
    if cached:
        product = eval(cached)
    else:
        r = requests.get('http://produtos:3001/produtos')
        produto = r.json()['produtos'][0]
        cache.set('produto', str(produto))

    db = mysql.connector.connect(
        host="db",
        user="root",
        password="prova_devops",
        database="positivo"
    )
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS pedidos (id INT AUTO_INCREMENT PRIMARY KEY, produto_id INT, quantity INT, total_price INT)")
    cursor.execute("INSERT INTO pedidos (produto_id, quantity, total_price) VALUES (%s, %s, %s)", (produto['id'], 2, produto['price'] * 2))
    db.commit()
    cursor.close()
    db.close()

    return jsonify({
        "pedido_id": 101,
        "produto_id": product['id'],
        "quantity": 2,
        "total_price": product['price'] * 2
    })

app.run(host='0.0.0.0', port=3002)
