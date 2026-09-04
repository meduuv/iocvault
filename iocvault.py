"""Offline IOC normalization utilities."""
import ipaddress
import re

_HASH = re.compile(r"^[0-9a-fA-F]{32,128}$")

def classify(value: str) -> str:
    v = value.strip().lower()
    try:
        ipaddress.ip_address(v)
        return "ip"
    except ValueError:
        pass
    if _HASH.fullmatch(v) and len(v) in (32, 40, 64, 128):
        return {32:"md5",40:"sha1",64:"sha256",128:"sha512"}[len(v)]
    if v.startswith(("http://", "https://")):
        return "url"
    if "." in v and " " not in v:
        return "domain"
    return "unknown"

def normalize(values):
    seen = set()
    result = []
    for value in values:
        item = str(value).strip().lower()
        if item and item not in seen:
            seen.add(item)
            result.append({"value": item, "type": classify(item)})
    return result
