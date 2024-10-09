# Internet Speed Indicator Web App

This is an **Internet Speed Indicator** web application that measures your internet speed (download, upload, and ping) in real-time using Python, FastAPI, and the `speedtest-cli` library. It provides a user-friendly interface with progress indicators and error handling.

## Features

- Real-time internet speed measurement (download, upload, ping).
- Progress loading animation while the test is running.
- Error handling in case of failure.
- Responsive and modern design using HTML and CSS.
- Backend powered by FastAPI and speedtest-cli.
- Interactive frontend using JavaScript and fetch API.

## Tech Stack

- **Backend:** Python (FastAPI)
- **Frontend:** HTML, CSS, JavaScript
- **Speed Test API:** speedtest-cli

## How to Run the Project

### Local Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/<kanhaiya772>/internet-speed-indicator.git
    ```

2. Navigate to the project directory:
    ```bash
    cd internet-speed-indicator
    ```

3. Install the dependencies:
    ```bash
    pip install fastapi uvicorn speedtest-cli
    ```

4. Run the application:
    ```bash
    uvicorn main:app --reload
    ```

5. Open your browser and visit `http://127.0.0.1:8000`.




