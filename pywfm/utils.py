def build_url(base_url: str, endpoint: str, slug: str = "") -> str:
    """Build a complete URL from base URL and endpoint."""
    if slug:
        endpoint = endpoint.format(slug=slug)
    return f"{base_url}{endpoint}"