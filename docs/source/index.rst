Generate message queue
-----------------------

**gen_message_queue** is framework for generation message queue modules.

Developed in `python <https://www.python.org/>`_ code: **100%**.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

|gen_message_queue python checker| |gen_message_queue python package| |github issues| |documentation status| |github contributors|

.. |gen_message_queue python checker| image:: https://github.com/vroncevic/gen_message_queue/actions/workflows/gen_message_queue_python_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_message_queue/actions/workflows/gen_message_queue_python_checker.yml

.. |gen_message_queue python package| image:: https://github.com/vroncevic/gen_message_queue/actions/workflows/gen_message_queue_package_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_message_queue/actions/workflows/gen_message_queue_package.yml

.. |github issues| image:: https://img.shields.io/github/issues/vroncevic/gen_message_queue.svg
   :target: https://github.com/vroncevic/gen_message_queue/issues

.. |github contributors| image:: https://img.shields.io/github/contributors/vroncevic/gen_message_queue.svg
   :target: https://github.com/vroncevic/gen_message_queue/graphs/contributors

.. |documentation status| image:: https://readthedocs.org/projects/gen_message_queue/badge/?version=latest
   :target: https://gen-message-queue.readthedocs.io/en/latest/?badge=latest

.. toctree::
   :maxdepth: 4
   :caption: Contents

   self
   modules

Installation
-------------

|gen_message_queue python3 build|

.. |gen_message_queue python3 build| image:: https://github.com/vroncevic/gen_message_queue/actions/workflows/gen_message_queue_python3_build.yml/badge.svg
   :target: https://github.com/vroncevic/gen_message_queue/actions/workflows/gen_message_queue_python3_build.yml

Navigate to release `page`_ download and extract release archive.

.. _page: https://github.com/vroncevic/gen_message_queue/releases

To install package type the following

.. code-block:: bash

    tar xvzf gen_message_queue-x.y.z.tar.gz
    cd gen_message_queue-x.y.z/
    # python3
    wget https://bootstrap.pypa.io/get-pip.py
    python3 get-pip.py 
    python3 -m pip install --upgrade setuptools
    python3 -m pip install --upgrade pip
    python3 -m pip install --upgrade build
    pip3 install -r requirements.txt
    python3 -m build --no-isolation --wheel
    pip3 install ./dist/gen_message_queue-*-py3-none-any.whl
    rm -f get-pip.py
    chmod 755 /usr/local/lib/python3.10/dist-packages/usr/local/bin/gen_message_queue_run.py
    ln -s /usr/local/lib/python3.10/dist-packages/usr/local/bin/gen_message_queue_run.py /usr/local/bin/gen_message_queue_run.py

You can use Docker to create image/container, or You can use pip to install

.. code-block:: bash

    # pyton3
    pip3 install gen_message_queue

Dependencies
-------------

**gen_message_queue** requires next modules and libraries

* `ats-utilities - Python App/Tool/Script Utilities <https://pypi.org/project/ats-utilities/>`_

Tool structure

**gen_message_queue** is based on OOP.

.. code-block:: bash

    gen_message_queue/
        ├── conf/
        │   ├── gen_message_queue.cfg
        │   ├── gen_message_queue.logo
        │   ├── gen_message_queue_util.cfg
        │   ├── project.yaml
        │   └── template/
        │       ├── posix/
        │       │   ├── mq_posix_close.template
        │       │   ├── mq_posix_fatal_error.template
        │       │   ├── mq_posix_open_mode.template
        │       │   ├── mq_posix_open.template
        │       │   ├── mq_posix_receive.template
        │       │   ├── mq_posix_send.template
        │       │   ├── mq_posix.template
        │       │   └── mq_posix_unlink.template
        │       └── sysv/
        │           ├── mq_sysv_control.template
        │           ├── mq_sysv_file_to_key.template
        │           ├── mq_sysv_get_buffer.template
        │           ├── mq_sysv_get_buffer_type.template
        │           ├── mq_sysv_key_to_id.template
        │           ├── mq_sysv_receive.template
        │           ├── mq_sysv_send.template
        │           ├── mq_sysv_set_buffer.template
        │           ├── mq_sysv_set_buffer_type.template
        │           └── mq_sysv.template
        ├── __init__.py
        ├── log/
        │   └── gen_message_queue.log
        ├── pro/
        │   ├── __init__.py
        │   ├── read_template.py
        │   └── write_template.py
        └── run/
            └── gen_message_queue_run.py
        
        8 directories, 28 files

Copyright and licence
----------------------

|license: gpl v3| |license: apache 2.0|

.. |license: gpl v3| image:: https://img.shields.io/badge/license-gplv3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. |license: apache 2.0| image:: https://img.shields.io/badge/license-apache%202.0-blue.svg
   :target: https://opensource.org/licenses/apache-2.0

Copyright (C) 2018 - 2026 by `vroncevic.github.io/gen_message_queue <https://vroncevic.github.io/gen_message_queue>`_

**gen_message_queue** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

|python software foundation|

.. |python software foundation| image:: https://raw.githubusercontent.com/vroncevic/gen_message_queue/dev/docs/psf-logo-alpha.png
   :target: https://www.python.org/psf/

|donate|

.. |donate| image:: https://www.paypalobjects.com/en_us/i/btn/btn_donatecc_lg.gif
   :target: https://www.python.org/psf/donations/

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
