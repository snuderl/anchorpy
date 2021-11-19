import subprocess
from pathlib import Path

from pytest import fixture

from anchorpy.pytest_plugin import localnet_fixture

PATH = Path("anchor/tests/cfo")

localnet = localnet_fixture(PATH)


@fixture(scope="module")
def build_lockup() -> None:
    subprocess.run(  # noqa: S603,S607
        ["anchor", "build"],
        check=True,
        cwd="anchor/tests/lockup",
    )


def boilerplate(build_lockup, localnet):
    """TODO."""
