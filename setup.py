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
            'static/base/css/zebra_datepicker/*.*',
            'static/base/js/*.*',
            'static/base/js/ckeditor/*.*',
            'static/base/js/ckeditor/adapters/*.*',
            'static/base/js/ckeditor/lang/*.*',
            'static/base/js/ckeditor/plugins/*.*',
            'static/base/js/ckeditor/plugins/about/*.*',
            'static/base/js/ckeditor/plugins/about/dialogs/*.*',
            'static/base/js/ckeditor/plugins/about/dialogs/hidpi/*.*',
            'static/base/js/ckeditor/plugins/clipboard/*.*',
            'static/base/js/ckeditor/plugins/clipboard/dialogs/*.*',
            'static/base/js/ckeditor/plugins/dialog/*.*',
            'static/base/js/ckeditor/plugins/fakeobjects/*.*',
            'static/base/js/ckeditor/plugins/fakeobjects/images/*.*',
            'static/base/js/ckeditor/plugins/image/*.*',
            'static/base/js/ckeditor/plugins/image/dialogs/*.*',
            'static/base/js/ckeditor/plugins/image/images/*.*',
            'static/base/js/ckeditor/plugins/link/*.*',
            'static/base/js/ckeditor/plugins/link/dialogs/*.*',
            'static/base/js/ckeditor/plugins/link/images/*.*',
            'static/base/js/ckeditor/plugins/link/images/hidpi/*.*',
            'static/base/js/ckeditor/plugins/pastefromword/*.*',
            'static/base/js/ckeditor/plugins/pastefromword/filter/*.*',
            'static/base/js/ckeditor/plugins/youtube/*.*',
            'static/base/js/ckeditor/plugins/youtube/images/*.*',
            'static/base/js/ckeditor/samples/*.*',
            'static/base/js/ckeditor/samples/assets/*.*',
            'static/base/js/ckeditor/samples/assets/inlineall/*.*',
            'static/base/js/ckeditor/samples/assets/outputxhtml/*.*',
            'static/base/js/ckeditor/samples/assets/uilanguages/*.*',
            'static/base/js/ckeditor/samples/plugins/*.*',
            'static/base/js/ckeditor/samples/plugins/dialog/*.*',
            'static/base/js/ckeditor/samples/plugins/dialog/assets/*.*',
            'static/base/js/ckeditor/samples/plugins/enterkey/*.*',
            'static/base/js/ckeditor/samples/plugins/toolbar/*.*',
            'static/base/js/ckeditor/samples/plugins/wysiwygarea/*.*',
            'static/base/js/ckeditor/skins/*.*',
            'static/base/js/ckeditor/skins/moono/*.*',
            'static/base/js/ckeditor/skins/moono/images/*.*',
            'static/base/js/ckeditor/skins/moono/images/hidpi/*.*',
            'static/base/js/nvd3/*.*',
            'templates/*.*',
            'templates/base/*.*',
        ],
    },
    version='0.1.04',
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