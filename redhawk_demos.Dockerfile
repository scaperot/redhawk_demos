# This file is protected by Copyright. Please refer to the COPYRIGHT file
# distributed with this source distribution.
#
# This file is part of Scaperot's REDHAWK Demos.
#
# REDHAWK Demos is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# REDHAWK Demos is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see http://www.gnu.org/licenses/.
#
FROM geontech/redhawk-development
LABEL name="redhawk-demos" \
	description="REDHAWK demos"


ADD ./01_sdds_loopback_rxtx_connect.py                  /opt/01_sdds_loopback_rxtx_connect.py
RUN chmod a+x /opt/01_sdds_loopback_rxtx_connect.py

ADD ./01_sdds_loopback_rxtx_connect_streamdefinition.py /opt/01_sdds_loopback_rxtx_connect_streamdefinition.py
ADD ./01_sdds_loopback_rxtx_override.py                 /opt/01_sdds_loopback_rxtx_override.py
ADD ./02_sdds_eth0_rxonly_override.py                   /opt/02_sdds_eth0_rxonly_override.py
ADD ./02_sdds_eth0_txonly.py                            /opt/02_sdds_eth0_txonly.py
ADD ./03_vita49a_loopback_rxtx_connect_demo.py          /opt/03_vita49a_loopback_rxtx_connect_demo.py
ADD ./03_vita49a_loopback_rxtx_connect.py               /opt/03_vita49a_loopback_rxtx_connect.py
ADD ./03_vita49a_loopback_rxtx_override.py              /opt/03_vita49a_loopback_rxtx_override.py
ADD ./04_vita49a_eth0_rxonly_override.py                /opt/04_vita49a_eth0_rxonly_override.py
ADD ./04_vita49a_eth0_txonly.py                         /opt/04_vita49a_eth0_txonly.py

CMD ["/bin/bash","-l"]
