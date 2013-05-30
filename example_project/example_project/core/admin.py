from django.contrib import admin

from admin_exporter.actions import export_as_csv_action
from admin_exporter.actions import export_as_json_action
from admin_exporter.actions import export_as_xml_action
from admin_exporter.actions import export_as_yaml_action


admin.site.add_action(export_as_csv_action)
admin.site.add_action(export_as_json_action)
admin.site.add_action(export_as_xml_action)
admin.site.add_action(export_as_yaml_action)
