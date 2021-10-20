from silex_client.core.context import Context
from silex_client.utils.log import logger
import traceback

actions = [item["name"] for item in Context.get().config.actions]

def command(action_name):
    Context.get().get_action(action_name).execute()

def creat_menus():
    for action in actions:
        #nuke.error(action)
        nuke.menu('Nuke').addCommand('SIlex/{}'.format(str(action)), lambda: command(action))

creat_menus()
