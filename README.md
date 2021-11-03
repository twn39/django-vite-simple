## vitejs for django

### Install

```py
INSTALLED_APPS = [
    'vitejs',
    ...
]
```


### Usage

```python
VITE_URL = 'http://localhost:3000' # vite host 
VITE_ENTRY = '/src/main.ts'  # vite entry path
```

use tags in template:

```html
{% vite_client %} 
{% vite_entry %}
```