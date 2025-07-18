#!/usr/bin/env python3
"""
#############################################################################
#
# Module contains an implementation of SONiC Platform Base API and
# provides the platform information
#
#############################################################################
"""
try:
    from sonic_platform_base.platform_base import PlatformBase
    from sonic_platform.chassis import Chassis
except ImportError as err:
    raise ImportError(str(err) + "- required module not found")


class Platform(PlatformBase):
    """
    DELLEMC Platform-specific class
    """

    def __init__(self):
        PlatformBase.__init__(self)
        self._chassis = Chassis()
