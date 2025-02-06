# websocket_iitmadras_task
Real-Time Data Display using Flask and WebSocket
This project demonstrates how to send real-time data from a Python Flask server to a web page using WebSockets.
The server generates an array of random float decimals at regular intervals and sends them to the client via WebSocket using Flask-SocketIO. 
The frontend (HTML + JavaScript) listens for incoming data and updates the page continuously without requiring a refresh. 
To set up, install Flask and Flask-SocketIO, then configure the backend to emit data and handle WebSocket connections. 
The frontend uses Socket.IO to receive and display the data. 
The Flask server runs locally, and you can customize the data source or update frequency. 
Troubleshoot by ensuring proper WebSocket connection and verifying JavaScript functionality.

