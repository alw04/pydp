from lib.build_systems.python import PythonPackage


class Snakemake(PythonPackage):
    """Workflow management system to create reproducible and scalable data analyses."""

    homepage = "https://snakemake.readthedocs.io/en"

    versions = [
        "9.6.3",
    ]
