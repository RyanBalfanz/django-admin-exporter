from django.contrib import admin
from django.core import serializers
from django.http import HttpResponse


def serialize_queryset(queryset, format):
	data = serializers.serialize(format, queryset)
	return data

def export(queryset, format):
	data = serialize_queryset(queryset, format)

	response = HttpResponse(data, mimetype="application/x-download")
	response["Content-Disposition"] = "attachment;filename=export.{extention}".format(extention=format.lower())

	return response

def export_as_json_action(modeladmin, request, queryset):
	return export(queryset, format="json")
export_as_json_action.short_description = "Export selected items to JSON"

def export_as_xml_action(modeladmin, request, queryset):
	return export(queryset, format="xml")
export_as_xml_action.short_description = "Export selected items to XML"

def export_as_yaml_action(modeladmin, request, queryset):
	return export(queryset, format="yaml")
export_as_yaml_action.short_description = "Export selected items to YAML"
