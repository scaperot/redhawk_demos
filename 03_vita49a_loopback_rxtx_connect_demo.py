#!/usr/bin/python -i
############################################################################
#                   sigGen -> SinkV49 -> SourceV49 -> plot 
#                          |
#                          -> plot
#
#     THE SAD.xml file is from the REDHAWK repos installed by default 
#     on CentOS
#############################################################################
from ossie.utils import sb

sb.loadSADFile('/var/redhawk/sdr/dom/waveforms/rh/vita49_loopback_demo/vita49_loopback_demo.sad.xml')
siggen = sb.getComponent('SigGen_1')
v49_out = sb.getComponent('SinkVITA49_1')
v49_in = sb.getComponent('SourceVITA49_1')

# test to make sure sig gen is running
sgplot = sb.LinePlot()
siggen.connect(sgplot,providesPortName="floatIn")

# see the data flowing through the source.
v49plot = sb.LinePlot()
v49_in.connect(v49plot,providesPortName="floatIn")

sb.start()

