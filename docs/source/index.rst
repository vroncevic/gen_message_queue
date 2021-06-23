Generate message queue
-----------------------

**gen_message_queue** is framework for generation message queue modules.

Developed in `python <https://www.python.org/>`_ code: **100%**.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

|Python package| |GitHub issues| |Documentation Status| |GitHub contributors|

.. |Python package| image:: https://github.com/vroncevic/gen_message_queue/workflows/Python%20package/badge.svg
   :target: https://github.com/vroncevic/gen_message_queue/workflows/Python%20package/badge.svg?branch=master

.. |GitHub issues| image:: https://img.shields.io/github/issues/vroncevic/gen_message_queue.svg
   :target: https://github.com/vroncevic/gen_message_queue/issues

.. |GitHub contributors| image:: https://img.shields.io/github/contributors/vroncevic/gen_message_queue.svg
   :target: https://github.com/vroncevic/gen_message_queue/graphs/contributors

.. |Documentation Status| image:: https://readthedocs.org/projects/gen_message_queue/badge/?version=latest
   :target: https://gen_message_queue.readthedocs.io/projects/gen_message_queue/en/latest/?badge=latest

.. toctree::
   :maxdepth: 4
   :caption: Contents:

   self
   modules

Installation
-------------

|Install Python2 Package| |Install Python3 Package|

.. |Install Python2 Package| image:: https://github.com/vroncevic/gen_message_queue/workflows/Install%20Python2%20Package%20gen_message_queue/badge.svg
   :target: https://github.com/vroncevic/gen_message_queue/workflows/Install%20Python2%20Package%20gen_message_queue/badge.svg?branch=master

.. |Install Python3 Package| image:: https://github.com/vroncevic/gen_message_queue/workflows/Install%20Python3%20Package%20gen_message_queue/badge.svg
   :target: https://github.com/vroncevic/gen_message_queue/workflows/Install%20Python3%20Package%20gen_message_queue/badge.svg?branch=master

Navigate to release `page`_ download and extract release archive.

.. _page: https://github.com/vroncevic/gen_message_queue/releases

To install package type the following:

.. code-block:: bash

    tar xvzf gen_message_queue-x.y.z.tar.gz
    cd gen_message_queue-x.y.z/
    # python2
    pip install -r requirements.txt
    python setup.py install_lib
    python setup.py install_egg_info
    # pyton3
    pip3 install -r requirements.txt
    python3 setup.py install_lib
    python3 setup.py install_egg_info

You can use Docker to create image/container, or You can use pip to install:

.. code-block:: bash

    # python2
    pip install gen-message-gueue
    # python3
    pip3 install gen-message-gueue

|GitHub docker checker|

.. |GitHub docker checker| image:: https://github.com/vroncevic/gen_message_queue/workflows/gen_message_queue%20docker%20checker/badge.svg
   :target: https://github.com/vroncevic/gen_message_queue/actions?query=workflow%3A%22gen_message_queue+docker+checker%22

Dependencies
-------------

**gen_message_queue** requires next modules and libraries:

* `ats-utilities - Python App/Tool/Script Utilities <https://pypi.org/project/ats-utilities/>`_

Framework structure
--------------------

**gen_message_queue** is based on OOP:

.. image:: https://raw.githubusercontent.com/vroncevic/gen_message_queue/dev/docs/arch_flow_usage.png

Framework structure:

.. code-block:: bash

    gen_message_queue/
    ├── conf/
    │   ├── gen_message_queue.cfg
    │   ├── gen_message_queue_util.cfg
    │   ├── project.yaml
    │   └── template/
    │       ├── mq_posix/
    │       │   ├── mq_posix_close.template
    │       │   ├── mq_posix_fatal_error.template
    │       │   ├── mq_posix_open_mode.template
    │       │   ├── mq_posix_open.template
    │       │   ├── mq_posix_receive.template
    │       │   ├── mq_posix_send.template
    │       │   ├── mq_posix.template
    │       │   └── mq_posix_unlink.template
    │       └── mq_sysv/
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
    │   ├── config/
    │   │   ├── __init__.py
    │   │   ├── pro_name.py
    │   │   └── template_dir.py
    │   ├── __init__.py
    │   ├── read_template.py
    │   └── write_template.py
    └── run/
        └── gen_message_queue_run.py

Copyright and licence
----------------------

|License: GPL v3| |License: Apache 2.0|

.. |License: GPL v3| image:: https://img.shields.io/badge/License-GPLv3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. |License: Apache 2.0| image:: https://img.shields.io/badge/License-Apache%202.0-blue.svg
   :target: https://opensource.org/licenses/Apache-2.0

Copyright (C) 2018 by `vroncevic.github.io/gen_message_queue <https://vroncevic.github.io/gen_message_queue>`_

**gen_message_queue** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.x/3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

|Python Software Foundation|

.. |Python Software Foundation| image:: https://raw.githubusercontent.com/vroncevic/gen_message_queue/dev/docs/psf-logo-alpha.png
   :target: https://www.python.org/psf/

|Donate|

.. |Donate| image:: https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif
   :target: https://psfmember.org/index.php?q=civicrm/contribute/transact&reset=1&id=2

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
