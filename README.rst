MapScript Python Notebook ReadMe
================================

Creating a Virtual Environment with Jupyter and mapscript:

.. code-block:: bat

    SET PYTHON_HOME=C:\Python36
    SET PYTHON_HOME=C:\Python27

    SET VENV=C:\VirtualEnvs\mapscript-jupyter3
    SET VENV=C:\VirtualEnvs\mapscript-jupyter


    %PYTHON_HOME%\Scripts\virtualenv %VENV%
    %VENV%\scripts\activate

    python -m pip install pip -U
    pip install jupytext
    python -m pip install jupyter
    pip install mapscript -U

To create a notebook from a Python script jupytext is used - https://github.com/mwouts/jupytext
The script is written using the "percent" format - https://github.com/mwouts/jupytext/blob/master/demo/World%20population.pct.py
To create the notebook:

.. code-block:: bat

    SET NOTEBOOK_HOME=D:\GitHub\GeoPythonNotebooks\notebooks
    %VENV%\scripts\activate

    cd /D %NOTEBOOK_HOME%

    jupytext --to notebook mapscript-quickstart.py

To set up the paths to MapServer and run the notebook:

.. code-block:: bat

    SET MAPSERVER_HOME=C:\Installation\release-1911-x64-gdal-2-3-2-mapserver-7-2-1
    SET MAPSERVER_HOME=D:\MapServer\release-1911-x64-gdal-2-3-2-mapserver-7-2-1
    SET MAPSERVER_DEMO=D:\GitHub\mapserver-demo

    SET PATH=%MAPSERVER_HOME%\bin;%PATH%
    SET PROJ_LIB=%MAPSERVER_HOME%\bin\proj\SHARE

    cd /D %NOTEBOOK_HOME%

    REM run the script
    python mapscript-quickstart.py
    REM run the notebook
    jupyter notebook mapscript-quickstart.ipynb

Jupyter and Binder
------------------

+ https://github.com/geographika/GeoPythonNotebooks
+ https://hub.mybinder.org - path to notebook - notebooks/mapscript-quickstart.ipynb

Running on OSGeoLive
--------------------

.. code-block:: bash

    wget https://github.com/geographika/GeoPythonNotebooks/archive/master.zip
    unzip master.zip
    cd GeoPythonNotebooks-master/jupyter/quickstarts

    export MAPSERVER_DEMO="/rofs/usr/local/share/mapserver/demos/itasca"
    
    python -m jupyter notebook mapscript-quickstart.ipynb

..
    Can't set export PYTHONPATH="/rofs/usr/lib/python2.7/dist-packages:$PYTHONPATH"

    /usr/lib/otb/python
    unset PYTHONPATH
    printenv
    $PYTHONPATH /usr/lib/otb/python

    /rofs/usr/lib/python2.7/dist-packages/_mapscript.x86_64-linux-gnu.so
    jupyter is set to use python3

    cat `which jupyter`
    #!/usr/bin/python3
    /usr/bin/jupyter

MapScript on Ubuntu
-------------------

https://packages.ubuntu.com/search?suite=default&section=all&arch=any&keywords=mapscript&searchon=names

+ bionic (18.04LTS) (devel): Python library for MapServer [universe] 
+ 7.0.7-1build2: amd64 arm64 armhf i386 ppc64el s390x

  + /usr/lib/x86_64-linux-gnu/libmapserver.so.2
  + /usr/lib/x86_64-linux-gnu/libmapserver.so.7.0.7

Script Updates
--------------

To add:

+ buffer - needs GEOS support
+ queryByShape towns near a lake

..
    #result = mapscript.msIO_getStdoutBufferString() # for string data, but this does not clear the buffer!
    # any future requests to msIO_getStdoutBufferBytes will get all the previous requests
    output_file = r"C:\Temp\map_ref.png"
    ref_image = map.drawReferenceMap()
    ref_image.save(output_file)
    result = results.getResult(0)
    print(result.classindex) # can get class, so therefore can test EXPRESSIONs!

Linux Install
-------------

.. code-block:: bash

    sudo apt-get update

    sudo apt-get install libmapserver2
    sudo apt-get install python-mapscript

    sudo apt-get install python-pip
    pip install ipython

    ipython -c "import mapscript"
    python2 -c "import mapscript"

..
    ImportError: /usr/lib/libgdal.so.20: undefined symbol: sqlite3_column_table_name

..
    OSGeoLive repo https://git.osgeo.org/gitea/osgeolive/OSGeoLive12-Notebooks/src/branch/master