Base
****

Simple Django base application

Install
=======

Virtual Environment
-------------------

::

  virtualenv --python=python3 venv-base
  source venv-base/bin/activate

  pip install -r requirements/local.txt

Testing
=======

::

  find . -name '*.pyc' -delete
  py.test -x

Usage
=====

::

  ./init_dev.sh

Release
=======

https://www.kbsoftware.co.uk/docs/
