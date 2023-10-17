# ug_tbt2pcie
TBT2PCIe User Guide

## Setup and installation

Optionally, create and activate a virtual environment
```shell
python -m venv .venv
. .\.venv\Scripts\activate
``` 

Install the requirements of the project
```shell
pip install -r requirements.txt
```


After that, run
```shell
make html
```
   or
```shell
make latexpdf
```
to compile the project as html or pdf. The html (pdf) output is in build/html
(build/latex).


## License
This documentation is licensed under an
[Creative Commons Attribution-NoDerivatives 4.0 International License](https://creativecommons.org/licenses/by-nd/4.0/).
You are free to copy and redistribute the material in any medium or format 
for any purpose (even commercially) unchanged if you give appropriate credit
to cronologic GmbH & Co. KG. A link to [this repository](https://github.com/crono-kircher/ug-PCIe-over-USB4) or the [product pages](https://www.cronologic.de/products/products-overview) is sufficient.

If you decide to contribute to this repository you transfer non-exclusive
but unlimited rights to your edit to cronologic GmbH & Co. KG.
![Creative Commons by-nd 4.0](https://i.creativecommons.org/l/by-nd/4.0/88x31.png)

The file [extraplaceins.sty](extraplaceins.sty) is in the public domain.
