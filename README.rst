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

  py.test -x && \
      touch temp.db && rm temp.db && \
      django-admin.py migrate --noinput && \
      django-admin.py demo_data_login && \
      django-admin.py runserver

Release
=======

https://www.kbsoftware.co.uk/docs/
