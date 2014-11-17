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
    name='kb-base',
    packages=['base', 'base.templatetags', 'base.tests'],
    package_data={
        'base': [
            'static/*.*',
            'static/base/*.*',
            'static/base/css/*.*',
            'static/base/js/*.*',
            'static/vendor/*.*',
            'static/vendor/css/*.*',
            'static/vendor/css/font-awesome/*.*',
            'static/vendor/css/font-awesome/css/*.*',
            'static/vendor/css/font-awesome/fonts/*.*',
            'static/vendor/css/nvd3/*.*',
            'static/vendor/css/pure/*.*',
            'static/vendor/css/zebra_datepicker/*.*',
            'static/vendor/js/*.*',
            'static/vendor/js/ckeditor/*.*',
            'static/vendor/js/ckeditor/adapters/*.*',
            'static/vendor/js/ckeditor/lang/*.*',
            'static/vendor/js/ckeditor/plugins/*.*',
            'static/vendor/js/ckeditor/plugins/about/*.*',
            'static/vendor/js/ckeditor/plugins/about/dialogs/*.*',
            'static/vendor/js/ckeditor/plugins/about/dialogs/hidpi/*.*',
            'static/vendor/js/ckeditor/plugins/clipboard/*.*',
            'static/vendor/js/ckeditor/plugins/clipboard/dialogs/*.*',
            'static/vendor/js/ckeditor/plugins/dialog/*.*',
            'static/vendor/js/ckeditor/plugins/fakeobjects/*.*',
            'static/vendor/js/ckeditor/plugins/fakeobjects/images/*.*',
            'static/vendor/js/ckeditor/plugins/image/*.*',
            'static/vendor/js/ckeditor/plugins/image/dialogs/*.*',
            'static/vendor/js/ckeditor/plugins/image/images/*.*',
            'static/vendor/js/ckeditor/plugins/link/*.*',
            'static/vendor/js/ckeditor/plugins/link/dialogs/*.*',
            'static/vendor/js/ckeditor/plugins/link/images/*.*',
            'static/vendor/js/ckeditor/plugins/link/images/hidpi/*.*',
            'static/vendor/js/ckeditor/plugins/pastefromword/*.*',
            'static/vendor/js/ckeditor/plugins/pastefromword/filter/*.*',
            'static/vendor/js/ckeditor/plugins/youtube/*.*',
            'static/vendor/js/ckeditor/plugins/youtube/images/*.*',
            'static/vendor/js/ckeditor/samples/*.*',
            'static/vendor/js/ckeditor/samples/assets/*.*',
            'static/vendor/js/ckeditor/samples/assets/inlineall/*.*',
            'static/vendor/js/ckeditor/samples/assets/outputxhtml/*.*',
            'static/vendor/js/ckeditor/samples/assets/uilanguages/*.*',
            'static/vendor/js/ckeditor/samples/plugins/*.*',
            'static/vendor/js/ckeditor/samples/plugins/dialog/*.*',
            'static/vendor/js/ckeditor/samples/plugins/dialog/assets/*.*',
            'static/vendor/js/ckeditor/samples/plugins/enterkey/*.*',
            'static/vendor/js/ckeditor/samples/plugins/toolbar/*.*',
            'static/vendor/js/ckeditor/samples/plugins/wysiwygarea/*.*',
            'static/vendor/js/ckeditor/skins/*.*',
            'static/vendor/js/ckeditor/skins/moono/*.*',
            'static/vendor/js/ckeditor/skins/moono/images/*.*',
            'static/vendor/js/ckeditor/skins/moono/images/hidpi/*.*',
            'static/vendor/js/nvd3/*.*',
            'static/vendor/js/pure/*.*',
            'templates/*.*',
            'templates/base/*.*',
        ],
    },
    version='0.1.33',
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