from __future__ import annotations
import typing
import logging
from typing import Any, Dict

import pathlib
from silex_client.action.command_base import CommandBase
from silex_nuke.utils.thread import execute_in_main_thread

# Forward references
if typing.TYPE_CHECKING:
    from silex_client.action.action_query import ActionQuery

import nuke


class Open(CommandBase):
    """
    Open the given scene file
    """

    parameters = {
        "file_path": {
            "label": "filename",
            "type": pathlib.Path,
            "value": None,
        },
        "save": {
            "label": "Save before opening",
            "type": bool,
            "value": True,
        },
    }

    @CommandBase.conform_command()
    async def __call__(
        self,
        parameters: Dict[str, Any],
        action_query: ActionQuery,
        logger: logging.Logger,
    ):
        file_path: pathlib.Path = parameters["file_path"]
        save_before_open: bool = parameters["save"]

        # First get the current file name
        current_file = pathlib.Path(nuke.root().name())

        # Don't open a file that is already open
        if current_file == file_path:
            return {"old_path": current_file, "new_path": parameters["file_path"]}

        # Test if the scene that we have to open exists
        if not file_path.exists():
            logger.error("Could not open %s: The file does not exists", file_path)
            return {"old_path": current_file, "new_path": current_file}

        # Save the current scene before openning a new one
        if save_before_open:
            await execute_in_main_thread(nuke.scriptSave)
        logger.info("Openning file %s", file_path)
        # Open the given scene in the main thread
        await execute_in_main_thread(nuke.scriptClear)
        await execute_in_main_thread(nuke.scriptOpen, file_path.as_posix())

        return {"old_path": current_file, "new_path": parameters["file_path"]}
