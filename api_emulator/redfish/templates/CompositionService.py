# Copyright Notice:
# Copyright 2016 Distributed Management Task Force, Inc. All rights reserved.
# License: BSD 3-Clause License. For full text see link: https://github.com/DMTF/Redfish-Interface-Emulator/LICENSE.md

# get_CompositionService_instance()

import copy
import strgen

_TEMPLATE = \
{
    "@Redfish.Copyright": "Copyright 2014-2016 Distributed Management Task Force, Inc. (DMTF). All rights reserved.",
    "@odata.context": "{rb}$metadata#CompositionService.CompositionService",
    "@odata.type": "#CompositionService.v1_0_0.CompositionService",
    "@odata.id": "{rb}CompositionService",
    "Id": "{id}",
    "Name": "Composition Service",
    "Status": {
        "State": "Enabled",
        "Health": "OK"
    },
    "ServiceEnabled": "true",
    "ResourceBlocks": {
        "@odata.id": "{rb}CompositionService/ResourceBlocks"
    },
    "ResourceZones": {
        "@odata.id": "{rb}CompositionService/ResourceZones"
    }
}


def get_CompositionService_instance(wildcards):
    """
    Instantiates and formats the template

    Arguments:
        wildcard - A dictionary of wildcards strings and their repalcement values
    """
    c = copy.deepcopy(_TEMPLATE)

    c['@odata.context'] = c['@odata.context'].format(**wildcards)
    c['@odata.id'] = c['@odata.id'].format(**wildcards)
    c['Id'] = c['Id'].format(**wildcards)
    c['ResourceBlocks']['@odata.id'] = c['ResourceBlocks']['@odata.id'].format(**wildcards)
    c['ResourceZones']['@odata.id'] = c['ResourceZones']['@odata.id'].format(**wildcards)

    return c
