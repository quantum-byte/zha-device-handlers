"""Module for Sinope quirks implementations."""
from zhaquirks.const import (
    ARGS,
    ATTRIBUTE_ID,
    ATTRIBUTE_NAME,
    CLUSTER_ID,
    COMMAND,
    COMMAND_BUTTON_DOUBLE,
    COMMAND_BUTTON_HOLD,
    COMMAND_BUTTON_SINGLE,
    DOUBLE_PRESS,
    ENDPOINT_ID,
    LONG_PRESS,
    SHORT_PRESS,
    TURN_OFF,
    TURN_ON,
    VALUE,
)

SINOPE = "Sinope Technologies"
ATTRIBUTE_ACTION = "actionReport"

LIGHT_DEVICE_TRIGGERS = {
    (SHORT_PRESS, TURN_ON): {
        ENDPOINT_ID: 1,
        CLUSTER_ID: 65281,
        COMMAND: COMMAND_BUTTON_SINGLE,
        ARGS: {ATTRIBUTE_ID: 84, ATTRIBUTE_NAME: ATTRIBUTE_ACTION, VALUE: 2},
    },
    (SHORT_PRESS, TURN_OFF): {
        ENDPOINT_ID: 1,
        CLUSTER_ID: 65281,
        COMMAND: COMMAND_BUTTON_SINGLE,
        ARGS: {ATTRIBUTE_ID: 84, ATTRIBUTE_NAME: ATTRIBUTE_ACTION, VALUE: 18},
    },
    (DOUBLE_PRESS, TURN_ON): {
        ENDPOINT_ID: 1,
        CLUSTER_ID: 65281,
        COMMAND: COMMAND_BUTTON_DOUBLE,
        ARGS: {ATTRIBUTE_ID: 84, ATTRIBUTE_NAME: ATTRIBUTE_ACTION, VALUE: 4},
    },
    (DOUBLE_PRESS, TURN_OFF): {
        ENDPOINT_ID: 1,
        CLUSTER_ID: 65281,
        COMMAND: COMMAND_BUTTON_DOUBLE,
        ARGS: {ATTRIBUTE_ID: 84, ATTRIBUTE_NAME: ATTRIBUTE_ACTION, VALUE: 20},
    },
    (LONG_PRESS, TURN_ON): {
        ENDPOINT_ID: 1,
        CLUSTER_ID: 65281,
        COMMAND: COMMAND_BUTTON_HOLD,
        ARGS: {ATTRIBUTE_ID: 84, ATTRIBUTE_NAME: ATTRIBUTE_ACTION, VALUE: 3},
    },
    (LONG_PRESS, TURN_OFF): {
        ENDPOINT_ID: 1,
        CLUSTER_ID: 65281,
        COMMAND: COMMAND_BUTTON_HOLD,
        ARGS: {ATTRIBUTE_ID: 84, ATTRIBUTE_NAME: ATTRIBUTE_ACTION, VALUE: 19},
    },
}
