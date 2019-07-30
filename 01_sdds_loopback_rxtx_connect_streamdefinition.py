#!/usr/bin/python -i
############################################################################
#                   sigGen -> SinkSDDS -> SourceSDDS -> plot 
#                          |
#                          -> plot
#           (using SDDS Stream Definition instead of attach override)
#############################################################################
from ossie.utils import sb
from bulkio.bulkioInterfaces import BULKIO

# connect sig gen to an SDDS sender
siggen = sb.launch('rh.SigGen')
sdds_out = sb.launch('rh.SinkSDDS')
sdds_out.network_settings.interface='lo'
sdds_out.network_settings.ip_address='127.0.0.1'
sdds_out.network_settings.port=29000
siggen.connect(sdds_out,providesPortName="dataFloatIn")

# test to make sure sig gen is running
sgplot = sb.LinePlot()
siggen.connect(sgplot,providesPortName="floatIn")


sdds_in = sb.launch("rh.SourceSDDS")
sdds_in.interface = "lo"
sdds_port=sdds_in.getPort("dataSddsIn")
# Stream Definition:
# id, dataFormat, multicast address, vlan, port, sampleRate, timeTagValid, privateInfo 
sd = BULKIO.SDDSStreamDefinition("big_stream", BULKIO.SDDS_CF, "127.0.0.1", 0, 29000, siggen.sample_rate.__long__(), True, "testing")
attach_id = sdds_port.attach(sd, "username")

## connect SDDS sender (sink) to receiver (source) blocks 
sdds_out.connect(sdds_in,providesPortName='dataSddsIn')

# see the data flowing through the source.
sddsplot = sb.LinePlot()
sdds_in.connect(sddsplot,providesPortName='floatIn')

sb.start()
