# pylint: skip-file
name = "silex_nuke"
version = "0.1.0"

authors = ["ArtFx TD gang"]

description = """
    Set of python module and nuke config to integrate nuke in the silex pipeline
    Part of the Silex ecosystem
    """

vcs = "git"

build_command = "python {root}/script/build.py {install}"


def commands():
    """
    Set the environment variables for silex_nuke
    """
    env.SILEX_ACTION_CONFIG.append("{root}/silex_nuke/config")
    env.PYTHONPATH.append("{root}")
    env.NUKE_PATH.append("{root}/startup")


@late()
def requires():
    major = str(this.version.major)
    silex_requirement = ["silex_client"]
    if major in ["dev", "beta", "prod"]:
        silex_requirement = [f"silex_client-{major}"]

    return ["nuke", "python-3.7"] + silex_requirement
