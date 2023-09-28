"""
Class for interacting with hosts
"""

def list_systems_requiring_reboot(api_client):
    """
    Lists all systems requiring a reboot
    """
    _result = api_client.query(
        "system/listSuggestedReboot"
    )
    _systems = []
    for _system in _result["result"]:
        _systems.append(_system["name"])
    return _systems
