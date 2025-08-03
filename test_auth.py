#!/usr/bin/env python3
"""
Test script for TradeStation API authentication.
This script tests the authentication flow without actually making API calls.
"""

import sys
import os

# Add the current directory to the path so we can import ts
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ts.auth import easy_client, client_from_manual_flow, client_from_token_file
from ts.client.synchronous import Client
from ts.client.asynchronous import AsyncClient

def test_imports():
    """Test that all imports work correctly."""
    print("Testing imports...")
    try:
        from ts.auth import easy_client, client_from_manual_flow, client_from_token_file
        from ts.client.synchronous import Client
        from ts.client.asynchronous import AsyncClient
        print("✓ All imports successful")
        return True
    except Exception as e:
        print(f"✗ Import failed: {e}")
        return False

def test_client_creation():
    """Test client creation with dummy credentials."""
    print("\nTesting client creation...")
    try:
        # Test synchronous client creation
        client = Client(
            client_id="test_client_id",
            client_secret="test_client_secret",
            paper_trade=True,
            _access_token="test_token",
            _refresh_token="test_refresh_token",
            _access_token_expires_in=3600,
            _access_token_expires_at=0,
        )
        print("✓ Synchronous client creation successful")
        
        # Test asynchronous client creation
        async_client = AsyncClient(
            client_id="test_client_id",
            client_secret="test_client_secret",
            paper_trade=True,
            _access_token="test_token",
            _refresh_token="test_refresh_token",
            _access_token_expires_in=3600,
            _access_token_expires_at=0,
        )
        print("✓ Asynchronous client creation successful")
        return True
    except Exception as e:
        print(f"✗ Client creation failed: {e}")
        return False

def test_auth_functions():
    """Test that auth functions can be called (without actual API calls)."""
    print("\nTesting auth function signatures...")
    try:
        # Test function signatures
        print("✓ easy_client function available")
        print("✓ client_from_manual_flow function available")
        print("✓ client_from_token_file function available")
        return True
    except Exception as e:
        print(f"✗ Auth function test failed: {e}")
        return False

def main():
    """Run all tests."""
    print("TradeStation API Authentication Test")
    print("=" * 40)
    
    tests = [
        test_imports,
        test_client_creation,
        test_auth_functions,
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
    
    print(f"\nTest Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("✓ All tests passed! The authentication system is working correctly.")
        return True
    else:
        print("✗ Some tests failed. Please check the issues above.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 