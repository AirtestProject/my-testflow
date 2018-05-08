
.. image:: doc/img/logo-simple-my-testflow.png

my-testflow
===========

**Test automation standard engineering project template**. More and more features to be added in future.

How to use?
-----------

**1.** Clone this repo and run the following command. (Installing with ``-e`` flag is strongly recommended.)

.. code-block:: bash
    
    git clone https://github.com/AirtestProject/my-testflow.git
    pip install -e my-testflow

**2.** Run the example script after installation.

.. code-block:: bash

    python testflow/scripts/example.py

**3.** Check the test results in ``pocounit-results/`` with `TestResultPlayer`_.

Project structure
-----------------

.. code-block:: text

    ─ my-testflow/
        ├─ testflow/                <-------  rename this folder if you with (identifier only)
        |   ├─ __init__.py
        |   ├─ lib/
        |   |   ├─ __init__.py
        |   |   └─ ...
        |   └─ scripts/
        |       ├─ __init__.py
        |       ├─ example.py       <-------  you can try running this script
        |       └─ ...
        ├─ res/                     <-------  store any resource files
        |   ├─ app/
        |   └─ img/
        ├─ pocounit-results/        <-------  test results will auto generated here
        ├─ setup.py
        ├─ requirements.txt
        └─ .gitignore


How to get the test results?
----------------------------

Use our `TestResultPlayer`_ to replay the whole procedure of your tests!

More info
---------

This template is designed for engineering test flow and it works along with following frameworks.
You can take a look at the API reference according to each framework.

- `airtest`_
- `poco`_
- `pocounit`_

`see also <http://poco-chinese.readthedocs.io/zh_CN/latest/source/doc/netease-internal-use-template.html>`_


.. _TestResultPlayer: http://poco.readthedocs.io/en/latest/source/doc/about-test-result-player.html
.. _airtest: http://airtest.readthedocs.io
.. _poco: http://poco.readthedocs.io
.. _pocounit: https://github.com/AirtestProject/PocoUnit

Join to discuss!
----------------

|chat on slack|

.. image:: doc/img/discussion-qq-qr.png

.. |chat on slack| image:: doc/img/chat_on_slack.png
    :alt: chat on slack
    :scale: 100%
    :target: https://join.slack.com/t/airtestproject/shared_invite/enQtMzYwMjc2NjQzNDkzLTcyMmJlNjgyNjgzZTRkNWRiYmE1YWI1ZWE5ZmQwYmM1YmY3ODZlMDc0YjkwMTQ5NDYxYmEyZWU1ZTFlZjg3ZjI