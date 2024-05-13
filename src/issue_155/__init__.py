import subprocess


class Command:

    def __init__(self, *elements: str) -> None:
        self._command = [str(element) for element in elements]

    def run(self):
        def _spawn_process() -> subprocess.Popen[bytes]:
            return subprocess.Popen(self._command)

        process = _spawn_process()
        return process
