import os
from distutils.core import setup


def read_file_into_string(filename):
    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(path, filename)
    try:
        return open(filepath).read()
    except IOError:
        return ''


def get_readme():
    for name in ('README', 'README.rst', 'README.md'):
        if os.path.exists(name):
            return read_file_into_string(name)
    return ''


setup(
    name='pkimber-base',
    packages=['base', 'base.templatetags', 'base.tests'],
    package_data={
        'base': [
            'static/*.*',
            'static/base/*.*',
            'static/base/css/*.*',
            'static/base/css/font-awesome/*.*',
            'static/base/css/font-awesome/css/*.*',
            'static/base/css/font-awesome/fonts/*.*',
            'static/base/css/nvd3/*.*',
            'static/base/js/*.*',
            'static/base/js/ck/*.*',
            'static/base/js/ck/lang/*.*',
            'static/base/js/ck/plugins/*.*',
            'static/base/js/ck/plugins/about/*.*',
            'static/base/js/ck/plugins/about/dialogs/*.*',
            'static/base/js/ck/plugins/about/dialogs/hidpi/*.*',
            'static/base/js/ck/plugins/link/*.*',
            'static/base/js/ck/plugins/link/dialogs/*.*',
            'static/base/js/ck/plugins/link/images/*.*',
            'static/base/js/ck/plugins/link/images/hidpi/*.*',
            'static/base/js/ck/skins/*.*',
            'static/base/js/ck/skins/moono/*.*',
            'static/base/js/ck/skins/moono/images/*.*',
            'static/base/js/ck/skins/moono/images/hidpi/*.*',
            'static/base/js/nvd3/*.*',
            'templates/*.*',
            'templates/base/*.*',
        ],
    },
    version='0.0.43',
    description='Base',
    author='Patrick Kimber',
    author_email='code@pkimber.net',
    url='git@github.com:pkimber/base.git',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Office/Business :: Scheduling',
    ],
    long_description=get_readme(),
)