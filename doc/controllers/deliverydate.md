# Deliverydate

### Summary

* Calculate expected delivery date based on shipping date or required shipping date based on requested delivery date.
* Input: Address, postalcode, shipping- or delivery date and delivery options.
* Output: Delivery date and Sent date.

Please note that you can use the all-in-one [Checkout API](#tag/Checkout) as well. This API combines he the functionality of the DeliveryDate, Location and Timeframe webservices. So it will be easier to implement the PostNL delivery options and there is less overhead in requesting the PostNL services by using this 3-in-1 API.

### Guidelines

At the <a href="https://developer.postnl.nl/" target="_blank" rel="noopener noreferrer">Developer Portal</a> you can find information about the use and functionality of the API. It is strongly recommended that you read this carefully before starting the implementation.

<button type="button">
  <a href="https://developer.postnl.nl/browse-apis/delivery-options/deliverydate-webservice/" target="_blank" rel="noopener noreferrer">Documentation</a>
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
      <td>v1_0</td>
      <td>Oct 07, 2013</td>
      <td>Not supported</td>
      <td/>
      <td/>
      <td/>
    </tr>
    <tr>
      <td>v1_1</td>
      <td>Jan 24, 2014</td>
      <td>Not supported</td>
      <td/>
      <td/>
      <td/>
    </tr>
    <tr>
      <td>v1_2</td>
      <td>Aug 14, 2014</td>
      <td>Not supported</td>
      <td/>
      <td/>
      <td/>
    </tr>
    <tr>
      <td>v2_0</td>
      <td>Aug 14, 2015</td>
      <td>Not supported</td>
      <td/>
      <td/>
      <td/>
    </tr>
    <tr>
      <td>v2_1</td>
      <td>Nov 03, 2015</td>
      <td>Supported</td>
      <td>See below</td>
      <td>Yes</td>
      <td>SOAP</td>
    </tr>
    <tr>
      <td>v2_2</td>
      <td>Aug 24, 2017</td>
      <td>Current version</td>
      <td>See below</td>
      <td>Yes</td>
      <td>REST and SOAP</td>
    </tr>
  </tbody>
</table>
### Release notes

#### v2.0

* CutOffTime and CutOffTimeForSundaySorting replaced by CutOffTimes list. In the previous version of the GetDeliveryDate method, cut off times were specified for weekdays and Sunday in two fields. It is now possible to specify cut off times for every day of the week in the new CutOffTimes field.*   Options field added. It is now possible to specify which delivery options should be considered when returning a delivery or sent date using the new Options field.*   New and updated address fields. Several address fields have been added to the GetDeliveryDate and GetSendDate elements to specify the delivery address more precisely. These fields are: Street, HouseNrExt, City and CountryCode.  
  Furthermore, the HouseNumber field has been renamed to HouseNr.

#### v2.1

* GetDeliveryDateResponse.Option is removed from the interface. The GetDeliveryDateResponse.Options is added to the interface.

#### v2.2

* Thee following fields have been added to the interface:  
  OriginCountryCode  
  CutoffTime.Available  
  New delivery option: MyTime (Delivery on demand)
  
  __NOTE: THIS PRODUCT NO LONGER EXIST__

* If applicable, sustainability scores are now returned for each option

```python
deliverydate_controller = client.deliverydate
```

## Class Name

`DeliverydateController`

## Methods

* [Calculate Expected Delivery Date](../../doc/controllers/deliverydate.md#calculate-expected-delivery-date)
* [Calculate Required Shipping Date](../../doc/controllers/deliverydate.md#calculate-required-shipping-date)


# Calculate Expected Delivery Date

Request example:

```
curl -X GET "https://api-sandbox.postnl.nl/shipment/v2_2/calculate/date/delivery?ShippingDate=29-05-2022+14%3A00%3A00&amp;ShippingDuration=1&amp;CutOffTime=17%3A00%3A00&amp;PostalCode=2132WT&amp;CountryCode=NL&amp;City=Hoofddorp&amp;Street=Siriusdreef&amp;HouseNumber=42&amp;HouseNrExt=A" \
 -H "Accept: application/json" \
 -H "apikey: APIKEY-HERE" 
```

```python
def calculate_expected_delivery_date(self,
                                    shipping_date,
                                    shipping_duration,
                                    cut_off_time,
                                    postal_code,
                                    country_code,
                                    options,
                                    origin_country_code='NL',
                                    city=None,
                                    street=None,
                                    house_number=None,
                                    house_nr_ext=None,
                                    cut_off_time_monday=None,
                                    available_monday=None,
                                    cut_off_time_tuesday=None,
                                    available_tuesday=None,
                                    cut_off_time_wednesday=None,
                                    available_wednesday=None,
                                    cut_off_time_thursday=None,
                                    available_thursday=None,
                                    cut_off_time_friday=None,
                                    available_friday=None,
                                    cut_off_time_saturday=None,
                                    available_saturday=None,
                                    cut_off_time_sunday=None,
                                    available_sunday=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `shipping_date` | [`str`](../../doc/models/string-enum.md) | Query, Required | Date/time of preparing the shipment for sending. Format: dd-MM-yyyy hh:mm:ss<br>**Constraints**: *Pattern*: `^[0-3]\d-[0-1]\d-[1-2]\d{3}\s[0-2]\d:[0-5]\d:[0-5]\d$` |
| `shipping_duration` | `int` | Query, Required | The duration it takes for the shipment to be delivered to PostNL in days. A value of 1 means that the parcel will be delivered to PostNL on the same day as the date specified in ShippingDate. A value of 2 means the parcel will arrive at PostNL a day later etc. |
| `cut_off_time` | [`str`](../../doc/models/string-enum.md) | Query, Required | Default cutoff time<br>**Constraints**: *Pattern*: `^[0-2]\d:[0-5]\d:[0-5]\d$` |
| `postal_code` | [`str`](../../doc/models/string-enum.md) | Query, Required | Zipcode of the destination address<br>**Constraints**: *Pattern*: `^[0-9]{4}([A-Z]{2})?$` |
| `country_code` | [`CountryCode1Enum`](../../doc/models/country-code-1-enum.md) | Query, Required | The ISO2 destination country code |
| `options` | [`List[Option3Enum]`](../../doc/models/option-3-enum.md) | Query, Required | The delivery options that you want to take into account when calculating the expected delivery date |
| `origin_country_code` | [`OriginCountryCodeEnum`](../../doc/models/origin-country-code-enum.md) | Query, Optional | The ISO2 origin country code<br>**Default**: `'NL'` |
| `city` | [`str`](../../doc/models/string-enum.md) | Query, Optional | City of the destination address |
| `street` | [`str`](../../doc/models/string-enum.md) | Query, Optional | The street name of the destination address. |
| `house_number` | `int` | Query, Optional | The house number of the destination address |
| `house_nr_ext` | [`str`](../../doc/models/string-enum.md) | Query, Optional | House number extension of the delivery address |
| `cut_off_time_monday` | [`str`](../../doc/models/string-enum.md) | Query, Optional | Overrides default cutoff time specified in the CutOffTime parameter for mondays specifically<br>**Constraints**: *Pattern*: `^[0-2]\d:[0-5]\d:[0-5]\d$` |
| `available_monday` | `bool` | Query, Optional | Specifies if you are available to ship to PostNL on mondays |
| `cut_off_time_tuesday` | [`str`](../../doc/models/string-enum.md) | Query, Optional | Overrides default cutoff time specified in the CutOffTime parameter for tuesdays specifically<br>**Constraints**: *Pattern*: `^[0-2]\d:[0-5]\d:[0-5]\d$` |
| `available_tuesday` | `bool` | Query, Optional | Specifies if you are available to ship to PostNL on tuesdays |
| `cut_off_time_wednesday` | [`str`](../../doc/models/string-enum.md) | Query, Optional | Overrides default cutoff time specified in the CutOffTime parameter for wednesdays specifically<br>**Constraints**: *Pattern*: `^[0-2]\d:[0-5]\d:[0-5]\d$` |
| `available_wednesday` | `bool` | Query, Optional | Specifies if you are available to ship to PostNL on wednesdays |
| `cut_off_time_thursday` | [`str`](../../doc/models/string-enum.md) | Query, Optional | Overrides default cutoff time specified in the CutOffTime parameter for thursdays specifically<br>**Constraints**: *Pattern*: `^[0-2]\d:[0-5]\d:[0-5]\d$` |
| `available_thursday` | `bool` | Query, Optional | Specifies if you are available to ship to PostNL on thursdays |
| `cut_off_time_friday` | [`str`](../../doc/models/string-enum.md) | Query, Optional | Overrides default cutoff time specified in the CutOffTime parameter for fridays specifically<br>**Constraints**: *Pattern*: `^[0-2]\d:[0-5]\d:[0-5]\d$` |
| `available_friday` | `bool` | Query, Optional | Specifies if you are available to ship to PostNL on fridays |
| `cut_off_time_saturday` | [`str`](../../doc/models/string-enum.md) | Query, Optional | Overrides default cutoff time specified in the CutOffTime parameter for saturdays specifically<br>**Constraints**: *Pattern*: `^[0-2]\d:[0-5]\d:[0-5]\d$` |
| `available_saturday` | `bool` | Query, Optional | Specifies if you are available to ship to PostNL on saturdays |
| `cut_off_time_sunday` | [`str`](../../doc/models/string-enum.md) | Query, Optional | Overrides default cutoff time specified in the CutOffTime parameter for sundays specifically<br>**Constraints**: *Pattern*: `^[0-2]\d:[0-5]\d:[0-5]\d$` |
| `available_sunday` | `bool` | Query, Optional | Specifies if you are available to ship to PostNL on sundays |

## Response Type

[`ShipmentV22CalculateDateDeliveryResponse`](../../doc/models/shipment-v22-calculate-date-delivery-response.md)

## Example Usage

```python
shipping_date = '29-05-2022 14:00:00'

shipping_duration = 1

cut_off_time = '17:00:00'

postal_code = '2132WT'

country_code = CountryCode1Enum.NL

options = [
    Option3Enum.SUNDAY,
    Option3Enum.TODAY,
    Option3Enum.AFTERNOON
]

origin_country_code = OriginCountryCodeEnum.NL

city = 'Hoofddorp'

street = 'Siriusdreef'

house_number = 42

house_nr_ext = 'A'

result = deliverydate_controller.calculate_expected_delivery_date(
    shipping_date,
    shipping_duration,
    cut_off_time,
    postal_code,
    country_code,
    options,
    origin_country_code=origin_country_code,
    city=city,
    street=street,
    house_number=house_number,
    house_nr_ext=house_nr_ext
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`DeliverydateResponseInvalidException`](../../doc/models/deliverydate-response-invalid-exception.md) |
| 401 | Invalid apikey | [`PostCIFDeliveryDateUnauthorizedException`](../../doc/models/post-cif-delivery-date-unauthorized-exception.md) |
| 405 | Method not allowed | [`PostCIFDeliveryDateMethodNotAllowedException`](../../doc/models/post-cif-delivery-date-method-not-allowed-exception.md) |
| 429 | Too many requests | [`PostCIFDeliveryDateTooManyRequestException`](../../doc/models/post-cif-delivery-date-too-many-request-exception.md) |
| 500 | Internal server error | [`DeliverydateResponseErrorException`](../../doc/models/deliverydate-response-error-exception.md) |


# Calculate Required Shipping Date

Request example:

```
curl -X GET "https://api-sandbox.postnl.nl/shipment/v2_2/calculate/date/shipping?DeliveryDate=30-05-2022&amp;ShippingDuration=1&amp;PostalCode=2132WT&amp;CountryCode=NL&amp;City=Hoofddorp&amp;Street=Siriusdreef&amp;HouseNumber=42&amp;HouseNrExt=A" \
 -H "Accept: application/json" \
 -H "apikey: APIKEY-HERE" \

```

```python
def calculate_required_shipping_date(self,
                                    delivery_date,
                                    shipping_duration,
                                    postal_code,
                                    country_code,
                                    origin_country_code='NL',
                                    city=None,
                                    street=None,
                                    house_number=None,
                                    house_nr_ext=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `delivery_date` | [`str`](../../doc/models/string-enum.md) | Query, Required | Date of the expected delivery (to the final destination) of the shipment.<br>**Constraints**: *Pattern*: `^[0-3]\d-[0-1]\d-[1-2]\d{3}$` |
| `shipping_duration` | `int` | Query, Required | The duration it takes for the shipment to be delivered to PostNL in days. A value of 1 means that the parcel will be delivered to PostNL on the same day as the date specified in ShippingDate. A value of 2 means the parcel will arrive at PostNL a day later etc. |
| `postal_code` | [`str`](../../doc/models/string-enum.md) | Query, Required | Zipcode of the address<br>**Constraints**: *Pattern*: `^[0-9]{4}([A-Z]{2})?$` |
| `country_code` | [`CountryCode1Enum`](../../doc/models/country-code-1-enum.md) | Query, Required | The ISO2 destination country code |
| `origin_country_code` | [`OriginCountryCodeEnum`](../../doc/models/origin-country-code-enum.md) | Query, Optional | The ISO2 country code of the origin country<br>**Default**: `'NL'` |
| `city` | [`str`](../../doc/models/string-enum.md) | Query, Optional | City of the destination address |
| `street` | [`str`](../../doc/models/string-enum.md) | Query, Optional | The street name of the destination address |
| `house_number` | `int` | Query, Optional | The house number of the destination address |
| `house_nr_ext` | [`str`](../../doc/models/string-enum.md) | Query, Optional | House number extension of the destination address |

## Response Type

[`ShipmentV22CalculateDateShippingResponse`](../../doc/models/shipment-v22-calculate-date-shipping-response.md)

## Example Usage

```python
delivery_date = '30-05-2022'

shipping_duration = 1

postal_code = '2132WT'

country_code = CountryCode1Enum.NL

origin_country_code = OriginCountryCodeEnum.NL

city = 'Hoofddorp'

street = 'Siriusdreef'

house_number = 42

house_nr_ext = 'A'

result = deliverydate_controller.calculate_required_shipping_date(
    delivery_date,
    shipping_duration,
    postal_code,
    country_code,
    origin_country_code=origin_country_code,
    city=city,
    street=street,
    house_number=house_number,
    house_nr_ext=house_nr_ext
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`DeliverydateResponseInvalidException`](../../doc/models/deliverydate-response-invalid-exception.md) |
| 401 | Invalid apikey | [`PostCIFDeliveryDateUnauthorizedException`](../../doc/models/post-cif-delivery-date-unauthorized-exception.md) |
| 405 | Method not allowed | [`PostCIFDeliveryDateMethodNotAllowedException`](../../doc/models/post-cif-delivery-date-method-not-allowed-exception.md) |
| 429 | Too many requests | [`PostCIFDeliveryDateTooManyRequestException`](../../doc/models/post-cif-delivery-date-too-many-request-exception.md) |
| 500 | Internal server error | [`DeliverydateResponseErrorException`](../../doc/models/deliverydate-response-error-exception.md) |

