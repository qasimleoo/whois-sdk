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

Get WHOIS information for a domain
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
client = WhoisfreaksApi(base_url="https://yourhost.com/path/to/api", )
client.whois.get_whois(api_key='YOUR_API_KEY', whois='live', domain_name='888starzci.ci', )

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

**domain_name:** `str` 
    
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

