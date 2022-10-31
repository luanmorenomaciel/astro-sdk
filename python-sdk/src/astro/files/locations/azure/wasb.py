from __future__ import annotations

import os
from urllib.parse import urlparse, urlunparse

from airflow.providers.microsoft.azure.hooks.wasb import WasbHook

from astro.constants import FileLocation
from astro.files.locations.base import BaseFileLocation


class WasbLocation(BaseFileLocation):
    """Handler Wasb object store operations"""

    location_type = FileLocation.WASB

    @property
    def hook(self) -> WasbHook:
        return WasbHook(wasb_conn_id=self.conn_id) if self.conn_id else WasbHook()

    @property
    def transport_params(self) -> dict:
        """get Wasb credentials for storage"""
        client = self.hook.get_conn()
        return {"client": client}
