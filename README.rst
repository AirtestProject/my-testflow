Test automation standard engineering project template
=====================================================

How to use?
-----------

Clone this repo and run following command. (You'd better install it with the ``-e`` flag.)

.. code-block:: bash
    
    git clone git@github.com:AirtestProject/my-testflow.git
    pip install -e my-testflow

Structure
---------

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

More
----

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
