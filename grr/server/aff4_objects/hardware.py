#!/usr/bin/env python
"""AFF4 objects for managing Chipsec responses."""

from grr_response_client.components.chipsec_support.actions import chipsec_types

from grr.server import sequential_collection


class ACPITableDataCollection(
    sequential_collection.IndexedSequentialCollection):
  """A collection of ACPI table data."""
  RDF_TYPE = chipsec_types.ACPITableData
