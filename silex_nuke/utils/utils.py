from typing import Callable
from silex_client.utils.log import logger
from concurrent import futures
import nuke


class Utils:

    @staticmethod
    async def wrapped_execute(action_query, nuke_function: Callable):

        future = action_query.event_loop.loop.create_future()
        def wrapped_function():
            result = nuke_function()
            future.set_result(result)
        nuke.executeInMainThread(wrapped_function)

        def callback(task_result: futures.Future):
            if task_result.cancelled():
                return

            exception = task_result.exception()
            if exception:
                logger.error("Exception raised %s", exception)

        future.add_done_callback(callback)
        return future