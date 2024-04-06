import os
import shutil
import pytest
from zipfile import ZipFile

from paths import RESOURCE_DIR, ZIP_FILE, TEMP_DIR


@pytest.fixture(scope='session', autouse=True)
def create_zip():
    if not os.path.exists(RESOURCE_DIR):
        os.makedirs(RESOURCE_DIR)

    with ZipFile(ZIP_FILE, 'w') as zip_file:
        for path, _, files in os.walk(TEMP_DIR):
            for file in files:
                file_path = os.path.join(path, file)
                zip_file.write(file_path, file)

    yield

    shutil.rmtree(RESOURCE_DIR)
