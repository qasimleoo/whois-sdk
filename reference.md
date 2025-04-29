# Reference
## Whois
<details><summary><code>client.whois.<a href="src/whoisfreaks/whois/client.py">get_live_whois</a>(...)</code></summary>
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
client.whois.get_live_whois(api_key='YOUR_API_KEY', domain_name='888starzci.ci', whois='live', )

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

<details><summary><code>client.whois.<a href="src/whoisfreaks/whois/client.py">get_historical_whois</a>(...)</code></summary>
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
client.whois.get_historical_whois(api_key='YOUR_API_KEY', domain_name='whoisfreaks.com', whois='historical', )

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

<details><summary><code>client.whois.<a href="src/whoisfreaks/whois/client.py">get_reverse_whois</a>(...)</code></summary>
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
client.whois.get_reverse_whois(api_key='YOUR_API_KEY', whois='reverse', keyword='google', )

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

<details><summary><code>client.whois.<a href="src/whoisfreaks/whois/client.py">get_ip_whois</a>(...)</code></summary>
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
client.whois.get_ip_whois(api_key='YOUR_API_KEY', ip='8.8.8.8', )

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

<details><summary><code>client.whois.<a href="src/whoisfreaks/whois/client.py">get_asn_whois</a>(...)</code></summary>
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
client.whois.get_asn_whois(api_key='YOUR_API_KEY', asn='1', )

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

<details><summary><code>client.whois.<a href="src/whoisfreaks/whois/client.py">get_bulk_whois</a>(...)</code></summary>
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
client.whois.get_bulk_whois(api_key='YOUR_API_KEY', format='json', domain_names=['whoisfreaks.com', 'jfreaks.com'], )

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

