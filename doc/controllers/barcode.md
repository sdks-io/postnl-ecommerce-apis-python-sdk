# Barcode

### Summary

* Reason to Call: Generate a barcode for your parcels.
* Input: Customer code and customer number and some specifications of the required barcode.
* Output: An unique identifier to use for creating shipments and to track and trace the status of the parcels.

Please note that you can use the all-in-one [Shipping API](#tag/Shipment) as well. This API combines the functionality of the Barcode, Labelling, Confirmation and Easy Return API. With this API you generate unique barcodes at the same time you create a label and so cutting down the number of API requests.

### Guidelines

At the <a href="https://developer.postnl.nl/" target="_blank" rel="noopener noreferrer">Developer Portal</a> you can find information about the use and functionality of the API. It is strongly recommended that you read this carefully before starting the implementation.

<button type="button">
  <a href="https://developer.postnl.nl/browse-apis/send-and-track/barcode-webservice/" target="_blank" rel="noopener noreferrer">Documentation</a>
</button>
### Versioning

<table>
  <tbody>
    <tr>
      <th>API</th>
      <th>Release date</th>
      <th>Status</th>
      <th>Release notes</th>
      <th>Schema changes</th>
      <th>Available as</th>
    </tr>
    <tr>
      <td>1_0</td>
      <td>Oct 01, 2012</td>
      <td>Not supported</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>1_1</td>
      <td>Oct 28, 2014</td>
      <td>Current version</td>
      <td>Different namespaces</td>
      <td>Yes</td>
      <td>REST and SOAP</td>
    </tr>
  </tbody>
</table>


```python
barcode_controller = client.barcode
```

## Class Name

`BarcodeController`


# Generate a Unique Barcode

Request example:

```
curl -X GET "https://api-sandbox.postnl.nl/shipment/v1_1/barcode?CustomerCode=DEVC&amp;CustomerNumber=11223344&amp;Type=3S&amp;Serie=000000000-999999999&amp;Range=NL" \
 -H "Accept: application/json" \
 -H "apikey: APIKEY-HERE" 
```

```python
def generate_a_unique_barcode(self,
                             customer_code,
                             customer_number,
                             mtype,
                             serie=None,
                             range=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_code` | [`str`](../../doc/models/string-enum.md) | Query, Required | The customer code for which you want a barcode to be generated |
| `customer_number` | [`str`](../../doc/models/string-enum.md) | Query, Required | The customer code for which you want a barcode to be generated |
| `mtype` | [`Type1Enum`](../../doc/models/type-1-enum.md) | Query, Required | The barcode type that you want to be generated |
| `serie` | [`str`](../../doc/models/string-enum.md) | Query, Optional | Barcode serie in the format '###000000-###000000', for example 100000-20000. The range must consist of a minimal difference of 100.000. It is allowed to add extra leading zeros at the beginning of the serie. See [Guidelines](https://developer.postnl.nl/browse-apis/send-and-track/barcode-webservice/) for more information.<br>**Constraints**: *Minimum Length*: `6`, *Maximum Length*: `9` |
| `range` | [`str`](../../doc/models/string-enum.md) | Query, Optional | Only used for International Mail and Packet products (PEPS) shipments (with type LA, RI, UE). Identifying the issuing postal administration's country (NL in this case). |

## Response Type

[`BarcodeResponse`](../../doc/models/barcode-response.md)

## Example Usage

```python
customer_code = 'DEVC'

customer_number = '11223344'

mtype = Type1Enum.ENUM_3S

range = 'NL'

result = barcode_controller.generate_a_unique_barcode(
    customer_code,
    customer_number,
    mtype,
    range=range
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid request | [`BarcodeResponseInvalidException`](../../doc/models/barcode-response-invalid-exception.md) |
| 401 | Unauthorized | [`BarcodeResponseErrorException`](../../doc/models/barcode-response-error-exception.md) |
| 405 | Method not allowed | [`BarcodeMethodNotAllowedException`](../../doc/models/barcode-method-not-allowed-exception.md) |
| 429 | Too many requests | [`BarcodeTooManyRequestException`](../../doc/models/barcode-too-many-request-exception.md) |
| 500 | Internal server error | [`BarcodeResponseErrorException`](../../doc/models/barcode-response-error-exception.md) |

