# -*- coding: utf-8 -*-

import time

from getpass import getuser

liestudio_task_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "title": "LIEStudio task",
    "description": "A default LIEStudio microservice task",
    "type": "object",
    "properties": {
        "status": {
            "description": "The status of the current task",
            "type": "string",
            "default": "ready",
            "enum": ["ready","submitted","running","failed","aborted","completed","deactivated"]
        },
        "itime": {
            "type": "integer",
            "description": "Time at which the task was initiated as UNIX time stamp",
            "format": "date-time",
            "default": int(time.time())
        },
        "utime": {
            "type": "integer",
            "description": "Time at which the task was finished as UNIX time stamp",
            "format": "date-time"
        },
        "package_name": {
            "type": "string",
            "description": "name of the package exposing WAMP API methods"
        },
        "uri": {
            "type": "string",
            "description": "LIEStudio microservice method uri",
            "pattern": "^\\w+(\\.\\w+)*$"
        },
        "realm": {
            "type": "string",
            "description": "The crossbar WAMP realm the method resides on"
        },
        "system_user": {
            "type": "string",
            "description": "System account name responsible for handling the microservice task",
            "default": getuser()
        },
        "authid": {
            "type": "string",
            "description": "The LIEStudio user name on behalf of which the task was issued"
        },
        "authrole": {
            "type": "string",
            "description": "Crossbar WAMP user role",
            "default": "default"
        },
        "authmethod": {
            "type": "string",
            "description": "Authentication method used"
        },
        "task_id": {
            "type": "string",
            "description": "Unique ID used to identify the task in the system"
        },
        "session": {
            "type": "integer",
            "description": "Crossbar WAMP session ID"
        },
        "class_name": {
            "type": "string",
            "description": "WAMP class name"
        },
        "log_level": {
            "type": "string",
            "desciption": "Log level for the microservice task",
            "default": "info",
            "enum": ["debug","info","warn","error","critical"]
        },
        "app": {
            "type": "string",
            "description": "The WAMP based application name",
            "default": "liestudio"
        }
    },
    "required": ["status","itime","system_user","task_id"]
}