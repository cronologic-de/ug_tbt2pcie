Hardware
========

.. _overview_frontback:
.. figure:: _figures/frontback.*

    Front and back panel of the **TBT2PCIe** enclosure.
    The interface at the front panel is the same as the interface of your
    respective TDC board.

Power requirements
------------------

It is possible to supply the **TBT2PCIe** enclosure with
sufficient power via the USB4 connector. If that is the case, the LED next to
the USB4 port (see :numref:`Fig. %s<overview_frontback>`) lights up **green**
(input voltage :math:`>` |usep| 8 |usep| V) and no additional power supply
needs to be connected. If the LED lights up **red**, an external power supply
is necessary.

.. note::
    No external power supply is provided with the **TBT2PCIe** enclosure.

In case an external power supply is necessary, we recommend the
MeanWell GST40A12-P1J (12 |usep| V |usep| DC, 3.34 |usep| A) power supply.
However, any power supply providing
**12** |hyphen| **17.5** |usep| **V** |usep| **DC @ 3** |usep| **A**
with a plug as depicted in :numref:`Fig. %s<p1j>` is sufficient.

If the power supply connected to the EXT PWR socket is sufficient, the LED
next to it will light up **green** (input voltage
:math:`>` |usep| 11.3 |usep| V). If a power supply is connected that does
not provide sufficient power, the LED will light up **red**.

.. note::
    While an external power supply is connected, the **TBT2PCIe** enclosure
    does not draw power via the USB4 port.

.. _p1j:
.. figure:: _figures/powerplug_overview.*

    Requirements for plugs fitting the EXT PWR socket of the
    **TBT2PCIe** enclosure.

Inputs and connectors
---------------------

Refer to the respective user guide of the particular TDC card that is installed
in your **TBT2PCIe** enclosure.

TimeTagger4:
    - `<https://download.cronologic.de/TimeTagger/TimeTagger4_User_Guide.pdf>`_

..
    - *readthedoc hyperlink*
  
xTDC4:
    - `<https://download.cronologic.de/xTDC4-PCIe/xTDC4_User_Guide.pdf>`_

..
    - *readthedoc hyperlink*


Environmental conditions
------------------------
.. note::

    are those values correct? TODO

- Operating temperature range: 5 to 40°C
- Storage temperature range: |hyphen|\ 10 to 60°C
- Relative humidity (non-condensing): :math:`<` 90\%
