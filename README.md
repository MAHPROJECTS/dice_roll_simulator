DICE ROLL SIMULATOR

In this project, I used Python to create a simple dice roll simulator. I built the GUI with Tkinter, and used the random module to simulate dice rolls based on probability. I also managed image assets carefully, handling file paths and errors, and used Pillow to display dice images dynamically. Throughout the project, I applied problem-solving skills to break down a visual idea into a working program, resulting in a straightforward but functional dice roll simulator.

FEATURES
Graphical user interface (GUI) implemented with Tkinter for event-driven user interaction.

Dice roll simulation leveraging Python’s random module to generate pseudo-random integers representing dice outcomes, accurately modeling probability distribution.

Dynamic image rendering using the Pillow (PIL) library to update dice face visuals based on roll results.

Comprehensive file management including asset organization, path resolution, and error handling to ensure reliability across different environments.

Modular code structure facilitating maintainability and potential future extensions.

INSTALLATION
Clone the repository (or download the project files) to your local machine.

Ensure you have Python 3 installed. You can download it from python.org.

Install required Python packages using pip. Open your terminal or command prompt and run:

bash
Copy
Edit
pip install Pillow
Note: Tkinter usually comes pre-installed with Python. If you don’t have it, install it via your system package manager:

On Ubuntu/Debian: sudo apt-get install python3-tk

On Windows and macOS, Tkinter should be included by default.

Place your dice image files (dice_1.png to dice_6.png) in the same folder as the Python script.

Run the script from your terminal or in your IDE (like VSCode):

bash
Copy
Edit
python dice_simulator.py

USAGE
Run the Python script:

bash
Copy
Edit
python dice_simulator.py
The GUI window will open displaying the default dice face.

Click the “Roll Dice” button to simulate a dice roll.

Each click randomly selects a dice face image and updates the display accordingly.

Close the window to exit the application.

FUTURE POSSIBLE IMPROVEMENTS
To improve this project, I could simulate multiple dice rolls and analyse the frequency of each outcome to better understand the probabilities. I could also store the roll history in a list or save it to a log file for tracking past results. Additionally, adding data visualization with a library like Matplotlib would allow me to graph the dice rolls and provide insightful analytics. 

LICENSE: MIT
