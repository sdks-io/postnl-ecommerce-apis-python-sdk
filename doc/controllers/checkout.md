# Checkout

### Summary

* Reason to Call: Receive information regarding delivery options.
* Input: Details of dates, address of the customer, order date and delivery options.
* Output: Timeframes and pickup locations.

Combines the functionality of the DeliveryDate, Timeframe and Location API.

### Guidelines

At the <a href="https://developer.postnl.nl/" target="_blank" rel="noopener noreferrer">Developer Portal</a> you can find information about the use and functionality of the API. It is strongly recommended that you read this carefully before starting the implementation.

<button type="button">
  <a href="https://developer.postnl.nl/browse-apis/checkout/checkout-api/" target="_blank" rel="noopener noreferrer">Documentation</a>
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
      <td>v1</td>
      <td>July 05, 2019</td>
      <td>Current version</td>
      <td>First version</td>
      <td>-</td>
      <td>REST</td>
    </tr>
  </tbody>
</table>


```python
checkout_controller = client.checkout
```

## Class Name

`CheckoutController`


# Checkout

Checkout

```python
def checkout(self,
            body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CheckoutRequest`](../../doc/models/checkout-request.md) | Body, Required | - |

## Response Type

[`CheckoutResponse`](../../doc/models/checkout-response.md)

## Example Usage

```python
body = CheckoutRequest(
    order_date='24-02-2021 12:00:00',
    cut_off_times=[
        CutOffTime(
            day=DayEnum.ENUM_00,
            available=True,
            mtype=TypeEnum.REGULAR,
            time='20:00:00'
        ),
        CutOffTime(
            day=DayEnum.ENUM_00,
            available=True,
            mtype=TypeEnum.TODAY,
            time='12:00:00'
        )
    ],
    options=[
        OptionEnum.DAYTIME,
        OptionEnum.EVENING,
        OptionEnum.TODAY,
        OptionEnum.SUNDAY,
        OptionEnum.PICKUP
    ],
    locations=2,
    days=3,
    addresses=[
        Address(
            address_type=AddressTypeEnum.ENUM_01,
            house_nr=74,
            zipcode='3571ZZ',
            countrycode=CountrycodeEnum.NL,
            street='Molengraaffplantsoen',
            city='Utrecht'
        )
    ],
    shipping_duration=1,
    holiday_sorting=True
)

result = checkout_controller.checkout(body)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid request | [`CheckoutResponseInvalidException`](../../doc/models/checkout-response-invalid-exception.md) |
| 401 | Invalid apikey | [`PostCIFCheckoutServiceUnauthorizedException`](../../doc/models/post-cif-checkout-service-unauthorized-exception.md) |
| 405 | Method not allowed | [`PostCIFCheckoutServiceMethodNotAllowedException`](../../doc/models/post-cif-checkout-service-method-not-allowed-exception.md) |
| 429 | Too many requests | [`PostCIFCheckoutServiceTooManyRequestException`](../../doc/models/post-cif-checkout-service-too-many-request-exception.md) |
| 500 | Internal server error | [`CheckoutResponseErrorException`](../../doc/models/checkout-response-error-exception.md) |

