from flask import Flask, jsonify, send_from_directory
from flask_socketio import SocketIO, emit
import os
import pyautogui

app = Flask(__name__, static_folder="static")
socketio = SocketIO(app)

# Directory containing videos
VIDEO_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "videos")

@app.route("/")
def tv_page():
    return send_from_directory("static", "tv.html")

@app.route("/remote")
def remote_page():
    return send_from_directory("static", "remote.html")

@app.route("/videos")
def list_videos():
    """Returns a JSON list of all MP4 files in the videos directory."""
    files = [file for file in os.listdir(VIDEO_DIR) if file.endswith(".mp4")]
    return jsonify(files)

@app.route("/videos/<filename>")
def serve_video(filename):
    """Serves an individual MP4 file."""
    return send_from_directory(VIDEO_DIR, filename)

@socketio.on("control")
def handle_control(data):
    """Handle control commands and simulate keyboard presses."""
    action = data.get('action')
    
    if action == 'prev':
        pyautogui.press('left')
    elif action == 'next':
        pyautogui.press('right')
    
    # Broadcast the action to all connected clients
    emit("control", data, broadcast=True)

if __name__ == "__main__":
    socketio.run(app, debug=True, host="0.0.0.0", port=5000)

