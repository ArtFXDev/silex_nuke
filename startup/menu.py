import nuke
from silex_client.action.action_query import ActionQuery
from silex_client.core.context import Context
from silex_client.resolve.config import Config


def create_menus():
    # Get actions names from the config
    actions = [item["name"] for item in Config().actions]

    # Create a menu
    menubar = nuke.menu("Nodes")
    silex_menu = menubar.addMenu("Silex", icon="silex_logo.png")

    for action_name in actions:
        execute_action = lambda action=action_name: ActionQuery(action).execute()

        # Create an entry in the Silex menu
        silex_menu.addCommand(
            action_name,
            execute_action,
            icon=f"{action_name}.svg",
        )


# Start the WS connection
Context.get().start_services()
create_menus()

# Override Ctrl+S and script save
save_menu = nuke.menu("Nuke").findItem("File").findItem("Save Comp")
save_menu.setScript("ActionQuery('save').execute()")
