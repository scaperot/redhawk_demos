#!/usr/bin/python -i
############################################################################
# Container 1 (172.17.0.2):            # Container 2 (172.17.0.3)
#                                      #
#                 sigGen -> SinkVITA49 #  SourceVITA49 -> plot 
#                          |           #
#                          -> plot     #   
#                                      #
#  DOnt know why i need to force transmit
#############################################################################
#
#                         Wireshark on docker0 interface
#
#############################################################################

##CONTAINER 2##
from ossie.utils import sb
v49_in = sb.launch("rh.SourceVITA49")
v49_in.attachment_override.ip_address="172.17.0.3"
v49_in.attachment_override.port=12344
v49_in.attachment_override.enabled=True
v49_in.interface="eth0"

# see the data flowing through the source.
v49plot = sb.LinePlot()
v49_in.connect(v49plot,providesPortName="floatIn")

sb.start()
