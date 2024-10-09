from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import speedtest

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Internet Speed Indicator</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
            <style>
                body { font-family: 'Arial', sans-serif; padding: 20px; background-color: #f8f9fa; }
                .container { max-width: 600px; margin: auto; }
                #results { display: none; margin-top: 20px; }
                #loader { display: none; }
                .error { color: red; }
                @media (max-width: 768px) {
                    .btn { width: 100%; }
                }
            </style>
        </head>
        <body>
            <div class="container text-center mt-5">
                <h1>Internet Speed Test</h1>
                <p>Click the button below to test your internet speed.</p>
                <button class="btn btn-primary btn-lg" onclick="getSpeed()">Test Speed</button>
                
                <div id="loader" class="mt-4">
                    <div class="spinner-border" role="status">
                        <span class="visually-hidden">Loading...</span>
                    </div>
                    <p class="mt-3">Testing your internet speed, please wait...</p>
                </div>
                
                <div id="results" class="mt-4">
                    <h4>Results</h4>
                    <div class="alert alert-success">
                        <strong>Download Speed:</strong> <span id="download-speed"></span> Mbps
                    </div>
                    <div class="alert alert-success">
                        <strong>Upload Speed:</strong> <span id="upload-speed"></span> Mbps
                    </div>
                    <div class="alert alert-info">
                        <strong>Ping:</strong> <span id="ping"></span> ms
                    </div>
                </div>
                
                <div id="error-message" class="alert alert-danger mt-4" role="alert" style="display: none;"></div>
            </div>

            <script>
                function getSpeed() {
                    document.getElementById("loader").style.display = "block";
                    document.getElementById("results").style.display = "none";
                    document.getElementById("error-message").style.display = "none";
                    
                    fetch('/speedtest')
                    .then(response => response.json())
                    .then(data => {
                        document.getElementById("loader").style.display = "none";
                        if (data.error) {
                            document.getElementById("error-message").innerText = "Failed to perform speed test. Please try again.";
                            document.getElementById("error-message").style.display = "block";
                        } else {
                            document.getElementById("results").style.display = "block";
                            document.getElementById("download-speed").innerText = data.download;
                            document.getElementById("upload-speed").innerText = data.upload;
                            document.getElementById("ping").innerText = data.ping;
                        }
                    })
                    .catch(error => {
                        document.getElementById("loader").style.display = "none";
                        document.getElementById("error-message").innerText = "An error occurred: " + error;
                        document.getElementById("error-message").style.display = "block";
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
