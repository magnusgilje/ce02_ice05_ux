"""pylint dynamic terraform fmt wrapper"""

import glob
import subprocess
import pytest

FILTER = './../../**/*.tf*'
TERRAFORM_FILES = glob.glob(FILTER, recursive=True)
@pytest.mark.parametrize('filepath', TERRAFORM_FILES)

def test_file_has_no_terraform_errors(filepath):
    """validate that there are valid terraform files"""
    print('creating tests for file {}'.format(filepath))

    proc = subprocess.Popen("terraform fmt -check "+ filepath ,
                            stdout=subprocess.PIPE, shell=True)
    (out, _err) = proc.communicate()

    # pylint: disable=C1801
    assert len(out) == 0
