# Jonathan Therrien, Marieville, Québec.

from tebdlc.cli import main


def test_cli_info_json(capsys):
    assert main(["info", "--json"]) == 0
    out = capsys.readouterr().out
    assert '"product": "TEBDLC"' in out
    assert '"network_required": false' in out


def test_cli_self_check_json(capsys):
    assert main(["self-check", "--json"]) == 0
    out = capsys.readouterr().out
    assert '"self_check": "PASS"' in out
    assert '"gain_count": 1' in out
