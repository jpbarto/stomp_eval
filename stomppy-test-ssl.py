import logging
logging.basicConfig ()
logging.getLogger ().setLevel (logging.DEBUG)

import stomp
import ssl

class StompListener (object):
    def on_error (self, headers, message):
        print "Received error: {}".format (message)
    def on_message (self, headers, message):
        print "Received message: {}".format (message)

stomp_hostname = 'localhost'
stomp_port = 61613
stomp_ssl_port = 61614
stomp_destination = '/exchange/amq.topic/a.b.c'
stomp_source = '/exchange/amq.topic/a.b.c'

conn = 0

def start_stomp ():
    global conn
    conn = stomp.Connection (host_and_ports = [(stomp_hostname, stomp_port)])
    conn.start ()
    conn.connect ()

def start_stomp_ssl ():
    global conn
    stop_stomp ()
    conn = stomp.Connection (host_and_ports = [(stomp_hostname, stomp_ssl_port)],
                            use_ssl = True,
                            ssl_version = ssl.PROTOCOL_TLSv1)
    conn.start ()
    conn.connect ()

def stop_stomp ():
    global conn
    if conn == 0:
        return
    conn.disconnect ()
    conn = 0

def send_stomp (message):
    conn.send (message, destination = stomp_destination)

def start_subscribe ():
    conn.set_listener ('', StompListener ())
    conn.subscribe (destination = stomp_source, ack = 'auto')
