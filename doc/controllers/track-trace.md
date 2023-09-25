# Track Trace

```python
track_trace_controller = client.track_trace
```

## Class Name

`TrackTraceController`

## Methods

* [Returns the Statuses for a Particular Barcode](../../doc/controllers/track-trace.md#returns-the-statuses-for-a-particular-barcode)
* [Get Status Information by Customer Reference](../../doc/controllers/track-trace.md#get-status-information-by-customer-reference)
* [Returns the Signature of a Particular Shipment](../../doc/controllers/track-trace.md#returns-the-signature-of-a-particular-shipment)
* [Returns the Updated Statuses for a Particular Customer Number](../../doc/controllers/track-trace.md#returns-the-updated-statuses-for-a-particular-customer-number)


# Returns the Statuses for a Particular Barcode

Request example:

```
curl -X GET "https://api-sandbox.postnl.nl/shipment/v2/status/barcode/3SDEVC172649258" \
 -H "Accept: application/json" \
 -H "apikey: APIKEY-HERE" \
```

```python
def returns_the_statuses_for_a_particular_barcode(self,
                                                 barcode,
                                                 detail=False,
                                                 language=None,
                                                 max_days=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `barcode` | [`str`](../../doc/models/string-enum.md) | Template, Required | Barcode of the shipment. This is a unique value. |
| `detail` | `bool` | Query, Optional | Option to include old statuses in the response<br>**Default**: `False` |
| `language` | [`LanguageEnum`](../../doc/models/language-enum.md) | Query, Optional | Language of the returned shipment and status descriptions (default is Dutch). |
| `max_days` | [`str`](../../doc/models/string-enum.md) | Query, Optional | Limit the number of days that will be searched (decrease this amount for better performance). |

## Response Type

[`ShippingstatusResponse`](../../doc/models/shippingstatus-response.md)

## Example Usage

```python
barcode = '3SDEVC172649258'

detail = False

language = LanguageEnum.NL

max_days = '14'

result = track_trace_controller.returns_the_statuses_for_a_particular_barcode(
    barcode,
    detail=detail,
    language=language,
    max_days=max_days
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid request | [`ShippingstatusResponseErrorException`](../../doc/models/shippingstatus-response-error-exception.md) |
| 401 | Invalid apikey | [`ShippingstatusUnauthorizedException`](../../doc/models/shippingstatus-unauthorized-exception.md) |
| 405 | Method not allowed | [`ShippingstatusMethodNotAllowedException`](../../doc/models/shippingstatus-method-not-allowed-exception.md) |
| 429 | Too many requests | [`ShippingstatusTooManyRequestException`](../../doc/models/shippingstatus-too-many-request-exception.md) |
| 500 | Internal server error | [`ShippingstatusResponseErrorException`](../../doc/models/shippingstatus-response-error-exception.md) |


# Get Status Information by Customer Reference

Request example:

```
curl -X GET "https://api-sandbox.postnl.nl/shipment/v2/status/reference?detail=true&language=NL&customerCode={{CustomerCode}}&customerNumber={{CustomerNumber}}&reference=REF98173245876329" \
 -H "Accept: application/json" \
 -H "apikey: APIKEY-HERE" 
```

```python
def get_status_information_by_customer_reference(self,
                                                customer_code,
                                                customer_number,
                                                reference_id,
                                                detail=False,
                                                language=None,
                                                max_days=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_code` | [`str`](../../doc/models/string-enum.md) | Query, Required | Customer code as known at PostNL Pakketten |
| `customer_number` | [`str`](../../doc/models/string-enum.md) | Query, Required | Customer number as known at PostNL Pakketten |
| `reference_id` | [`str`](../../doc/models/string-enum.md) | Template, Required | The customer reference belonging to the shipment |
| `detail` | `bool` | Query, Optional | Option to include old statuses in the response<br>**Default**: `False` |
| `language` | [`LanguageEnum`](../../doc/models/language-enum.md) | Query, Optional | Language of the returned shipment and status descriptions (default is Dutch). |
| `max_days` | [`str`](../../doc/models/string-enum.md) | Query, Optional | Limit the number of days that will be searched (decrease this amount for better performance). By default this is 90 days in the past. |

## Response Type

[`ShippingstatusResponse`](../../doc/models/shippingstatus-response.md)

## Example Usage

```python
customer_code = 'DEVC'

customer_number = '11223344'

reference_id = 'REF-12345'

detail = False

language = LanguageEnum.NL

max_days = '14'

result = track_trace_controller.get_status_information_by_customer_reference(
    customer_code,
    customer_number,
    reference_id,
    detail=detail,
    language=language,
    max_days=max_days
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid request | [`ShippingstatusResponseErrorException`](../../doc/models/shippingstatus-response-error-exception.md) |
| 401 | Invalid apikey | [`ShippingstatusUnauthorizedException`](../../doc/models/shippingstatus-unauthorized-exception.md) |
| 405 | Method not allowed | [`ShippingstatusMethodNotAllowedException`](../../doc/models/shippingstatus-method-not-allowed-exception.md) |
| 429 | Too many requests | [`ShippingstatusTooManyRequestException`](../../doc/models/shippingstatus-too-many-request-exception.md) |
| 500 | Internal server error | [`ShippingstatusResponseErrorException`](../../doc/models/shippingstatus-response-error-exception.md) |


# Returns the Signature of a Particular Shipment

Request example:

```
curl -X GET "https://api-sandbox.postnl.nl/shipment/v2/status/signature/3SDEVC172649258" \
 -H "Accept: application/json" \
 -H "apikey: APIKEY-HERE" 
```

```python
def returns_the_signature_of_a_particular_shipment(self,
                                                  barcode)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `barcode` | [`str`](../../doc/models/string-enum.md) | Template, Required | Barcode of the shipment |

## Response Type

[`ShippingstatusResponseSignature`](../../doc/models/shippingstatus-response-signature.md)

## Example Usage

```python
barcode = '3SDEVC172649258'

result = track_trace_controller.returns_the_signature_of_a_particular_shipment(barcode)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "Signature": {
    "Barcode": "3SDEVC317858754",
    "SignatureDate": "2022-11-07T19:28:16",
    "SignatureImage": "iVBORw0KGgoAAAANSUhEUgAAAogAAAGTCAYAAACrs[TRUNCATED]"
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid request | [`ShippingstatusResponseErrorException`](../../doc/models/shippingstatus-response-error-exception.md) |
| 401 | Invalid apikey | [`ShippingstatusUnauthorizedException`](../../doc/models/shippingstatus-unauthorized-exception.md) |
| 405 | Method not allowed | [`ShippingstatusMethodNotAllowedException`](../../doc/models/shippingstatus-method-not-allowed-exception.md) |
| 429 | Too many requests | [`ShippingstatusTooManyRequestException`](../../doc/models/shippingstatus-too-many-request-exception.md) |
| 500 | Internal server error | [`ShippingstatusResponseErrorException`](../../doc/models/shippingstatus-response-error-exception.md) |


# Returns the Updated Statuses for a Particular Customer Number

Request example:

```
curl -X GET "https://api-sandbox.postnl.nl/shipment/v2/status/11223344/updatedshipments?period=2022-12-25T10:00:00&amp;period=2022-12-25T10:12:00" \
 -H "Accept: application/json" \
 -H "apikey: APIKEY-HERE" \
```

```python
def returns_the_updated_statuses_for_a_particular_customer_number(self,
                                                                 customernumber,
                                                                 period=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customernumber` | [`str`](../../doc/models/string-enum.md) | Template, Required | Your customer number |
| `period` | [`List[str]`](../../doc/models/string-enum.md) | Query, Optional | Optional array which defines a specific period in which to return updated shipments. For optimal results, schedule calls at a frequency between 5-15 minutes and align the requested period accordingly to ensure complete coverage of past updates. Shorter periods yield improved response times. The API accommodates a maximum requested period of 2 hours, granting access to shipment data up to 48 hours in the past. Please use the following format: YYYY-MM-DDTHH:MM:SS and repeat this variable to define the period (e.g. /updatedshipments?period=2022-11-07T12:00:00.000&period=2022-11-07T12:05:00.000).<br>**Constraints**: *Maximum Items*: `2` |

## Response Type

[`List[ShippingstatusResponseUpdatedShipment]`](../../doc/models/shippingstatus-response-updated-shipment.md)

## Example Usage

```python
customernumber = '11223344'

period = [
    '2022-11-07T12:00:00.000',
    '2022-11-07T12:05:00.000'
]

result = track_trace_controller.returns_the_updated_statuses_for_a_particular_customer_number(
    customernumber,
    period=period
)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "Barcode": "3SDEVC2260332157",
    "CreationDate": "2022-11-07T00:00:00",
    "CustomerNumber": "11223344",
    "CustomerCode": "DEVC",
    "Status": {
      "Timestamp": "2022-11-08T02:17:49",
      "StatusCode": "5",
      "StatusDescription": "Zending gesorteerd",
      "PhaseCode": "2",
      "PhaseDescription": "Sortering"
    }
  },
  {
    "Barcode": "3SDEVC775533088",
    "CreationDate": "2022-11-07T00:00:00",
    "CustomerNumber": "11223344",
    "CustomerCode": "DEVC",
    "Status": {
      "Timestamp": "2022-11-08T04:15:00",
      "StatusCode": "13",
      "StatusDescription": "Voorgemeld: nog niet aangenomen",
      "PhaseCode": "1",
      "PhaseDescription": "Collectie"
    }
  },
  {
    "Barcode": "3SDEVC563372025",
    "CreationDate": "2022-11-07T00:00:00",
    "CustomerNumber": "11223344",
    "CustomerCode": "DEVC",
    "Status": {
      "Timestamp": "2022-11-08T04:15:00",
      "StatusCode": "13",
      "StatusDescription": "Voorgemeld: nog niet aangenomen",
      "PhaseCode": "1",
      "PhaseDescription": "Collectie"
    }
  },
  {
    "Barcode": "3SDEVC336510881",
    "CreationDate": "2022-11-08T00:00:00",
    "CustomerNumber": "11223344",
    "CustomerCode": "DEVC",
    "Status": {
      "Timestamp": "2022-11-08T01:01:28",
      "StatusCode": "1",
      "StatusDescription": "Zending voorgemeld",
      "PhaseCode": "1",
      "PhaseDescription": "Collectie"
    }
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid request | [`ShippingstatusResponseErrorException`](../../doc/models/shippingstatus-response-error-exception.md) |
| 401 | Invalid apikey | [`ShippingstatusUnauthorizedException`](../../doc/models/shippingstatus-unauthorized-exception.md) |
| 405 | Method not allowed | [`ShippingstatusMethodNotAllowedException`](../../doc/models/shippingstatus-method-not-allowed-exception.md) |
| 429 | Too many requests | [`ShippingstatusTooManyRequestException`](../../doc/models/shippingstatus-too-many-request-exception.md) |
| 500 | Internal server error | [`ShippingstatusResponseErrorException`](../../doc/models/shippingstatus-response-error-exception.md) |

