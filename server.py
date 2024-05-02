from flask import Flask, request, jsonify
from datetime import datetime
from flask_cors import CORS
from kafka import KafkaProducer
import json
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

app = Flask(__name__)
CORS(app)
producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))


# Simulação de uma senha hashada real num banco
bd_password_hash = "a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3"

def hash_password(password):
    # Criando o objeto para hash
    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    digest.update(password.encode())
    hashed_password = digest.finalize()
    return hashed_password.hex()

@app.route('/produce', methods=['POST'])
def produce():
    data = request.get_json()
    message = data.get('message', None)
    password = data.get('password', None)

    if password:
        # Substituindo a senha pela versão hashada e comparando com a simulação de BD
        hashed_password = hash_password(password)
        data['password'] = hashed_password
        
        if hashed_password == bd_password_hash:
            data['message'] = "Login successful"
        else:
            data['message'] = "Login failed"

    data['timestamp'] = datetime.now().isoformat()

    try:
        # Comunicação com Kafka
        producer.send('user-events', {'value': data})
        producer.flush()
        return jsonify({'status': 'Message sent to Kafka successfully'}), 200
    except Exception as e:
        return jsonify({'error': f'Failed to send message to Kafka: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
