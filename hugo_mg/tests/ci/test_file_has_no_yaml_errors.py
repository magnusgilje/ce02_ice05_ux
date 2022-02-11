"""yamllint dynamic pytest wrapper"""

import glob
import subprocess
import pytest

FILTER = './../**/*.yaml'
PYTHON_FILES = glob.glob(FILTER, recursive=True)
@pytest.mark.parametrize('filepath', PYTHON_FILES)

def test_file_has_no_yamllint_errors(filepath):
    """validate that there are zero yamllint warnings against an YAML file"""
    print('creating tests for file {}'.format(filepath))

    proc = subprocess.Popen("yamllint "+ filepath + " -c ../../.yamllint",
                            stdout=subprocess.PIPE, shell=True)
    (out, _err) = proc.communicate()

    # pylint: disable=C1801
    assert len(out) == 0


# """yamllint dynamic pytest wrapper"""

# import glob
# import subprocess
# import pytest

# FILTER = './../../**/*.yaml'
# PYTHON_FILES = glob.glob(FILTER, recursive=True)
# @pytest.mark.parametrize('filepath', PYTHON_FILES)

# def test_file_has_no_pylint_errors(filepath):
#     """validate that there are zero yamllint warnings against an YAML file"""
#     print('creating tests for file {}'.format(filepath))

#     proc = subprocess.Popen("yamllint "+ filepath + " -c ../../../.yamllint",
#                             stdout=subprocess.PIPE, shell=True)
#     (out, _err) = proc.communicate()

#     # pylint: disable=C1801
#     assert len(out) == 0
