#!/usr/bin/python -i
############################################################################
#                   sigGen -> SinkSDDS -> SourceSDDS -> plot 
#                          |
#                          -> plot
#############################################################################
from ossie.utils import sb

# connect sig gen to an SDDS sender
siggen = sb.launch('rh.SigGen')
sdds_out = sb.launch('rh.SinkSDDS')
sdds_out.network_settings.interface='lo'
sdds_out.network_settings.ip_address='127.0.0.1' #sender IP
sdds_out.network_settings.port=29000
siggen.connect(sdds_out,providesPortName="dataFloatIn")

# test to make sure sig gen is running
sgplot = sb.LinePlot()
siggen.connect(sgplot,providesPortName="floatIn")


sdds_in = sb.launch("rh.SourceSDDS")
sdds_in.interface="lo"

## SOURCESDDS connection method #1
# this is not necessary if you connect BULKIO ports
#sdds_in.attachment_override.ip_address='127.0.0.1' #sender IP
#sdds_in.attachment_override.port=29000
#sdds_in.attachment_override.enabled=True

## SOURCESDDS connection method #2
## connect SDDS sender (sink) to receiver (source) blocks 
## this is not necessary if you do attach override
sdds_out.connect(sdds_in,providesPortName='dataSddsIn')

# see the data flowing through the source.
sddsplot = sb.LinePlot()
sdds_in.connect(sddsplot,providesPortName='floatIn')


sb.start()
