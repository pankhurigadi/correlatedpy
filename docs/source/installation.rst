.. _install:

Installation
============

Prerequisites
-------------

This project requires python3 (>=3.5)

The algorithm requires the installation of libraries such as `quantecon <https://pypi.org/project/quantecon/>`_, which itself has dependencies that must be installed manually.

The following python packages are needed to run the program 
* [matplotlib](https://pypi.org/project/matplotlib/)

* [nashpy](https://pypi.org/project/nashpy/)

* [numpy](https://pypi.org/project/numpy/)

* [tqdm](https://pypi.org/project/tqdm/)

* [quantecon](https://pypi.org/project/qe/)

These can all be installed with pip, e.g.,  
```sh
  pip install nashpy
  ```


Ubuntu
~~~~~~

.. code-block:: bash

    sudo apt-get update -y
    sudo apt-get install -y python-dev libsdl-image1.2-dev libsdl-mixer1.2-dev
        libsdl-ttf2.0-dev libsdl1.2-dev libsmpeg-dev python-numpy subversion libportmidi-dev
        ffmpeg libswscale-dev libavformat-dev libavcodec-dev libfreetype6-dev gcc

Windows 10
~~~~~~~~~~

We recommend using `Anaconda <https://conda.io/docs/user-guide/install/windows.html>`_.


Stable release
---------------------
To install the latest stable version:

.. code-block:: bash

    pip install correlatedpy

Development version
---------------------

To install the current development version:

.. code-block:: bash

    pip install --user git+https://github.com/oboufous/correlatedpy
