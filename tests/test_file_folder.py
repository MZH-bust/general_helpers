import pytest
from genutil import file_folder
import hamcrest
from datetime import datetime
from pathlib import Path
from tests import generic


class TestGetFileModificationDatetime:
    @pytest.mark.parametrize(
        "test_parameter,test_cases,expected",
        [
            pytest.param(("file_folder.py", ), {"type": datetime}, True, id="Param1"),
            pytest.param((Path.cwd().parent.joinpath("data/Excelfile1.xlsx"), ), {"type": datetime}, True,
                         id="Param2"),
            pytest.param(("Excelfile1.xlsx", r"C:\Users\Martin.Zoeltsch\Desktop\Coding\general_helpers\data"),
                         {"type": datetime}, True, id="Param3"),
            pytest.param(("FILE_DOES_NOT_EXIST.md",), {"error": (FileNotFoundError, )}, True, id="Param4"),
        ],
    )
    def test_all_generic(self, test_parameter, test_cases, expected):
        test_function = file_folder.get_file_modification_datetime
        generic.generic_function(test_function, test_parameter, test_cases, expected)


class TestListFilesInFolder:
    @pytest.mark.parametrize(
        "test_parameter,test_cases,expected",
        [
            pytest.param((Path.cwd().parent.joinpath("data"), ),
                         {"result": ['Excelfile1.xlsx', 'Excelfile2.XLSX', 'Excelfile3.xlsx', 'Powerpoint1.pptx', 'Powerpoint2.PPTX', 'Textfile1.txt']}, True, id="Param1"),
            pytest.param((Path.cwd().parent.joinpath("data"), ".pptx"),
                         {"result": ['Powerpoint1.pptx', 'Powerpoint2.PPTX']}, True, id="Param2"),
            pytest.param((Path.cwd().parent.joinpath("data"), (".pptx", ".txt")),
                         {"result": ['Powerpoint1.pptx', 'Powerpoint2.PPTX', 'Textfile1.txt']}, True, id="Param3"),
            pytest.param((r"A PATH THAT DOESNT EXIST", (".pptx", ".txt")),
                         {"error": (IOError, OSError, FileNotFoundError)}, True, id="Param4"),
        ],
    )
    def test_all_generic(self, test_parameter, test_cases, expected):
        test_function = file_folder.list_files_in_folder
        generic.generic_function(test_function, test_parameter, test_cases, expected)