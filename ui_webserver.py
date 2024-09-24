import cherrypy
import time
import json


class LiveUpdateUIServer:
    def __init__(self, shm):
        self.shm = shm

    @cherrypy.expose
    def index(self):
        return '''
        <html>
            <body>
                <h1>Live Values</h1>
                <div><b>Data:</b> <pre id="dataDisplay"></pre></div>

                <script>
                    const eventSource = new EventSource('/subscribe');
                    eventSource.onmessage = function(event) {
                        // Display the raw JSON data
                        document.getElementById('dataDisplay').innerText = event.data;
                    };
                </script>
            </body>
        </html>
        '''
    def run_loop(self):
        while self.shm.running.value:
            # Convert dictionary to JSON for streaming
            current_values = json.dumps(self.shm.__dict__)
            print(current_values)
            yield f"data: {current_values}\n\n"
            time.sleep(1)  # Push updates every second

    @cherrypy.expose
    def subscribe(self):
        cherrypy.response.headers['Content-Type'] = 'text/event-stream'
        cherrypy.response.headers['Cache-Control'] = 'no-cache'

        return self.run_loop()

    subscribe._cp_config = {'response.stream': True}