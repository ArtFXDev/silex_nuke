from typing import Callable

import nuke
from silex_client.utils.thread import ExecutionInThread


class NukeExecutionInMainThread(ExecutionInThread):
    def execute_wrapped_function(self, wrapped_function: Callable):
        nuke.executeInMainThread(wrapped_function)


execute_in_main_thread = NukeExecutionInMainThread()
