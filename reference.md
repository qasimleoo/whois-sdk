# Reference
## Dns
<details><summary><code>client.dns.<a href="src/whoisfreaks/dns/client.py">live_dns_lookup</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Live DNS information for a domain or an IP address
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from whoisfreaks import WhoisfreaksApi
from whoisfreaks.environment import WhoisfreaksApiEnvironment
client = WhoisfreaksApi(environment=WhoisfreaksApiEnvironment.PRODUCTION, )
client.dns.live_dns_lookup(api_key='YOUR_API_KEY', domain_name='google.com', type='all', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**domain_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**ip_address:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dns.<a href="src/whoisfreaks/dns/client.py">ns_lookup</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get NS information for a domain
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from whoisfreaks import WhoisfreaksApi
from whoisfreaks.environment import WhoisfreaksApiEnvironment
client = WhoisfreaksApi(environment=WhoisfreaksApiEnvironment.PRODUCTION, )
client.dns.ns_lookup(api_key='YOUR_API_KEY', domain_name='google.com', type='ns', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**domain_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dns.<a href="src/whoisfreaks/dns/client.py">mx_lookup</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get MX information for a domain
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from whoisfreaks import WhoisfreaksApi
from whoisfreaks.environment import WhoisfreaksApiEnvironment
client = WhoisfreaksApi(environment=WhoisfreaksApiEnvironment.PRODUCTION, )
client.dns.mx_lookup(api_key='YOUR_API_KEY', domain_name='google.com', type='mx', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**domain_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dns.<a href="src/whoisfreaks/dns/client.py">historical_dns_lookup</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Historical DNS information for a domain
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from whoisfreaks import WhoisfreaksApi
from whoisfreaks.environment import WhoisfreaksApiEnvironment
client = WhoisfreaksApi(environment=WhoisfreaksApiEnvironment.PRODUCTION, )
client.dns.historical_dns_lookup(api_key='YOUR_API_KEY', domain_name='google.com', type='all', page=1, )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**domain_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dns.<a href="src/whoisfreaks/dns/client.py">reverse_dns_lookup</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Reverse DNS info for a DNS record
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from whoisfreaks import WhoisfreaksApi
from whoisfreaks.environment import WhoisfreaksApiEnvironment
client = WhoisfreaksApi(environment=WhoisfreaksApiEnvironment.PRODUCTION, )
client.dns.reverse_dns_lookup(api_key='YOUR_API_KEY', value='8.8.8.8', type='a', page=1, format='json', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**value:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.dns.<a href="src/whoisfreaks/dns/client.py">bulk_dns_lookup</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Bulk DNS information for multiple domains or IP addresses
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from whoisfreaks import WhoisfreaksApi
from whoisfreaks.environment import WhoisfreaksApiEnvironment
client = WhoisfreaksApi(environment=WhoisfreaksApiEnvironment.PRODUCTION, )
client.dns.bulk_dns_lookup(api_key='YOUR_API_KEY', type='all', format='json', domain_names=['whoisfreaks.com', 'jfreaks.com'], ip_addresses=['1.1.1.1', '8.8.8.8'], )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**domain_names:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**ip_addresses:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Whois
<details><summary><code>client.whois.<a href="src/whoisfreaks/whois/client.py">live_lookup</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get live WHOIS information for a domain
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from whoisfreaks import WhoisfreaksApi
from whoisfreaks.environment import WhoisfreaksApiEnvironment
client = WhoisfreaksApi(environment=WhoisfreaksApiEnvironment.PRODUCTION, )
client.whois.live_lookup(api_key='YOUR_API_KEY', domain_name='888starzci.ci', whois='live', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**domain_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**whois:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.whois.<a href="src/whoisfreaks/whois/client.py">historical_lookup</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get historical WHOIS records for a domain
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from whoisfreaks import WhoisfreaksApi
from whoisfreaks.environment import WhoisfreaksApiEnvironment
client = WhoisfreaksApi(environment=WhoisfreaksApiEnvironment.PRODUCTION, )
client.whois.historical_lookup(api_key='YOUR_API_KEY', domain_name='whoisfreaks.com', whois='historical', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**domain_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**whois:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.whois.<a href="src/whoisfreaks/whois/client.py">reverse_lookup</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Perform a reverse WHOIS lookup based on registrant information
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from whoisfreaks import WhoisfreaksApi
from whoisfreaks.environment import WhoisfreaksApiEnvironment
client = WhoisfreaksApi(environment=WhoisfreaksApiEnvironment.PRODUCTION, )
client.whois.reverse_lookup(api_key='YOUR_API_KEY', whois='reverse', keyword='google', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**whois:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**keyword:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**owner:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**company:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**exact:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**includes:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.whois.<a href="src/whoisfreaks/whois/client.py">ip_whois_lookup</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get WHOIS information for an IP
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from whoisfreaks import WhoisfreaksApi
from whoisfreaks.environment import WhoisfreaksApiEnvironment
client = WhoisfreaksApi(environment=WhoisfreaksApiEnvironment.PRODUCTION, )
client.whois.ip_whois_lookup(api_key='YOUR_API_KEY', ip='8.8.8.8', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**ip:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.whois.<a href="src/whoisfreaks/whois/client.py">asn_whois_lookup</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get WHOIS information for an ASN
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from whoisfreaks import WhoisfreaksApi
from whoisfreaks.environment import WhoisfreaksApiEnvironment
client = WhoisfreaksApi(environment=WhoisfreaksApiEnvironment.PRODUCTION, )
client.whois.asn_whois_lookup(api_key='YOUR_API_KEY', asn='1', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**asn:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.whois.<a href="src/whoisfreaks/whois/client.py">bulk_domain_lookup</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get Live WHOIS information for more than one domain names
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from whoisfreaks import WhoisfreaksApi
from whoisfreaks.environment import WhoisfreaksApiEnvironment
client = WhoisfreaksApi(environment=WhoisfreaksApiEnvironment.PRODUCTION, )
client.whois.bulk_domain_lookup(api_key='YOUR_API_KEY', format='json', domain_names=['whoisfreaks.com', 'jfreaks.com'], )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**domain_names:** `typing.Sequence[str]` 
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

