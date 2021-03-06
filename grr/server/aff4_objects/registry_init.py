#!/usr/bin/env python
"""Load all aff4 objects in order to populate the registry.
"""
# pylint: disable=unused-import
from grr.server.aff4_objects import aff4_grr
from grr.server.aff4_objects import collects
from grr.server.aff4_objects import cronjobs
from grr.server.aff4_objects import filestore
from grr.server.aff4_objects import security
from grr.server.aff4_objects import standard
from grr.server.aff4_objects import stats
from grr.server.aff4_objects import stats_store
from grr.server.aff4_objects import user_managers
from grr.server.aff4_objects import users
