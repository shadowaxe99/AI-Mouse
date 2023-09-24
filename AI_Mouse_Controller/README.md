# AI Mouse Controller

The AI Mouse Controller is a Python-based application that allows you to control your mouse using voice commands. With this application, you can perform various mouse actions such as moving the mouse, clicking, scrolling, and more, simply by speaking voice commands.

## Installation

To install and run the AI Mouse Controller, follow these steps:

1. Clone the repository to your local machine:
   ```
   git clone https://github.com/shadowaxe99/AI-Mouse.git
   ```

2. Navigate to the 'AI_Mouse_Controller' directory:
   ```
   cd AI_Mouse_Controller
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To use the AI Mouse Controller, follow these steps:

1. Run the main.py file:
   ```
   python main.py
   ```

2. The application will start listening for voice commands. You can speak the following commands to control the mouse:
   - 'start learning': This command will initiate the learning mode. The application will record mouse movement, train the AI model, and move the mouse based on the predicted positions.
   - 'stop learning': This command will stop the learning mode.
   - 'move mouse': This command will allow you to specify the coordinates to move the mouse to. You will be prompted to provide the X and Y coordinates.
   - 'click': This command will perform a left click.
   - 'double click': This command will perform a double click.
   - 'right click': This command will perform a right click.
   - 'scroll': This command will allow you to specify the number of clicks to scroll. You will be prompted to provide the number of clicks.
   - 'exit': This command will exit the application.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
