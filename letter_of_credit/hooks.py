app_name = "letter_of_credit"
app_title = "Letter of Credit"
app_publisher = "Sowaan"
app_description = "Letter of Credit"
app_email = "sufyan.sadiq@sowaan.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "letter_of_credit",
# 		"logo": "/assets/letter_of_credit/logo.png",
# 		"title": "Letter of Credit",
# 		"route": "/letter_of_credit",
# 		"has_permission": "letter_of_credit.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------





fixtures = [
	{
		"doctype":"Custom Field",
		"filters":[
			[
				"module","=","Letter of Credit"
			]
		]
	}

]






# include js, css files in header of desk.html
# app_include_css = "/assets/letter_of_credit/css/letter_of_credit.css"
# app_include_js = "/assets/letter_of_credit/js/letter_of_credit.js"

# include js, css files in header of web template
# web_include_css = "/assets/letter_of_credit/css/letter_of_credit.css"
# web_include_js = "/assets/letter_of_credit/js/letter_of_credit.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "letter_of_credit/public/scss/website"

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
# app_include_icons = "letter_of_credit/public/icons.svg"

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
# 	"methods": "letter_of_credit.utils.jinja_methods",
# 	"filters": "letter_of_credit.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "letter_of_credit.install.before_install"
# after_install = "letter_of_credit.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "letter_of_credit.uninstall.before_uninstall"
# after_uninstall = "letter_of_credit.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "letter_of_credit.utils.before_app_install"
# after_app_install = "letter_of_credit.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "letter_of_credit.utils.before_app_uninstall"
# after_app_uninstall = "letter_of_credit.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "letter_of_credit.notifications.get_notification_config"

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
# 		"letter_of_credit.tasks.all"
# 	],
# 	"daily": [
# 		"letter_of_credit.tasks.daily"
# 	],
# 	"hourly": [
# 		"letter_of_credit.tasks.hourly"
# 	],
# 	"weekly": [
# 		"letter_of_credit.tasks.weekly"
# 	],
# 	"monthly": [
# 		"letter_of_credit.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "letter_of_credit.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "letter_of_credit.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "letter_of_credit.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["letter_of_credit.utils.before_request"]
# after_request = ["letter_of_credit.utils.after_request"]

# Job Events
# ----------
# before_job = ["letter_of_credit.utils.before_job"]
# after_job = ["letter_of_credit.utils.after_job"]

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
# 	"letter_of_credit.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

