# ug_tbt2pcie - Desktop Solutions
This is a [Sphinx](https://www.sphinx-doc.org) project that creates the 
user guide for our desktop solution of the time-to-digital converters by
[cronologic GmbH & Co. KG](https://www.cronologic.de/products/products-overview#tdcdata).

This user guide is available at
[docs.cronologic.de](https://docs.cronologic.de/projects/tbt2pcie/en/latest/).

## Setup and installation
A Python installation is necessary to compile the user guide.

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
to compile the project as HTML or PDF. The HTML (PDF) output is in
`build/html/` (`build/latex/`).


## License
![Creative Commons by-nd 4.0](https://i.creativecommons.org/l/by-nd/4.0/88x31.png)

This documentation is licensed under an
[Creative Commons Attribution-NoDerivatives 4.0 International License](https://creativecommons.org/licenses/by-nd/4.0/).
You are free to copy and redistribute the material in any medium or format 
for any purpose (even commercially) unchanged if you give appropriate credit
to cronologic GmbH & Co. KG. A link to [this repository](https://github.com/cronologic-de/ug_tbt2pcie)
or the [product pages](https://www.cronologic.de/products/products-overview)
is sufficient.

If you decide to contribute to this repository you transfer non-exclusive
but unlimited rights to your edit to cronologic GmbH & Co. KG.

The file [extraplaceins.sty](extraplaceins.sty) is in the public domain.
