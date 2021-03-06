import sys

from wordcount import main


def run(mode, capsys, monkeypatch):
	monkeypatch.setattr(sys, 'argv', ['wordcount.py', mode, 'letras.txt'])
	main()
	out, _ = capsys.readouterr()
	return out


def test_count(capsys, monkeypatch):
	assert run('--count', capsys, monkeypatch) == "b 3\nc 2\na 6\n"


def test_topcount(capsys, monkeypatch):
	assert run('--topcount', capsys, monkeypatch) == "a 6\nb 3\nc 2\n"
