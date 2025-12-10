from flask import Flask, render_template, request
from datetime import datetime
import os

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'wedding_videos'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    # Page 1: Enter Name
    return render_template('index.html')

@app.route('/record')
def record():
    # Page 2: Camera & Recording
    guest_name = request.args.get('name', 'Guest')
    return render_template('record.html', guest_name=guest_name)

@app.route('/upload', methods=['POST'])
def upload_video():
    if 'video' not in request.files:
        return "No video part", 400
    
    file = request.files['video']
    guest_name = request.form.get('guest_name', 'Unknown')
    
    safe_name = "".join([c for c in guest_name if c.isalnum() or c in (' ', '_')]).strip()
    safe_name = safe_name.replace(" ", "_")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{safe_name}.webm"
    
    save_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(save_path)
    
    print(f"✅ Saved video from {guest_name}: {filename}")
    return "Success", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)