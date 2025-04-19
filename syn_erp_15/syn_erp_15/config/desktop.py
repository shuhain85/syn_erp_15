# syn_erp_15/config/desktop.py
from frappe import _

def get_data():
    return [{
        "module_name": "Sync ERP",
        "label": _("Sync ERP"),
        "icon": "octicon octicon-sync",
        "items": [
            {"type": "doctype", "name": "Sync Settings"},
            {"type": "page",   "name": "sync-dashboard"}
        ]
    }]