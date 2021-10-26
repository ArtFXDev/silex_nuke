from silex_client.core.context import Context
from silex_client.resolve.config import Config
from silex_client.action.action_query import ActionQuery

actions = [item["name"] for item in Config().actions]


def command(action_name):
    ActionQuery(action_name).execute()


def create_menus():
    for action in actions:
        # nuke.error(action)
        nuke.menu("Nuke").addCommand(
            "SIlex/{}".format(str(action)), lambda: command(action)
        )


Context.get().start_services()
create_menus()
