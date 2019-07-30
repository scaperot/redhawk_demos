#!/usr/bin/python -i
############################################################################
# Container 1:                         # Container 2
#                                      #
#                   sigGen -> SinkSDDS #  SourceSDDS -> plot 
#                          |           #
#                          -> plot     #   
#                                      #
#############################################################################
#
#                         Wireshark on docker0 interface
#                         to see traffic traverse the gateway
#############################################################################

##CONTAINER 1##
from ossie.utils import sb

# connect sig gen to an SDDS sender
siggen = sb.launch('rh.SigGen')
sdds_out = sb.launch('rh.SinkSDDS')
sdds_out.network_settings.interface='eth0'
sdds_out.network_settings.ip_address='172.17.0.3' #receiver IP
sdds_out.network_settings.port=29000
siggen.connect(sdds_out,providesPortName="dataFloatIn")

# test to make sure sig gen is running
sgplot = sb.LinePlot()
siggen.connect(sgplot,providesPortName="floatIn")

sb.start()
