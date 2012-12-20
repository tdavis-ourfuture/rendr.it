"""
Constants for CollectdClient
"""

MAX_PACKET_SIZE = 1024  # bytes

TYPE_HOST = 0x0000
TYPE_TIME = 0x0001
TYPE_PLUGIN = 0x0002
TYPE_PLUGIN_INSTANCE = 0x0003
TYPE_TYPE = 0x0004
TYPE_TYPE_INSTANCE = 0x0005
TYPE_VALUES = 0x0006
TYPE_INTERVAL = 0x0007
LONG_INT_CODES = [TYPE_TIME, TYPE_INTERVAL]
STRING_CODES = [
    TYPE_HOST,
    TYPE_PLUGIN,
    TYPE_PLUGIN_INSTANCE,
    TYPE_TYPE,
    TYPE_TYPE_INSTANCE
]

VALUE_COUNTER = 0
VALUE_GAUGE = 1
VALUE_DERIVE = 2
VALUE_ABSOLUTE = 3
VALUE_CODES = {
    VALUE_COUNTER: "!Q",
    VALUE_GAUGE: "<d",
    VALUE_DERIVE: "!q",
    VALUE_ABSOLUTE: "!Q"
}

DEFAULT_PLUGIN_NAME = "any"
DEFAULT_PLUGIN_INSTANCE = ""
DEFAULT_PLUGIN_TYPE = "gauge"
DEFAULT_SEND_INTERVAL = 10  # seconds
DEFAULT_PORT = 25826
DEFAULT_CUMM_FUNCTION = sum
