from __future__ import annotations

import logging
import typing
from typing import Any, Dict, List

import fileseq
from silex_client.action.command_base import CommandBase
from silex_client.utils.files import format_sequence_string
from silex_client.utils.parameter_types import AnyParameter, ListParameterMeta
from silex_nuke.utils.constants import MATCH_FILE_SEQUENCE
from silex_nuke.utils.thread import execute_in_main_thread

# Forward references
if typing.TYPE_CHECKING:
    from silex_client.action.action_query import ActionQuery

import nuke


class SetReferences(CommandBase):

    parameters = {
        "attributes": {
            "label": "Attributes",
            "type": ListParameterMeta(AnyParameter),
            "value": None,
        },
        "values": {
            "label": "Values",
            "type": ListParameterMeta(AnyParameter),
            "value": None,
        },
    }

    def _set_reference(self, attribute: nuke.Knob, value: fileseq.FileSequence) -> str:
        previous_value = attribute.getValue()
        reference_value = format_sequence_string(
            value, previous_value, MATCH_FILE_SEQUENCE
        )

        attribute.setValue(reference_value)
        return reference_value

    @CommandBase.conform_command()
    async def __call__(
        self,
        parameters: Dict[str, Any],
        action_query: ActionQuery,
        logger: logging.Logger,
    ):
        attributes: List[str] = parameters["attributes"]
        values = []
        # TODO: This should be done in the get_value method of the ParameterBuffer
        for value in parameters["values"]:
            value = value.get_value(action_query)[0]
            value = value.get_value(action_query)
            values.append(value)

        # Execute the function in the main thread
        new_values = []
        for attribute, value in zip(attributes, values):
            if not isinstance(value, list):
                value = [value]
            value = fileseq.findSequencesInList(value)[0]

            new_value = await execute_in_main_thread(
                self._set_reference, attribute, value
            )
            logger.info("Attribute %s set to %s", attribute, value)
            new_values.append(new_value)

        return new_values
