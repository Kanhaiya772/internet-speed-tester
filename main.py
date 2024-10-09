from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import speedtest

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <html>
        <head>
            <title>Internet Speed Indicator</title>
            <style>
                body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }
                .container { max-width: 500px; margin: auto; }
                #results { display: none; margin-top: 20px; }
                .btn { padding: 12px 25px; font-size: 18px; background-color: #4CAF50; color: white; border: none; cursor: pointer; }
                .btn:hover { background-color: #45a049; }
                #loader { display: none; margin-top: 20px; }
                .loading-text { font-size: 18px; margin-bottom: 10px; }
                .error { color: red; font-weight: bold; margin-top: 20px; }
                @media (max-width: 768px) {
                    .btn { width: 100%; }
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Check Your Internet Speed</h1>
                <button class="btn" onclick="getSpeed()">Test Speed</button>
                <div id="loader">
                    <p class="loading-text">Testing your internet speed...</p>
                    <img src="https://i.gifer.com/YCZH.gif" alt="loading" width="50" />
                </div>
                <div id="results">
                    <h2>Speed Test Results</h2>
                    <p><strong>Download:</strong> <span id="download-speed"></span> Mbps</p>
                    <p><strong>Upload:</strong> <span id="upload-speed"></span> Mbps</p>
                    <p><strong>Ping:</strong> <span id="ping"></span> ms</p>
                </div>
                <p id="error-message" class="error"></p>
            </div>
            <script>
                function getSpeed() {
                    document.getElementById("loader").style.display = "block";
                    document.getElementById("results").style.display = "none";
                    document.getElementById("error-message").innerText = "";
                    
                    fetch('/speedtest')
                    .then(response => response.json())
                    .then(data => {
                        document.getElementById("loader").style.display = "none";
                        document.getElementById("results").style.display = "block";
                        document.getElementById("download-speed").innerText = data.download;
                        document.getElementById("upload-speed").innerText = data.upload;
                        document.getElementById("ping").innerText = data.ping;
                    })
                    .catch(error => {
                        document.getElementById("loader").style.display = "none";
                        document.getElementById("error-message").innerText = "Failed to get speed test results. Please try again.";
                    });
                }
            </script>
        </body>
    </html>
    """

@app.get("/speedtest")
async def speed_test():
    try:
        speed = speedtest.Speedtest()
        speed.get_best_server()
        download_speed = round(speed.download() / 10**6, 2)  # Convert to Mbps
        upload_speed = round(speed.upload() / 10**6, 2)  # Convert to Mbps
        ping = round(speed.results.ping, 2)
        return {"download": download_speed, "upload": upload_speed, "ping": ping}
    except Exception as e:
        return {"error": str(e)}
