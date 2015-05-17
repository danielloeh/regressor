#! /usr/bin/python
import json


def parseSitesFromJson(jsonFile):
	with open(jsonFile) as json_file:
		data = json.load(json_file)
		return data






