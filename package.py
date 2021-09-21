# pylint: skip-file
name = "silex_nuke"
version = "0.1.0"

authors = ["ArtFx TD gang"]

description = \
    """
    Set of python module and nuke config to integrate nuke in the silex pipeline
    Part of the Silex ecosystem
    """

vcs = "git"

requires = ["silex_client", "nuke", "python-3.7"]

build_command = "python {root}/script/build.py {install}"

def commands():
    """
    Set the environment variables for silex_nuke
    """
    env.SILEX_ACTION_CONFIG = "{root}/config/action"
    env.PYTHONPATH.append("{root}")
    env.NUKE_PATH.append("{root}/startup")
