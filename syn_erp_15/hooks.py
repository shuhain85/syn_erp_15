# syn_erp_15/hooks.py
from . import __version__ as app_version

app_name = "syn_erp_15"
app_title = "syn_erp_15"
app_publisher = "syn_erp_15"
app_description = "Two-way sync between Godown and Shops"
app_icon = "octicon octicon-sync"
app_color = "grey"
app_email = "shuhain@gmail.com"
app_license = "MIT"

# Document Events: hook into specific doctype submissions
doc_events = {
    "Sales Invoice": {
        "on_submit": "syn_erp_15.sync.enqueue_sales_invoice"
    },
    "Stock Entry": {
        "on_submit": "syn_erp_15.sync.enqueue_stock_entry"
    }
}

# Scheduler Tasks: cron-triggered sync routines
scheduler_events = {
    "cron": [
        {"cron": "*/5 * * * *", "method": "syn_erp_15.sync.perform_sales_sync"},
        {"cron": "0 * * * *",   "method": "syn_erp_15.sync.perform_stock_distribution"}
    ],
    "daily": [
        "syn_erp_15.reports.generate_daily_reconciliation"
    ],
    "weekly": [
        "syn_erp_15.sync.purge_old_logs"
    ]
}

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "syn_erp_15",
# 		"logo": "/assets/syn_erp_15/logo.png",
# 		"title": "syn_erp_15",
# 		"route": "/syn_erp_15",
# 		"has_permission": "syn_erp_15.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/syn_erp_15/css/syn_erp_15.css"
# app_include_js = "/assets/syn_erp_15/js/syn_erp_15.js"

# include js, css files in header of web template
# web_include_css = "/assets/syn_erp_15/css/syn_erp_15.css"
# web_include_js = "/assets/syn_erp_15/js/syn_erp_15.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "syn_erp_15/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "syn_erp_15/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "syn_erp_15.utils.jinja_methods",
# 	"filters": "syn_erp_15.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "syn_erp_15.install.before_install"
# after_install = "syn_erp_15.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "syn_erp_15.uninstall.before_uninstall"
# after_uninstall = "syn_erp_15.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "syn_erp_15.utils.before_app_install"
# after_app_install = "syn_erp_15.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "syn_erp_15.utils.before_app_uninstall"
# after_app_uninstall = "syn_erp_15.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "syn_erp_15.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"syn_erp_15.tasks.all"
# 	],
# 	"daily": [
# 		"syn_erp_15.tasks.daily"
# 	],
# 	"hourly": [
# 		"syn_erp_15.tasks.hourly"
# 	],
# 	"weekly": [
# 		"syn_erp_15.tasks.weekly"
# 	],
# 	"monthly": [
# 		"syn_erp_15.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "syn_erp_15.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "syn_erp_15.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "syn_erp_15.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["syn_erp_15.utils.before_request"]
# after_request = ["syn_erp_15.utils.after_request"]

# Job Events
# ----------
# before_job = ["syn_erp_15.utils.before_job"]
# after_job = ["syn_erp_15.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"syn_erp_15.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

