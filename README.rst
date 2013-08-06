Base
****

Simple Django base application

Install
=======

Virtual Environment
-------------------

Note: replace ``patrick`` with your name (checking in the ``example`` folder
to make sure a file has been created for you).

::

  mkvirtualenv dev_base
  pip install -r requirements-dev.txt

  echo "export DJANGO_SETTINGS_MODULE=example.dev_patrick" >> $VIRTUAL_ENV/bin/postactivate
  echo "unset DJANGO_SETTINGS_MODULE" >> $VIRTUAL_ENV/bin/postdeactivate

  add2virtualenv ../login
  add2virtualenv .
  deactivate

To check the order of the imports:

::

  workon dev_base
  cdsitepackages
  cat _virtualenv_path_extensions.pth

Check the imports are in the correct order e.g:

::

  /home/your_name/repo/dev/app/base
  /home/your_name/repo/dev/app/login

Testing
=======

We use ``pytest-django``:

::

  workon dev_base
  py.test

To stop on first failure:

::

  py.test -x

Usage
=====

::

  workon dev_base
  django-admin.py syncdb --noinput
  django-admin.py migrate --all --noinput
  django-admin.py demo_data_login
  django-admin.py demo_data_base
  django-admin.py runserver

Release
=======

To release the application:

::

  fab -f ../../module/fabric/release.py dist
  hg push

To check the contents of the distribution:

::

  tar -ztvf dist/dev-base-0.2.1.tar.gz
