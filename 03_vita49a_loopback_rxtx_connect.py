#!/usr/bin/python -i
############################################################################
#                   sigGen -> SinkV49 -> SourceV49 -> plot 
#                          |
#                          -> plot
#############################################################################
from ossie.utils import sb

# connect sig gen to an VITA49 sender
siggen = sb.launch('rh.SigGen', instanceName='SigGen_1',configure=False)
siggen.sample_rate = 50000
siggen.frequency   = 5000

v49_out = sb.launch('rh.SinkVITA49',instanceName='SinkVITA49_1',configure=False)
v49_out.network_settings.interface="lo"
v49_out.network_settings.ip_address="127.0.0.1"
v49_out.network_settings.port=12344
v49_out.advanced_configuration.time_between_context_packets = 5
v49_out.network_settings.enable=True

siggen.connect(v49_out,providesPortName="dataFloat_in")

# test to make sure sig gen is running
sgplot = sb.LinePlot()
siggen.connect(sgplot,providesPortName="floatIn")


v49_in = sb.launch("rh.SourceVITA49", instanceName='SourceVITA49_1',configure=False)
v49_in.interface="lo"
v49_in.advanced_configuration.corba_transfer_size = 6000
v49_in.advanced_configuration.buffer_size = 100000


# connect sender (sink) to receiver (source) blocks 
v49_out.connect(v49_in,providesPortName='dataVITA49_in')

# see the data flowing through the source.
v49plot = sb.LinePlot()
v49_in.connect(v49plot,providesPortName="floatIn")


sb.start()
