# websocket_iitmadras_task
Real-Time Data Display using Flask and WebSocket
This project demonstrates how to send real-time data from a Python Flask server to a web page using WebSockets. The server continuously sends an array of random float decimals, and the client updates the displayed data in real-time.

Requirements
Before starting, make sure you have the following installed:

Python 3.x
Flask
Flask-SocketIO
A modern web browser (e.g., Chrome, Firefox, etc.)
Step 1: Install Dependencies
To install the necessary Python libraries, use the following commands:

bash
Copy
pip install flask flask-socketio
These libraries are required to set up the Flask server and handle WebSocket communication.

Step 2: Set Up the Flask Backend
Create a Flask App: Start by creating a Flask app that will serve the webpage and handle WebSocket communication.

Set Up WebSocket: Flask-SocketIO is used to create a WebSocket server. This will allow the server to send data to the client in real-time.

Generate Random Data: Use a function to continuously generate an array of random float decimals at regular intervals (e.g., every second).

Emit Data: Use Flask-SocketIO’s emit() method to send the generated data to the client over the WebSocket connection.

Background Task: Use Flask-SocketIO’s start_background_task() method to keep the data generation running in the background.

Step 3: Set Up the Frontend (HTML + JavaScript)
WebSocket Connection: The frontend will use JavaScript and the Socket.IO library to establish a WebSocket connection to the server.

Display the Data: The data received from the server will be displayed inside an HTML element (e.g., <div id="data-container">). Every time new data is received, the content of this element will be updated.

Continuous Updates: The JavaScript will listen for incoming data, and every time data is received, it will update the page without the need for a manual refresh.

Step 4: Run the Flask Server
Start Flask Server: To start the server, run the Flask application by using the following command in your terminal:

bash
Copy
python app.py
Access the Webpage: Open your web browser and go to http://localhost:5000/ to view the real-time data updates.

Step 5: Troubleshooting
WebSocket Not Connecting: Ensure that the Flask-SocketIO server is running and the WebSocket client (JavaScript) is properly connected to the correct URL (e.g., http://localhost:5000).
Data Not Updating: Check the browser console for any JavaScript errors. Make sure that the Socket.IO library is correctly included in the HTML.
Step 6: Customization
You can customize the data generation logic in the backend to send different kinds of data, such as real sensor readings, data from a file, or any custom data source. You can also adjust the frequency of updates by modifying the sleep interval in the data generation function.
