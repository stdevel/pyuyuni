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
    return _result["result"]
