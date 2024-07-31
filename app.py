from flask import Flask, request, jsonify, render_template
from datetime import datetime
import os

app = Flask(__name__)

# Directory to store received files
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Data structure to store received messages for channels A to Z and A1 to A11
messages = {f'channel-{chr(i)}': [] for i in range(ord('a'), ord('z') + 1)}
messages.update({f'channel-a{i}': [] for i in range(1, 12)})

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/regz')
def register():
    return render_template('register.html')

@app.route('/adel')
def channel_a():
    return render_template('channel_a.html', messages=messages['channel-a'])

@app.route('/alya')
def channel_b():
    return render_template('channel_b.html', messages=messages['channel-b'])

@app.route('/amanda')
def channel_c():
    return render_template('channel_c.html', messages=messages['channel-c'])

@app.route('/anin')
def channel_d():
    return render_template('channel_d.html', messages=messages['channel-d'])

@app.route('/callie')
def channel_e():
    return render_template('channel_e.html', messages=messages['channel-e'])

@app.route('/cathy')
def channel_f():
    return render_template('channel_f.html', messages=messages['channel-f'])

@app.route('/chelsea')
def channel_g():
    return render_template('channel_g.html', messages=messages['channel-g'])

@app.route('/christy')
def channel_h():
    return render_template('channel_h.html', messages=messages['channel-h'])

@app.route('/chyntia')
def channel_i():
    return render_template('channel_i.html', messages=messages['channel-i'])

@app.route('/daisy')
def channel_j():
    return render_template('channel_j.html', messages=messages['channel-j'])

@app.route('/danella')
def channel_k():
    return render_template('channel_k.html', messages=messages['channel-k'])

@app.route('/eli')
def channel_l():
    return render_template('channel_l.html', messages=messages['channel-l'])

@app.route('/elin')
def channel_m():
    return render_template('channel_m.html', messages=messages['channel-m'])

@app.route('/ella')
def channel_n():
    return render_template('channel_n.html', messages=messages['channel-n'])

@app.route('/feni')
def channel_o():
    return render_template('channel_o.html', messages=messages['channel-o'])

@app.route('/fiony')
def channel_p():
    return render_template('channel_p.html', messages=messages['channel-p'])

@app.route('/flora')
def channel_q():
    return render_template('channel_q.html', messages=messages['channel-q'])

@app.route('/freya')
def channel_r():
    return render_template('channel_r.html', messages=messages['channel-r'])

@app.route('/gendis')
def channel_s():
    return render_template('channel_s.html', messages=messages['channel-s'])

@app.route('/gita')
def channel_t():
    return render_template('channel_t.html', messages=messages['channel-t'])

@app.route('/gracia')
def channel_u():
    return render_template('channel_u.html', messages=messages['channel-u'])

@app.route('/gracie')
def channel_v():
    return render_template('channel_v.html', messages=messages['channel-v'])

@app.route('/greesel')
def channel_w():
    return render_template('channel_w.html', messages=messages['channel-w'])

@app.route('/indah')
def channel_x():
    return render_template('channel_x.html', messages=messages['channel-x'])

@app.route('/indira')
def channel_y():
    return render_template('channel_y.html', messages=messages['channel-y'])

@app.route('/jessi')
def channel_z():
    return render_template('channel_z.html', messages=messages['channel-z'])

@app.route('/atin')
def channel_a1():
    return render_template('channel_a1.html', messages=messages['channel-a1'])

@app.route('/lia')
def channel_a2():
    return render_template('channel_a2.html', messages=messages['channel-a2'])

@app.route('/lulu')
def channel_a3():
    return render_template('channel_a3.html', messages=messages['channel-a3'])

@app.route('/lyn')
def channel_a4():
    return render_template('channel_a4.html', messages=messages['channel-a4'])

@app.route('/marsha')
def channel_a5():
    return render_template('channel_a5.html', messages=messages['channel-a5'])

@app.route('/michie')
def channel_a6():
    return render_template('channel_a6.html', messages=messages['channel-a6'])

@app.route('/muthe')
def channel_a7():
    return render_template('channel_a7.html', messages=messages['channel-a7'])

@app.route('/olla')
def channel_a8():
    return render_template('channel_a8.html', messages=messages['channel-a8'])

@app.route('/oniel')
def channel_a9():
    return render_template('channel_a9.html', messages=messages['channel-a9'])

@app.route('/raisha')
def channel_a10():
    return render_template('channel_a10.html', messages=messages['channel-a10'])

@app.route('/zee')
def channel_a11():
    return render_template('channel_a11.html', messages=messages['channel-a11'])

# Dynamic route to handle all channels from A to Z and A1 to A11
@app.route('/receive/<channel>', methods=['POST'])
def receive_message(channel):
    if channel not in messages:
        return jsonify({'status': 'error', 'message': 'Channel not found'}), 404

    data = request.get_json()
    file_url = data.get('url')
    username = data.get('username')

    # Add a timestamp for when the message is received
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Save message data to the data structure for the specified channel
    messages[channel].append({
        'username': username,
        'url': file_url,
        'time': current_time  # Add the timestamp
    })
    return jsonify({'status': 'success', 'message': f'Data received successfully for {channel}'}), 200

if __name__ == '__main__':
    app.run(debug=True)
