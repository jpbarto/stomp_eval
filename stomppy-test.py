import stomp
import time

class StompListener (object):
    def on_error (self, headers, message):
        print "Received error: {}".format (message)
    def on_message (self, headers, message):
        print "Received message: {}".format (message)

conn = stomp.Connection ()
conn.set_listener ('', StompListener ())
conn.start ()
conn.connect ()

conn.subscribe (destination = '/exchange/amq.topic/a.b.c', ack = 'auto')

conn.send ('hello world', destination = '/exchange/amq.topic/a.b.c')

time.sleep (2)
conn.disconnect ()
