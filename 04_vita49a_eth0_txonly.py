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

##CONTAINER 1##
from ossie.utils import sb

# connect sig gen to an VITA49 sender
siggen = sb.launch('rh.SigGen')
v49_out = sb.launch('rh.SinkVITA49')
v49_out.network_settings.interface="eth0"
v49_out.network_settings.ip_address="172.17.0.3" #receivers ip
v49_out.network_settings.port=12344
v49_out.network_settings.enable=True
v49_out.force_transmit = True
siggen.connect(v49_out,providesPortName="dataFloat_in")

# test to make sure sig gen is running
sgplot = sb.LinePlot()
siggen.connect(sgplot,providesPortName="floatIn")

sb.start()

