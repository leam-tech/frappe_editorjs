# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "frappe_editorjs"
app_title = "Frappe Editorjs"
app_publisher = "Leam Technology Systems"
app_description = "EditorJS backend"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "admin@leam.ae"
app_license = "MIT"

fixtures = [
    {
        "dt": "Editorjs Template"
    }
]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/frappe_editorjs/css/frappe_editorjs.css"
# app_include_js = "/assets/frappe_editorjs/js/frappe_editorjs.js"

# include js, css files in header of web template
# web_include_css = "/assets/frappe_editorjs/css/frappe_editorjs.css"
# web_include_js = "/assets/frappe_editorjs/js/frappe_editorjs.js"

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

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "frappe_editorjs.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "frappe_editorjs.install.before_install"
# after_install = "frappe_editorjs.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "frappe_editorjs.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"frappe_editorjs.tasks.all"
# 	],
# 	"daily": [
# 		"frappe_editorjs.tasks.daily"
# 	],
# 	"hourly": [
# 		"frappe_editorjs.tasks.hourly"
# 	],
# 	"weekly": [
# 		"frappe_editorjs.tasks.weekly"
# 	]
# 	"monthly": [
# 		"frappe_editorjs.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "frappe_editorjs.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "frappe_editorjs.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "frappe_editorjs.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]
