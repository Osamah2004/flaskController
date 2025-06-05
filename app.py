from flask import Flask, jsonify, send_from_directory
from flask_socketio import SocketIO, emit
import os
import pyautogui
import webbrowser
import requests
from bs4 import BeautifulSoup

app = Flask(__name__, static_folder="static")
socketio = SocketIO(app)

# Directory containing videos
VIDEO_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "videos")

@app.route("/")
def remote_page():
    return send_from_directory("static", "remote.html")

@app.route("/navigation")
def navigation_page():
    return send_from_directory("static", "navigation.html")

@app.route("/presentation")
def presentation_page():
    return send_from_directory("static", "presentation.html")

@socketio.on("keyboardInput")
def keyboardInput(action):
    pyautogui.press(action)
    print(f"Keyboard input: {action}")
    # Broadcast the action to all connected clients
    emit("keyboardInput", broadcast=True)

@socketio.on("keyDown")
def keyDown(key):
    pyautogui.keyDown(key)
    print(f"Key down: {key}")
    emit("keyDown", broadcast=True)

@socketio.on("keyUp")
def keyUp(key):
    pyautogui.keyUp(key)
    print(f"Key up: {key}")
    emit("keyUp", broadcast=True)

@socketio.on("hotkey")
def hotkey(combination):
    # Split the combination into individual keys
    keys = combination.split('+')
    # Press all keys in sequence
    for key in keys:
        pyautogui.keyDown(key)
    # Release all keys in reverse order
    for key in reversed(keys):
        pyautogui.keyUp(key)
    print(f"Hotkey: {combination}")
    emit("hotkey", broadcast=True)

@socketio.on("deleteLine")
def deleteLine():
    pyautogui.press('end')
    pyautogui.keyDown('shiftleft')
    pyautogui.keyDown('shiftright')
    pyautogui.press('home')
    pyautogui.press('backspace')
    pyautogui.keyUp('shiftleft')
    pyautogui.keyUp('shiftright')
    print("deleteLine")
    # Broadcast the action to all connected clients
    emit("deleteLine", broadcast=True)


@socketio.on("right")
def right():
    pyautogui.press('right')
    print("right")
    # Broadcast the action to all connected clients
    emit("right", broadcast=True)

@socketio.on("left")
def left():
    pyautogui.press('left')
    print("left")
    # Broadcast the action to all connected clients
    emit("left", broadcast=True)

@socketio.on("up")
def up():
    pyautogui.press('up')
    print("up")
    # Broadcast the action to all connected clients
    emit("up", broadcast=True)

@socketio.on("down")
def down():
    pyautogui.press('down')
    print("down")
    # Broadcast the action to all connected clients
    emit("down", broadcast=True)

@socketio.on("open_youtube")
def open_youtube():
    webbrowser.open("https://www.youtube.com")
    print("open_youtube")
    # Broadcast the action to all connected clients
    emit("open_youtube", broadcast=True)

@socketio.on("open_url")
def open_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.p['title-and-badge'])
    # Broadcast the action to all connected clients
    emit("open_url", broadcast=True)
if __name__ == "__main__":
    socketio.run(app, debug=True, host="0.0.0.0", port=5000)

