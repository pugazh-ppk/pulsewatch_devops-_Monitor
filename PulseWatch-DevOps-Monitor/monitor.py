import ipaddress
import socket
import time
from urllib.parse import urlparse

import requests

def _validate_url(url):
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https") or not parsed.hostname:
        return "Enter a valid http:// or https:// URL."

    host = parsed.hostname
    try:
        # Reject direct private/loopback/link-local IPs.
        ip = ipaddress.ip_address(host)
        if not ip.is_global:
            return "Only publicly reachable websites are allowed."
    except ValueError:
        # For hostnames, reject if any resolved address is non-public.
        try:
            addresses = {item[4][0] for item in socket.getaddrinfo(host, None)}
            if not addresses or any(not ipaddress.ip_address(a).is_global for a in addresses):
                return "Only publicly reachable websites are allowed."
        except socket.gaierror:
            return "Could not resolve this hostname."

    return None

def check_website(url):
    validation_error = _validate_url(url)
    if validation_error:
        return {"ok": False, "error": validation_error}

    start = time.perf_counter()
    try:
        response = requests.get(url, timeout=5, allow_redirects=False,
                                headers={"User-Agent": "PulseWatch/1.0"})
        elapsed_ms = round((time.perf_counter() - start) * 1000, 2)
        return {
            "ok": True,
            "url": url,
            "status_code": response.status_code,
            "response_time_ms": elapsed_ms,
            "online": 200 <= response.status_code < 400,
        }
    except requests.RequestException as exc:
        return {"ok": False, "error": f"Request failed: {exc.__class__.__name__}"}
