from silex_client.utils.context import Context
import nuke

Context.get().ws_connection.start_multithreaded()
