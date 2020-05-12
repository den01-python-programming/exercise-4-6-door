import pytest
from src import door

def test_exercise(capsys):
    alexander = door.Door()

    print(alexander.knock())

    out, err = capsys.readouterr()
    assert out == "Who's there?\n"
