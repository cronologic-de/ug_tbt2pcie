Hardware
========

.. _overview_frontback:
.. figure:: _figures/frontback.*

    Front and back panel of the TBT variant of our TDC cards.
    The interface at the front panel is the same as the interface of the
    respective TDC board.

Power requirements
------------------

It is possible to supply the device with sufficient power via the USB4
connector. If that is the case, the LED next to the USB4 port (see
:numref:`Fig. %s<overview_frontback>`) lights up **green** (input voltage
:math:`>` 8 V) and no additional power supply needs to be
connected. If the LED lights up **red**, an external power supply is necessary.

.. note::
    No external power supply is provided with the TBT variants of our TDC
    cards.

In case an external power supply is necessary, we recommend the
`MeanWell GST90A15-P1M <https://www.meanwell-web.com/en-gb/ac-dc-industrial-desktop-adaptor-with-pfc-input-3-gst90a15--p1m>`_
(15 V DC, 6 A) power supply.
However, any power supply providing
**12–20 V DC @ 3 A**
with a plug as depicted in :numref:`Fig. %s<p1j>` is sufficient.

If the power supply connected to the EXT PWR socket is sufficient, the LED
next to it will light up **green** (input voltage
:math:`>` 11.3 V). If a power supply is connected that does
not provide sufficient power, the LED will light up **red**.

.. note::
    While an external power supply is connected, the device does not draw
    power via the USB4 port.

.. _p1j:
.. figure:: _figures/powerplug_overview.*

    Requirements for plugs fitting the EXT PWR socket of the device.

Inputs and connectors
---------------------

For the front-panel connectors, refer to the main user guide of the
particular TDC card in your device.

TimeTagger4:
    - `<https://download.cronologic.de/TimeTagger/TimeTagger4_User_Guide.pdf>`_
  
xTDC4:
    - `<https://download.cronologic.de/xTDC4-PCIe/xTDC4_User_Guide.pdf>`_