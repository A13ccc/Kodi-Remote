from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)

KODI_URL = 'http://192.168.12.248:8080'
KODI_USERNAME = 'alec'
KODI_PASSWORD = '2532'

def send_kodi_command(method, params=[]):
    url = f"{KODI_URL}/jsonrpc"
    headers = {'Content-Type': 'application/json'}
    data = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params,
        "id": 1
    }
    response = requests.post(url, json=data, auth=(KODI_USERNAME, KODI_PASSWORD), headers=headers)
    return response.json()

@app.route('/send_text', methods=['POST'])
def send_text():
    data = request.get_json()
    text = data.get('text')
    if text:
        result = send_kodi_command('Input.SendText', {'text': text, 'done': True})
        return jsonify(result)
    return jsonify({'error': 'No text provided'})

def get_active_player():
    result = send_kodi_command('Player.GetActivePlayers')
    players = result.get('result', [])
    return players[0]['playerid'] if players else None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play_pause')
def play_pause():
    send_kodi_command('Input.ExecuteAction', {'action': 'playpause'})
    return jsonify(success=True)

@app.route('/stop')
def stop():
    send_kodi_command('Input.ExecuteAction', {'action': 'stop'})
    return jsonify(success=True)

@app.route('/input/up')
def input_up():
    send_kodi_command('Input.ExecuteAction', {'action': 'up'})
    return jsonify(success=True)

@app.route('/input/down') 
def input_down():
    send_kodi_command('Input.ExecuteAction', {'action': 'down'})
    return jsonify(success=True)

@app.route('/input/left')
def input_left():
    send_kodi_command('Input.ExecuteAction', {'action': 'left'})
    return jsonify(success=True)

@app.route('/input/right')
def input_right():
    send_kodi_command('Input.ExecuteAction', {'action': 'right'})
    return jsonify(success=True)

@app.route('/input/select')
def input_select():
    send_kodi_command('Input.ExecuteAction', {'action': 'select'})
    return jsonify(success=True)

@app.route('/input/back')
def input_back():
    send_kodi_command('Input.ExecuteAction', {'action': 'back'})
    return jsonify(success=True)

@app.route('/input/home')
def input_home():
    send_kodi_command('Input.Home')
    return jsonify(success=True)

@app.route('/input/volume_up')
def volume_up():
    send_kodi_command('Input.ExecuteAction', {'action': 'volumeup'})
    return jsonify(success=True)

@app.route('/input/volume_down')
def volume_down():
    send_kodi_command('Input.ExecuteAction', {'action': 'volumedown'})
    return jsonify(success=True)

@app.route('/input/context_menu')
def context_menu():
    send_kodi_command('Input.ExecuteAction', {'action': 'contextmenu'})
    return jsonify(success=True)

@app.route('/input/info_menu')
def info_menu():
    try:
        response = send_kodi_command('Input.ExecuteAction', {'action': 'osd'})
        return jsonify(success=response.get('result') is not None)
    except Exception as e:
        return jsonify(success=False, error=str(e))

@app.route('/seek/<action>')
def seek_action(action):
    if action == 'forward':
        send_kodi_command('Input.ExecuteAction', {'action': 'fastforward'})
    elif action == 'backward':
        send_kodi_command('Input.ExecuteAction', {'action': 'rewind'})
    return jsonify(success=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
