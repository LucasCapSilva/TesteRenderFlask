from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  # Usando SQLite como banco de dados
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

@app.route('/items', methods=['GET', 'POST'])
def manage_items():
    if request.method == 'GET':
        items = Item.query.all()
        items_list = [{'id': item.id, 'name': item.name} for item in items]
        return jsonify(items_list)
    if request.method == 'POST':
        data = request.get_json()
        new_item = Item(name=data['name'])
        db.session.add(new_item)
        db.session.commit()
        return jsonify({'message': 'Item created successfully'})

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host='0.0.0.0')
