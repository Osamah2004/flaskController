from flask import Flask, send_from_directory
from flask_socketio import SocketIO, emit
import os
import pyautogui
import subprocess

app = Flask(__name__, static_folder="static")
socketio = SocketIO(app)

# Directory containing videos
presentation_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "presentation")

@socketio.on('connect')
def handle_connect():
    print("Client connected")
    emit("getFiles", os.listdir(presentation_dir))

@app.route("/")
def remote_page():
    return send_from_directory("static", "index.html")

@app.route("/keyboard")
def keyboard_page():
    return send_from_directory("static", "keyboard.html")

@app.route("/presentation")
def presentation_page():
    return send_from_directory("static", "presentation.html")

@app.route("/mousepad")
def mousepad_page():
    return send_from_directory("static", "mousepad.html")

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
    keys = combination.split('+')
    pyautogui.hotkey(*keys)
    print(f"Hotkey: {combination}")
    emit("hotkey", broadcast=True)

@socketio.on("deleteLine")
def deleteLine():
    pyautogui.hotkey('shift','del')
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

@socketio.on("backspace")
def backspace():
    pyautogui.press('backspace')
    print("pressed backspace")
    emit("getFiles",os.listdir(presentation_dir),broadcast=True)
    # Broadcast the action to all connected clients
    emit("backspace", broadcast=True)

@socketio.on("openFile")
def openFile(fileName):
    file_path = os.path.join(presentation_dir, fileName)
    try:
        os.startfile(file_path)
        print(f"Opening file: {fileName}")
        emit("fileOpened", fileName, broadcast=True)
    except Exception as e:
        print(f"Error opening file: {e}")
        emit("fileError", str(e), broadcast=True)

@socketio.on("closeFile")
def closeFile():
    try:
        pyautogui.hotkey('alt', 'f4')
        print("Closing current file")
        emit("fileClosed", broadcast=True)
    except Exception as e:
        print(f"Error closing file: {e}")
        emit("fileError", str(e), broadcast=True)

# Mouse pad event handlers
@socketio.on("mouseMove")
def handle_mouse_move(data):
    deltaX = data.get('deltaX', 0)
    deltaY = data.get('deltaY', 0)
    pyautogui.moveRel(deltaX, deltaY)
    emit("mouseMove", data, broadcast=True)

@socketio.on("mouseClick")
def handle_mouse_click():
    print("left click")
    pyautogui.click()
    emit("mouseClick", broadcast=True)

@socketio.on("mouseRightClick")
def handle_mouse_right_click():
    print("right click")
    pyautogui.click(button='right')
    emit("mouseRightClick", broadcast=True)

@socketio.on("mouseMiddleClick")
def handle_mouse_middle_click():
    pyautogui.click(button='middle')
    emit("mouseMiddleClick", broadcast=True)

@socketio.on("mouseDown")
def handle_mouse_down():
    pyautogui.mouseDown(button='left')
    emit("mouseDown", broadcast=True)

@socketio.on("mouseUp")
def handle_mouse_up():
    pyautogui.mouseUp(button='left')
    emit("mouseUp", broadcast=True)

@socketio.on("scrollUp")
def handle_scroll_up(amount):
    pyautogui.scroll(amount)
    emit("scrollUp", amount, broadcast=True)

@socketio.on("scrollDown")
def handle_scroll_down(amount):
    pyautogui.scroll(-amount)
    emit("scrollDown", amount, broadcast=True)

@socketio.on("scroll")
def handle_scroll(data):
    delta = data.get('delta', 0)
    pyautogui.scroll(delta)
    emit("scroll", data, broadcast=True)

if __name__ == "__main__":
    socketio.run(app, debug=True, host="0.0.0.0", port=5000)

