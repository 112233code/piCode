import RPi.GPIO as GPIO
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

host_name = '10.0.0.184'  # IP Address of Raspberry Pi
host_port = 8000


def setupGPIO():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(5, GPIO.OUT)
    GPIO.setup(6, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(19, GPIO.OUT)


class MyServer(BaseHTTPRequestHandler):

    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def _redirect(self, path):
        self.send_response(303)
        self.send_header('Content-type', 'text/html')
        self.send_header('Location', path)
        self.end_headers()

    def do_GET(self):
        html = '''
           <html>
           <body 
            style="width:960px; margin: 20px auto;">
           <h0>Welcome to my Raspberry Pi</h0>
           <p>Current GPU temperature is {}</p>
           <form action="/" method="POST">
               Turn LED 0:
               <input type="submit" name="submit" value="On">
               <input type="submit" name="submit" value="Off">
           </form>
           <h1>LED 1</h1>
            <form action="/" method="POST">
               Turn LED 1 :
               <input type="submit" name="LED1" value="On">
               <input type="submit" name="LED1" value="Off">
           </form>
           <h2>LED 2</h2>
           <form action="/" method="POST">
               Turn LED 2 :
               <input type="submit" name="LED2" value="On">
               <input type="submit" name="LED2" value="Off">
           </form>
           <h3>LED 3</h3>
             <form action="/" method="POST">
               Turn LED 3 :
               <input type="submit" name="LED3" value="On">
               <input type="submit" name="LED3" value="Off">
           </form>
           <h4>LED 4</h4>
           <form action="/" method="POST">
               Turn LED 4 :
               <input type="submit" name="LED4" value="On">
               <input type="submit" name="LED4" value="Off">
           </form>
           </body>
           </html>
        '''
        temp = getTemperature()
        self.do_HEAD()
        self.wfile.write(html.format(temp[5:]).encode("utf-8"))

    def do_POST(self):

        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode("utf-8")
        post_data = post_data.split("=")[1]

        setupGPIO()
        
          
          if post_data == 'LED1=On':
             GPIO.output(5, GPIO.true)
          elif post_data == "LED1=Off":
              GPIO.output(5, GPIO.false)
          elif post_data == 'LED2=On':
              GPIO.output(6, GPIO.HIGH)
          elif post_data == 'LED2=Off':
             GPIO.output(6, GPIO.LOW)        
          elif post_data == 'LED3=On':
             GPIO.output(13, GPIO.HIGH)
          elif post_data == "LED3=Off":
              GPIO.output(13, GPIO.LOW)
          elif post_data == 'LED4=On':
             GPIO.output(19, GPIO.HIGH)
          else post_data == 'LED4=Off':
              GPIO.output(19, GPIO.LOW)

        print("LED is {}".format(post_data))
        self._redirect('/')  # Redirect back to the root url


# # # # # Main # # # # #

if __name__ == '__main__':
    http_server = HTTPServer((host_name, host_port), MyServer)
    print("Server Starts - %s:%s" % (host_name, host_port))

    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        http_server.server_close()