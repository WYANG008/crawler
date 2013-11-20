
from setuptools import setup, find_packages

requires = [
    'celery',
    'redis',
    'requests',
    'lxml',
    'cssselect',
    'happybase',
]


setup(
    name = "WebCrawler",
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = requires,
    entry_points="""
    [console_scripts]
    start_celery = WebCrawler.scripts:start_celery
    start_job = WebCrawler.scripts:start_job
    """
)
