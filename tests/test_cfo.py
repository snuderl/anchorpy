import subprocess
from pathlib import Path

from pytest import fixture

from tests.utils import get_localnet

PATH = Path("anchor/tests/cfo")

localnet = get_localnet(PATH)


@fixture(scope="module")
def build_lockup() -> None:
    subprocess.run(  # noqa: S603
        ["anchor", "build"],
        check=True,
        cwd="anchor/tests/lockup",
    )


def boilerplate(build_lockup, localnet):
    """TODO."""
