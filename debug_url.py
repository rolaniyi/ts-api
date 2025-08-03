#!/usr/bin/env python3
"""
Debug script to help analyze URL parsing issues
"""

from urllib.parse import urlparse, parse_qs

def debug_url(url):
    """Debug a URL to see what parameters are found"""
    print(f"Original URL: {url}")
    
    parsed_url = urlparse(url)
    print(f"Scheme: {parsed_url.scheme}")
    print(f"Netloc: {parsed_url.netloc}")
    print(f"Path: {parsed_url.path}")
    print(f"Query: {parsed_url.query}")
    
    query_params = parse_qs(parsed_url.query)
    print(f"Query parameters: {query_params}")
    
    code_list = query_params.get("code", [])
    if code_list:
        print(f"Authorization code found: {code_list[0]}")
    else:
        print("No authorization code found!")
        print("Available parameters:", list(query_params.keys()))

if __name__ == "__main__":
    print("Paste the redirect URL you received from TradeStation:")
    url = input().strip()
    debug_url(url) 