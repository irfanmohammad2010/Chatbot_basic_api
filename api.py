from flask import Flask, jsonify, request
import logging

app = Flask(__name__)
data_store = {}
logging.basicConfig(level=logging.INFO)
@app.route('/items', methods=['POST'])
def create_item():
    app.logger.info("Received request body: %s", request.json)
    item_id = request.json.get('id')
    item_data = request.json.get('data')
    data_store[item_id] = item_data
    return jsonify({"message": "Item created", "id": item_id}), 201

@app.route('/items/<item_id>', methods=['GET'])
def get_item(item_id):
    item = data_store.get(item_id)
    if item is None:
        return jsonify({"message": "Item not found"}), 404
    return jsonify({"id": item_id, "data": item}), 200

@app.route('/items/<item_id>', methods=['PUT'])
def update_item(item_id):
    item_data = request.json.get('data')
    if item_id in data_store:
        data_store[item_id] = item_data
        return jsonify({"message": "Item updated", "id": item_id}), 200
    return jsonify({"message": "Item not found"}), 404

@app.route('/items/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    if item_id in data_store:
        del data_store[item_id]
        return jsonify({"message": "Item deleted"}), 200
    return jsonify({"message": "Item not found"}), 404

if __name__ == '__main__':
    app.run(port=5000)
