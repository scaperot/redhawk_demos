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

################################ Other tips...###############################
## Xauthority work around
# >> xhost +
#
## docker commands
#docker run -it --volume=/tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY geontech/redhawk-development bash
#
## plotting multiple streams with matplotlib
#sgplot._figure.legend((sgplot._plot.lines[0],sgplot._plot.lines[1]),('SigGen Float Output','SourceNic BULKIO Float Output'))
#sgplot._canvas.set_window_title('Sig Gen and SourceNic vs. Time(s)')
#############################################################################

##CONTAINER 2##
from ossie.utils import sb

sdds_in = sb.launch("rh.SourceSDDS")
sdds_in.interface="eth0"

## SOURCESDDS connection
sdds_in.attachment_override.ip_address='172.17.0.3' #sender IP
sdds_in.attachment_override.port=29000
sdds_in.attachment_override.enabled=True

# see the data flowing through the source.
sddsplot = sb.LinePlot()
sdds_in.connect(sddsplot,providesPortName='floatIn')

sb.start()
