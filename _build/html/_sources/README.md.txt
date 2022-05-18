# The MEGA65 Welcome Guide

This is the source repository for the MEGA65 Welcome Guide, a booklet for new owners of the [MEGA65 personal computer](https://mega65.org/).

To read this booklet, visit: https://dansanderson.com/mega65/welcome/

## Reporting an issue with the Welcome Guide

If you have a bug report or feature request for the Welcome Guide, [report an issue](https://github.com/dansanderson/mega65-welcome-guide/issues) or just [email me](mailto:contact@dansanderson.com).

Pull requests are welcome for minor fixes. If you want to make major changes or additions, please file an issue first so we can discuss it.

The goal of the Welcome Guide is to make things easier for new owners of the Mega65 while the early stage hardware and software are being improved. It is not intended to be a complete description of new features and improvements added since the Mega65 was released. As the official documentation catches up, this Guide will be less necessary.

## Developing the Welcome Guide

This is a [Sphinx](https://www.sphinx-doc.org/) project. See the Sphinx documentation for instructions on how to install and use Sphinx. For example:

```
python3 -m pip install sphinx
```

The document sources are in the CommonMark format. You will need the `myst-parser` Python module with Sphinx. To install it:

```
python3 -m pip install myst-parser
```

To build the HTML version of the Guide:

```
make html
```
