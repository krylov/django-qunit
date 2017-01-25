import os

BASE_PATH = os.path.dirname(__file__)

QUNIT_TEST_DIRECTORY = os.path.join(BASE_PATH, "qunit_tests")
QUNIT_PACKAGE_JSON = "package.json"
QUNIT_INDEX_HTML = "tests.html"

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ROOT_URLCONF = "example.urls"

INSTALLED_APPS = (
    "django_qunit",
)

SECRET_KEY = "qwerty"
TEMPLATE_DIRS = [QUNIT_TEST_DIRECTORY]
