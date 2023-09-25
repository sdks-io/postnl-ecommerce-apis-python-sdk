
# Getting Started with PostNL Ecommerce APIs

## Introduction

Collection of PostNL API's for ecommerce processes

## Install the Package

The package is compatible with Python versions `3 >=3.7, <= 3.11`.
Install the package from PyPi using the following pip command:

```python
pip install sdksio-postnl-ecommerce-apis-sdk==1.0.0
```

You can also view the package at:
https://pypi.python.org/pypi/sdksio-postnl-ecommerce-apis-sdk/1.0.0

## Test the SDK

You can test the generated SDK and the server with test cases. `unittest` is used as the testing framework and `pytest` is used as the test runner. You can run the tests as follows:

Navigate to the root directory of the SDK and run the following commands

```
pip install -r test-requirements.txt
pytest
```

## Initialize the API Client

**_Note:_** Documentation for the client can be found [here.](https://www.github.com/sdks-io/postnl-ecommerce-apis-python-sdk/tree/1.0.0/doc/client.md)

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| `environment` | Environment | The API environment. <br> **Default: `Environment.PRODUCTION`** |
| `http_client_instance` | `HttpClient` | The Http Client passed from the sdk user for making requests |
| `override_http_client_configuration` | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| `http_call_back` | `HttpCallBack` | The callback value that is invoked before and after an HTTP call is made to an endpoint |
| `timeout` | `float` | The value to use for connection timeout. <br> **Default: 60** |
| `max_retries` | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| `backoff_factor` | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| `retry_statuses` | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| `retry_methods` | `Array of string` | The http methods on which retry is to be done. <br> **Default: ['GET', 'PUT']** |
| `apikey` | `str` |  |

The API client can be initialized as follows:

```python
from postnlecommerceapis.postnlecommerceapis_client import PostnlecommerceapisClient
from postnlecommerceapis.configuration import Environment

client = PostnlecommerceapisClient(
    apikey='apikey'
)
```

## Environments

The SDK can be configured to use a different environment for making API calls. Available environments are:

### Fields

| Name | Description |
|  --- | --- |
| production | **Default** |
| environment2 | - |

## Authorization

This API uses `Custom Header Signature`.

## List of APIs

* [Postalcodecheck](https://www.github.com/sdks-io/postnl-ecommerce-apis-python-sdk/tree/1.0.0/doc/controllers/postalcodecheck.md)
* [Track Trace](https://www.github.com/sdks-io/postnl-ecommerce-apis-python-sdk/tree/1.0.0/doc/controllers/track-trace.md)
* [Checkout](https://www.github.com/sdks-io/postnl-ecommerce-apis-python-sdk/tree/1.0.0/doc/controllers/checkout.md)
* [Deliverydate](https://www.github.com/sdks-io/postnl-ecommerce-apis-python-sdk/tree/1.0.0/doc/controllers/deliverydate.md)
* [Locations](https://www.github.com/sdks-io/postnl-ecommerce-apis-python-sdk/tree/1.0.0/doc/controllers/locations.md)
* [Timeframes](https://www.github.com/sdks-io/postnl-ecommerce-apis-python-sdk/tree/1.0.0/doc/controllers/timeframes.md)
* [Labelling](https://www.github.com/sdks-io/postnl-ecommerce-apis-python-sdk/tree/1.0.0/doc/controllers/labelling.md)
* [Barcode](https://www.github.com/sdks-io/postnl-ecommerce-apis-python-sdk/tree/1.0.0/doc/controllers/barcode.md)
* [Confirming](https://www.github.com/sdks-io/postnl-ecommerce-apis-python-sdk/tree/1.0.0/doc/controllers/confirming.md)

## Classes Documentation

* [Utility Classes](https://www.github.com/sdks-io/postnl-ecommerce-apis-python-sdk/tree/1.0.0/doc/utility-classes.md)
* [HttpResponse](https://www.github.com/sdks-io/postnl-ecommerce-apis-python-sdk/tree/1.0.0/doc/http-response.md)
* [HttpRequest](https://www.github.com/sdks-io/postnl-ecommerce-apis-python-sdk/tree/1.0.0/doc/http-request.md)

