import cherrypy
import time
import json
from multiprocessing.sharedctypes import SynchronizedArray



class LiveUpdateUIServer:
    def __init__(self, shm):
        self.shm = shm

    @cherrypy.expose
    def index(self):
        return '''
        <html>
        <head>
            <style>
                #dataDisplay {
                    white-space: pre-wrap;
                    word-wrap: break-word;
                    width: 100%;
                    overflow-wrap: break-word;
                }
            </style>
        </head>
            <body>
                <h1>Live Values</h1>
                <div><b>Data:</b> <pre id="dataDisplay"></pre></div>

                <script>
                    const eventSource = new EventSource('/subscribe');
                    eventSource.onmessage = function(event) {
                        // Display the raw data
                        document.getElementById('dataDisplay').innerText = event.data;
                    };
                </script>
            </body>
        </html>
        '''
    def run_loop(self):
        while self.shm.running.value:
            self.shm.iterations.value += 1
            output = []
            # Convert dictionary to JSON for streaming
            for attr, value in self.shm.__dict__.items():
                output.append(f"{attr}: {value.value}")
            yield f"data: {output}\n\n"
            time.sleep(.25)  # Push updates every second

    @cherrypy.expose
    def subscribe(self):
        cherrypy.response.headers['Content-Type'] = 'text/event-stream'
        cherrypy.response.headers['Cache-Control'] = 'no-cache'

        return self.run_loop()

    subscribe._cp_config = {'response.stream': True}