# WhoisFreaks Python SDK

A Python package to interact with the WhoisFreaks API, providing services such as Whois lookup, domain availability checks, DNS information, and SSL certificate details.

## Installation

To install the SDK, use pip:


```bash
pip install whois-sdk
```

## Configuration

Before using the SDK, obtain a free API key by signing up at [WhoisFreaks](https://whoisfreaks.com). Once you have your API key, configure it in your environment variables:


```bash
export WHOISFREAKS_API_KEY='your_api_key_here'
```

Alternatively, you can set the API key directly in your Python script:


```python
import whoisfreaks

whoisfreaks.api_key = 'your_api_key_here'
```

## Usage

### Whois Lookup

To perform a Whois lookup:


```python
import whoisfreaks

domain_info = whoisfreaks.whois('example.com')
print(domain_info)
```

### Domain Availability

To check if a domain is available:


```python
import whoisfreaks

availability = whoisfreaks.domain_availability('example.com')
print(availability)
```

### DNS Information

To retrieve DNS records:


```python
import whoisfreaks

dns_info = whoisfreaks.dns('example.com')
print(dns_info)
```

### SSL Certificate Details

To get SSL certificate information:


```python
import whoisfreaks

ssl_info = whoisfreaks.ssl('example.com')
print(ssl_info)
```

## Error Handling

The SDK raises exceptions for various error conditions:

- `whoisfreaks.exceptions.APIError`: Raised for general API errors.
- `whoisfreaks.exceptions.InvalidDomain`: Raised when a domain is invalid.
- `whoisfreaks.exceptions.NetworkError`: Raised for network-related issues.

Example of handling exceptions:


```python
import whoisfreaks
from whoisfreaks.exceptions import APIError, InvalidDomain

try:
    domain_info = whoisfreaks.whois('example.com')
    print(domain_info)
except InvalidDomain:
    print("The domain is invalid.")
except APIError as e:
    print(f"API error occurred: {e}")
```

## License

This SDK is released under the MIT License.

---

This README provides a structured approach to using the WhoisFreaks API in Python, aligning with the functionalities offered in the Python SDK. For more detailed information and updates.
