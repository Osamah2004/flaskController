# Flask Controller

A powerful web-based remote control application that allows you to control your PC from any mobile device or web browser. This application provides keyboard control, mouse control, and presentation management capabilities through a modern, responsive web interface.

## Features

### 1. Keyboard Transfer
- Direct keyboard input to your PC
- Key remapping functionality
- Hotkey combinations support
- Key hold mode for continuous key presses (doesn't work for some buttons like backspace or page up/down)
- Persistent settings using local storage (once you disconnect it will resets, it's available to prevent rebinding when you refresh the page)

![image](https://github.com/user-attachments/assets/9967f0bf-9a72-4a76-ac88-caef10b79a9d)

### 2. Mouse Control
- Touch-based mouse pad
- Left, right, and middle click support
- Mouse hold functionality
- Scroll control with customizable speed

![image](https://github.com/user-attachments/assets/53d67643-0b23-4848-b50c-6be2b7153587)

### 3. Presentation Control
- File browser for presentations and documents
- Support for multiple file types (PDF, PPTX, DOC)
- Presentation navigation controls
- Full-screen mode support
- File filtering by type

![image](https://github.com/user-attachments/assets/c0ea2649-c49a-448f-a6ee-5da4e08771c0)
![image](https://github.com/user-attachments/assets/4e4f9d86-3201-4924-855f-afa462e8bf57)



## Technologies Used

- **Backend:**
  - Python
  - Flask
  - Flask-SocketIO
  - PyAutoGUI

- **Frontend:**
  - HTML5
  - JavaScript
  - Socket.IO
  - Tailwind CSS

## Setup

1. Install Python dependencies:
```bash
pip install flask
pip install flask-socketio
pip install pyautogui
```

2. Clone the repository:
```bash
git clone https://github.com/Osamah2004/flaskController.git
```

3. Run the application:
```bash
python app.py
```
or double click the app icon.

4. Access the application:
   - Open your web browser
   - On mobile devices, got to your PC's local IP address (once you open app.py, it will show you the IP address, something that looks like this * Running on http://192.168.x.x:5000)
   - When you go to the link, it should display a page that looks like this

![image](https://github.com/user-attachments/assets/59b4a914-47c0-482b-bdb4-a93f76860a36)
  
## Usage Guide

### Keyboard Transfer
1. Click "Transfer keyboard" to enable keyboard input
2. Use the remap buttons feature to customize key mappings
3. Create hotkey combinations for quick access
4. Use key hold mode for continuous key presses

### Mouse Control
1. Use the touch pad area to move the mouse
2. Tap for left click, long press for right click
3. Use the scroll buttons or pinch gestures for scrolling
4. Adjust mouse speed using the slider

### Presentation Control
1. Add necessary files under presentation folder
2. Browse and filter files by type
3. Open presentations or documents
4. Use navigation controls for slides
5. Access full-screen mode for presentations

## Security Considerations

- The application runs on your local network
- No data is stored on external servers
- All keyboard and mouse inputs are processed locally
- Settings are stored in your browser's local storage

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or suggest features.

