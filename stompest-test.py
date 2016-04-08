import logging
logging.basicConfig ()
logging.getLogger ().setLevel (logging.DEBUG)

from stompest.config import StompConfig
from stompest.protocol import StompSpec
from stompest.sync import Stomp

"""stomp_uri is of the format 'tcp://<host>:<port>'"""
stomp_uri = 'tcp://127.0.0.1:61613'
"""stomp_destination is of the format '/exchange/<exchange-name>/<routing-key>'"""
stomp_destination = '/exchange/amq.topic/a.b.c'
stomp_source = '/exchange/amq.topic/a.b.c'

def send_stomp (message):
    config = StompConfig (stomp_uri)
    client = Stomp (config)
    client.connect ()
    client.send (stomp_destination, message)
    client.disconnect ()

def recv_stomp ():
    config = StompConfig (stomp_uri)
    client = Stomp (config)
    client.connect ()
    client.subscribe (stomp_source, {StompSpec.ACK_HEADER: StompSpec.ACK_CLIENT_INDIVIDUAL})
    frame = client.receiveFrame ()
    print "Received: {}".format (frame.info ())
    client.ack (frame)
    client.disconnect ()
