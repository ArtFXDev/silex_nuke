import logging
import os
import pathlib
from typing import Any, Dict

import nuke
from silex_client.action.action_query import ActionQuery
from silex_client.action.command_base import CommandBase
from silex_nuke.utils.thread import execute_in_main_thread


class Save(CommandBase):
    """
    Save current scene with context as path
    """

    parameters = {
        "file_path": {"type": pathlib.Path, "value": None, "hide": True},
    }

    @CommandBase.conform_command()
    async def __call__(
        self,
        parameters: Dict[str, Any],
        action_query: ActionQuery,
        logger: logging.Logger,
    ):
        file_path: pathlib.Path = parameters["file_path"]

        # Create directories
        os.makedirs(file_path.parents[0], exist_ok=True)

        logger.info("Saving scene to %s", file_path)
        await execute_in_main_thread(nuke.scriptSaveAs, filename=str(file_path))

        return {"new_path": file_path}
