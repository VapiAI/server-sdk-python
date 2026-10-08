# Vapi Python Library

[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-Built%20with%20Fern-brightgreen)](https://buildwithfern.com?utm_source=github&utm_medium=github&utm_campaign=readme&utm_source=https%3A%2F%2Fgithub.com%2FVapiAI%2Fserver-sdk-python)
[![pypi](https://img.shields.io/pypi/v/vapi_server_sdk)](https://pypi.python.org/pypi/vapi_server_sdk)

The Vapi Python library provides convenient access to the Vapi API from Python.

## Installation

This release supports Python 3.10 through 3.14.

```bash
python -m pip install vapi_server_sdk
```

Install the optional async transport:

```bash
python -m pip install "vapi_server_sdk[aiohttp]"
```

## Upgrade to 3.0.0

Version 3.0.0 updates the generated types to the current Vapi API definition. Review the [3.0.0 migration notes](./changelog.md) before upgrading from 1.x. Public helper imports, declared model fields, and structured-output run response types have changed.

```bash
python -m pip install --upgrade "vapi_server_sdk>=3.0.0,<4"
```

## Reference

See the [Python SDK reference](./reference.md) for methods, parameters, and response types.

## Usage

Set the `VAPI_API_KEY` environment variable to your Vapi private API key. Create a client and list up to 10 assistants in your organization:

```python
import os

from vapi import Vapi

client = Vapi(token=os.environ["VAPI_API_KEY"])
assistants = client.assistants.list(limit=10)
for assistant in assistants:
    print(assistant.id)
```

## Async Client

Use `AsyncVapi` to await API requests:

```python
import asyncio
import os

from vapi import AsyncVapi


async def main() -> None:
    client = AsyncVapi(token=os.environ["VAPI_API_KEY"])
    assistants = await client.assistants.list(limit=10)
    for assistant in assistants:
        print(assistant.id)


asyncio.run(main())
```

## Exception Handling

Catch `ApiError` to inspect an unsuccessful API response:

```python
import os

from vapi import Vapi
from vapi.core.api_error import ApiError

client = Vapi(token=os.environ["VAPI_API_KEY"])
try:
    client.assistants.list(limit=10)
except ApiError as error:
    print(error.status_code)
    print(error.body)
```

## List Resources

`client.assistants.list()` returns a Python list. Use its `limit` and timestamp filters to select results. Other endpoints have their own response types and pagination parameters; consult the [SDK reference](./reference.md) for the endpoint you use.

## Advanced

### Retries

The SDK retries HTTP 408, 409, 429, and 5xx responses with backoff. The default maximum is two retries. Set `max_retries` for an individual request:

```python
import os

from vapi import Vapi

client = Vapi(token=os.environ["VAPI_API_KEY"])
client.assistants.list(limit=10, request_options={"max_retries": 1})
```

### Timeouts

The default client timeout is 60 seconds. Set `timeout` when creating the client or override it with `timeout_in_seconds` for a request. When you supply a custom HTTPX client, its read timeout becomes the default unless you set `timeout` explicitly.

```python
import os

from vapi import Vapi

client = Vapi(token=os.environ["VAPI_API_KEY"], timeout=20.0)
client.assistants.list(limit=10, request_options={"timeout_in_seconds": 1})
```

### Custom Client

Pass an HTTPX client to configure its transport. This example sets `HTTPTransport.local_address` and closes the custom client when the block finishes:

```python
import os

import httpx
from vapi import Vapi

with httpx.Client(transport=httpx.HTTPTransport(local_address="0.0.0.0")) as http:
    client = Vapi(token=os.environ["VAPI_API_KEY"], httpx_client=http)
    assistants = client.assistants.list(limit=10)
    for assistant in assistants:
        print(assistant.id)
```

## Contributing

While we value open-source contributions to this SDK, this library is generated programmatically.
Additions made directly to this library would have to be moved over to our generation code,
otherwise they would be overwritten upon the next generated release. Feel free to open a PR as
a proof of concept, but know that we will not be able to merge it as-is. We suggest opening
an issue first to discuss with us!

On the other hand, contributions to the README are always very welcome!
