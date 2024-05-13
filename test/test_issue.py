from __future__ import annotations

from typing import TYPE_CHECKING
from issue_155 import Command

if TYPE_CHECKING:
    from pytest_subprocess.fake_process import FakeProcess


def test_default(
    fp: FakeProcess
) -> None:
    fp.register(["cmake", fp.any(min=2)], returncode=1)
    fp.register(["cmake", "--build", fp.any(min=1)], returncode=1)
    fp.allow_unregistered(allow=True)
    def _spawn_process():
        import subprocess
        return subprocess.Popen(["ls"])
    process_in_test = _spawn_process()
    command = Command("ls")
    command.run()
