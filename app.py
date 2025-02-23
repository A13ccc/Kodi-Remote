from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

KODI_URL = 'http://192.168.12.192:8080'
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

def get_active_player():
    result = send_kodi_command('Player.GetActivePlayers')
    players = result.get('result', [])
    return players[0]['playerid'] if players else None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play_pause')
def play_pause():
    player_id = get_active_player()
    if player_id is not None:
        send_kodi_command('Player.PlayPause', {'playerid': player_id})
        return jsonify(success=True)
    return jsonify(success=False, error="No active player")

@app.route('/stop')
def stop():
    player_id = get_active_player()
    if player_id is not None:
        send_kodi_command('Player.Stop', {'playerid': player_id})
        return jsonify(success=True)
    return jsonify(success=False, error="No active player")

@app.route('/input/up')
def input_up():
    send_kodi_command('Input.Up')
    return jsonify(success=True)

@app.route('/input/down') 
def input_down():
    send_kodi_command('Input.Down')
    return jsonify(success=True)

@app.route('/input/left')
def input_left():
    send_kodi_command('Input.Left') 
    return jsonify(success=True)

@app.route('/input/right')
def input_right():
    send_kodi_command('Input.Right')
    return jsonify(success=True)

@app.route('/input/select')
def input_select():
    send_kodi_command('Input.Select')
    return jsonify(success=True)

@app.route('/input/back')
def input_back():
    send_kodi_command('Input.Back')
    return jsonify(success=True)

@app.route('/input/volume_up')
def volume_up():
    player_id = get_active_player()
    if player_id is not None:
        send_kodi_command('Player.SetVolume', {'playerid': player_id, 'volume': 'increment'})
        return jsonify(success=True)
    return jsonify(success=False, error="No active player")

@app.route('/input/volume_down')
def volume_down():
    player_id = get_active_player()
    if player_id is not None:
        send_kodi_command('Player.SetVolume', {'playerid': player_id, 'volume': 'decrement'})
        return jsonify(success=True)
    return jsonify(success=False, error="No active player")


@app.route('/input/context_menu')
def context_menu():
    send_kodi_command('Input.ContextMenu')
    return jsonify(success=True)

@app.route('/seek/<action>')
def seek_action(action):
    player_id = get_active_player()
    if player_id is not None:
        if action == 'forward':
            send_kodi_command('Player.Seek', {'playerid': player_id, 'value': 'smallforward'})
        elif action == 'backward':
            send_kodi_command('Player.Seek', {'playerid': player_id, 'value': 'smallbackward'})
        return jsonify(success=True)
    return jsonify(success=False, error="No active player")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
