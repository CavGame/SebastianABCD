from flask import Flask, request, jsonify
from minecraft_bot import move_to, build_structure, get_status

app = Flask(__name__)

@app.route('/command', methods=['GET'])
def command():
    command_type = request.args.get('type')

    if command_type == 'move':
        move_to(200, 64, 200)
        return jsonify({'message': 'Il bot si sta muovendo verso la nuova posizione!'})
    elif command_type == 'build':
        build_structure()
        return jsonify({'message': 'Il bot sta costruendo qualcosa!'})
    elif command_type == 'status':
        status = get_status()
        return jsonify({'message': status})
    else:
        return jsonify({'message': 'Comando non riconosciuto.'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
