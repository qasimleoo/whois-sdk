# Reference
## Whois
<details><summary><code>client.whois.<a href="src/whoisfreaks/whois/client.py">get_whois</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get WHOIS information for a domain (live, historical or reverse)
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
client.whois.get_whois(api_key='YOUR_API_KEY', whois='reverse', keyword='google', email='google@gmail.com', owner='markmonitor', company='google', mode='mini', exact='true', format='xml', includes='billing', page='3', )

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

**domain_name:** `typing.Optional[str]` 
    
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

