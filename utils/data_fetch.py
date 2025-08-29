"""
utils/data_fetch.py

Helper functions to fetch ITS_LIVE glacier velocity datasets
by glacier name or bounding box.
"""

import requests
import xarray as xr
from itslive import ITS_LIVE
from geopy.geocoders import Nominatim


def geocode_glacier(name: str, buffer_deg: float = 0.2):
    """
    Geocode a glacier name into a bounding box.
    Uses OpenStreetMap via geopy (Nominatim).
    """
    geolocator = Nominatim(user_agent="glaciotrack")
    loc = geolocator.geocode(name)
    if loc is None:
        raise ValueError(f"Could not geocode glacier name: {name}")

    lat, lon = loc.latitude, loc.longitude
    bbox = [
        lon - buffer_deg,
        lat - buffer_deg,
        lon + buffer_deg,
        lat + buffer_deg,
    ]
    return bbox


def fetch_velocity_dataset(aoi, dataset_index: int = 0):
    """
    Query ITS_LIVE for velocity datasets intersecting an AOI (bounding box).
    Returns an xarray.Dataset (NetCDF opened from AWS S3).
    """
    client = ITS_LIVE()
    results = client.search(aoi)

    if not results:
        raise RuntimeError("No ITS_LIVE datasets found for AOI")

    url = results[dataset_index]["url"]
    ds = xr.open_dataset(url)
    return ds


def fetch_by_name(name: str, buffer_deg: float = 0.2, dataset_index: int = 0):
    """
    Convenience wrapper: provide glacier name, return ITS_LIVE dataset.
    """
    bbox = geocode_glacier(name, buffer_deg=buffer_deg)
    return fetch_velocity_dataset(bbox, dataset_index=dataset_index)


if __name__ == "__main__":
    # Example usage: fetch Columbia Glacier dataset
    ds = fetch_by_name("Columbia Glacier, Alaska")
    print(ds)
