# Locations

### Summary

* Reason to Call: Retrieve a list of pick up points that support the option for direct delivery to a standard pick up point.
* Input: Address, city and country code of the preferred location Or longitude and latitude.
* Output: Locations nearest to the supplied address, location within the supplied area or location information of the location code.

Please note that you can use the all-in-one [Checkout API](#tag/Checkout) as well. This API combines he the functionality of the DeliveryDate, Location and Timeframe webservices. So it will be easier to implement the PostNL delivery options and there is less overhead in requesting the PostNL services by using this 3-in-1 API.

### Guidelines

At the <a href="https://developer.postnl.nl/" target="_blank" rel="noopener noreferrer">Developer Portal</a> you can find information about the use and functionality of the API. It is strongly recommended that you read this carefully before starting the implementation.

<button type="button">
  <a href="https://developer.postnl.nl/browse-apis/delivery-options/location-webservice/" target="_blank" rel="noopener noreferrer">Documentation</a>
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
      <td>Jul 22, 2013</td>
      <td>Not supported</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>v1_1</td>
      <td>Aug 21, 2014</td>
      <td>Supported</td>
      <td>See below</td>
      <td>Yes</td>
      <td>SOAP</td>
    </tr>
    <tr>
      <td>v2_0</td>
      <td>Aug 14, 2015</td>
      <td>Not supported</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>v2_1</td>
      <td>May 10, 2016</td>
      <td>Supported</td>
      <td>See below</td>
      <td>Yes</td>
      <td>REST and SOAP</td>
    </tr>
  </tbody>
</table>
### Release notes

#### v1.1

* The operation GetNearestLocations has been updated with new request properties:
  * Countrycode [M] has been added for international locations
  * Location.City [O] has been added for better international matching
  * Location.HouseNr [O] has been added for better international matching
  * Location.HouseNrExt [O] has been added for better international matching
  * Location.Street [O] has been added for better international matching
* The operation GetLocationsInArea has been updated with new request properties:
  * Countrycode [M] has been added for international locations
  * The operation GetBLSLocation has been removed
  * The operation GetLocation has been added
  * The Location Type has been extended with international address properties.

#### v2.1

* The Location Type has been extended with PartnerLocationCodes (ResponseLocationCode).
* If applicable, sustainability scores are now returned for each option

```python
locations_controller = client.locations
```

## Class Name

`LocationsController`

## Methods

* [Returns Pickup Locations Nearest to the Provided Address](../../doc/controllers/locations.md#returns-pickup-locations-nearest-to-the-provided-address)
* [Returns Pickup Locations Nearest to the Provided Coordinates](../../doc/controllers/locations.md#returns-pickup-locations-nearest-to-the-provided-coordinates)
* [Returns Pickup Locations Within a Provided Area](../../doc/controllers/locations.md#returns-pickup-locations-within-a-provided-area)
* [Returns a Specific Pickup Location](../../doc/controllers/locations.md#returns-a-specific-pickup-location)


# Returns Pickup Locations Nearest to the Provided Address

Request example:

```
curl -X GET "https://api-sandbox.postnl.nl/shipment/v2_1/locations/nearest?CountryCode=NL&PostalCode=2132WT&City=Hoofddorp&Street=Siriusdreef&HouseNumber=42&HouseNumberExtension=-60&DeliveryDate=24-12-2022&OpeningTime=09%3A00%3A00" \
 -H "Accept: application/json" \
 -H "apikey: APIKEY-HERE" \
```

```python
def returns_pickup_locations_nearest_to_the_provided_address(self,
                                                            country_code,
                                                            postal_code,
                                                            city=None,
                                                            street=None,
                                                            house_number=None,
                                                            house_number_extension=None,
                                                            delivery_date=None,
                                                            opening_time=None,
                                                            delivery_options=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `country_code` | [`CountryCode1Enum`](../../doc/models/country-code-1-enum.md) | Query, Required | The country of the recipient's address |
| `postal_code` | [`str`](../../doc/models/string-enum.md) | Query, Required | The zipcode of the recipient's address<br>**Constraints**: *Pattern*: `^[0-9]{4}([A-Z]{2})?$` |
| `city` | [`str`](../../doc/models/string-enum.md) | Query, Optional | The city of the recipient's address |
| `street` | [`str`](../../doc/models/string-enum.md) | Query, Optional | The street name of the recipient's address |
| `house_number` | `int` | Query, Optional | The house number of the recipient's address |
| `house_number_extension` | [`str`](../../doc/models/string-enum.md) | Query, Optional | The house number extension of the recipient's address |
| `delivery_date` | [`str`](../../doc/models/string-enum.md) | Query, Optional | The date of the earliest delivery date at the pickup location. Format:  dd-MM-yyyy. Note: this date cannot be in the past, otherwise an error is returned. If not provided, the present day is used as a default<br>**Constraints**: *Pattern*: `^[0-3]\d-[0-1]\d-[1-2]\d{3}$` |
| `opening_time` | [`str`](../../doc/models/string-enum.md) | Query, Optional | Opening time filter. Format: hh:mm:ss. This field will be used to filter out locations that are closed at the time provided. If no opening time is provided all locations will be returned regardless of their opening times.<br>**Constraints**: *Pattern*: `^[0-2]\d:[0-5]\d:[0-5]\d$` |
| `delivery_options` | [`List[DeliveryOption1Enum]`](../../doc/models/delivery-option-1-enum.md) | Query, Optional | The pickup location types for which locations should be filtered. By default all location types are returned (PG = Retail points and parcel lockers). This can be used to filter on only parcel lockers (PA) or specifically exclude parcel lockers from the response (PG_EX). |

## Response Type

[`LocationsResponse`](../../doc/models/locations-response.md)

## Example Usage

```python
country_code = CountryCode1Enum.NL

postal_code = '2132WT'

city = 'Hoofddorp'

street = 'Siriusdreef'

house_number = 42

house_number_extension = '-60'

delivery_date = '24-12-2022'

opening_time = '09:00:00'

result = locations_controller.returns_pickup_locations_nearest_to_the_provided_address(
    country_code,
    postal_code,
    city=city,
    street=street,
    house_number=house_number,
    house_number_extension=house_number_extension,
    delivery_date=delivery_date,
    opening_time=opening_time
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid request | [`LocationsResponseInvalidException`](../../doc/models/locations-response-invalid-exception.md) |
| 401 | Unauthorized | [`PostCIFLocationUnauthorizedException`](../../doc/models/post-cif-location-unauthorized-exception.md) |
| 405 | Method not allowed | [`PostCIFLocationMethodNotAllowedException`](../../doc/models/post-cif-location-method-not-allowed-exception.md) |
| 429 | Too many requests | [`PostCIFLocationTooManyRequestException`](../../doc/models/post-cif-location-too-many-request-exception.md) |
| 500 | Internal server error | [`LocationsResponseErrorException`](../../doc/models/locations-response-error-exception.md) |


# Returns Pickup Locations Nearest to the Provided Coordinates

Request example:

```
curl -X GET "https://api-sandbox.postnl.nl/shipment/v2_1/locations/nearest/geocode?Latitude=52.2864669620795&Longitude=4.68239055845954&CountryCode=NL&DeliveryDate=24-12-2022&OpeningTime=09%3A00%3A00" \
 -H "Accept: application/json" \
 -H "apikey: APIKEY-HERE" \
```

```python
def returns_pickup_locations_nearest_to_the_provided_coordinates(self,
                                                                latitude,
                                                                longitude,
                                                                country_code,
                                                                delivery_date=None,
                                                                opening_time=None,
                                                                delivery_options=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `latitude` | `float` | Query, Required | The latitude of the location |
| `longitude` | `float` | Query, Required | The longitude of the location |
| `country_code` | [`CountryCode1Enum`](../../doc/models/country-code-1-enum.md) | Query, Required | The coutry for which the coordinates are provided |
| `delivery_date` | [`str`](../../doc/models/string-enum.md) | Query, Optional | The date of the earliest delivery date. Format:  dd-MM-yyyy. Note: this date cannot be in the past, otherwise an error is returned.<br>**Constraints**: *Pattern*: `^[0-3]\d-[0-1]\d-[1-2]\d{3}$` |
| `opening_time` | [`str`](../../doc/models/string-enum.md) | Query, Optional | Opening time filter. Format: hh:mm:ss. This field will be used to filter out locations that are closed at the time provided.<br>**Constraints**: *Pattern*: `^[0-2]\d:[0-5]\d:[0-5]\d$` |
| `delivery_options` | [`List[DeliveryOptions1Enum]`](../../doc/models/delivery-options-1-enum.md) | Query, Optional | The pickup location types for which locations should be filtered. By default all location types are returned (PG = Retail points and parcel lockers). This can be used to filter on only parcel lockers (PA) or specifically exclude parcel lockers from the response (PG_EX). |

## Response Type

[`LocationsResponse`](../../doc/models/locations-response.md)

## Example Usage

```python
latitude = 52.2864669620795

longitude = 4.68239055845954

country_code = CountryCode1Enum.NL

delivery_date = '24-12-2022'

opening_time = '09:00:00'

result = locations_controller.returns_pickup_locations_nearest_to_the_provided_coordinates(
    latitude,
    longitude,
    country_code,
    delivery_date=delivery_date,
    opening_time=opening_time
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid request | [`LocationsResponseInvalidException`](../../doc/models/locations-response-invalid-exception.md) |
| 401 | Unauthorized | [`PostCIFLocationUnauthorizedException`](../../doc/models/post-cif-location-unauthorized-exception.md) |
| 405 | Method not allowed | [`PostCIFLocationMethodNotAllowedException`](../../doc/models/post-cif-location-method-not-allowed-exception.md) |
| 429 | Too many requests | [`PostCIFLocationTooManyRequestException`](../../doc/models/post-cif-location-too-many-request-exception.md) |
| 500 | Internal server error | [`LocationsResponseErrorException`](../../doc/models/locations-response-error-exception.md) |


# Returns Pickup Locations Within a Provided Area

Request example:

```
curl -X GET "https://api-sandbox.postnl.nl/shipment/v2_1/locations/area?LatitudeNorth=52.156439&LongitudeWest=5.015643&LatitudeSouth=52.017473&LongitudeEast=5.065254&CountryCode=NL&DeliveryDate=24-12-2023&OpeningTime=09%3A00%3A00" \
 -H "Accept: application/json" \
 -H "apikey: APIKEY-HERE" \
```

```python
def returns_pickup_locations_within_a_provided_area(self,
                                                   latitude_north,
                                                   longitude_west,
                                                   latitude_south,
                                                   longitude_east,
                                                   country_code,
                                                   delivery_date=None,
                                                   opening_time=None,
                                                   delivery_options=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `latitude_north` | `float` | Query, Required | The northmost coordinates of the area |
| `longitude_west` | `float` | Query, Required | The westmost coordinates of the area |
| `latitude_south` | `float` | Query, Required | The southmost coordinates of the area |
| `longitude_east` | `float` | Query, Required | The eastmost coordinates of the area |
| `country_code` | [`CountryCode1Enum`](../../doc/models/country-code-1-enum.md) | Query, Required | - |
| `delivery_date` | [`str`](../../doc/models/string-enum.md) | Query, Optional | The date of the earliest delivery date. Format:  dd-MM-yyyy. Note: this date cannot be in the past, otherwise an error is returned.<br>**Constraints**: *Pattern*: `^[0-3]\d-[0-1]\d-[1-2]\d{3}$` |
| `opening_time` | [`str`](../../doc/models/string-enum.md) | Query, Optional | Opening time filter. Format: hh:mm:ss. This field will be used to filter out locations that are closed at the time provided.<br>**Constraints**: *Pattern*: `^[0-2]\d:[0-5]\d:[0-5]\d$` |
| `delivery_options` | [`List[DeliveryOptions1Enum]`](../../doc/models/delivery-options-1-enum.md) | Query, Optional | The pickup location types for which locations should be filtered. By default all location types are returned (PG = Retail points and parcel lockers). This can be used to filter on only parcel lockers (PA) or specifically exclude parcel lockers from the response (PG_EX). |

## Response Type

[`LocationsResponse`](../../doc/models/locations-response.md)

## Example Usage

```python
latitude_north = 52.156439

longitude_west = 5.015643

latitude_south = 52.017473

longitude_east = 5.065254

country_code = CountryCode1Enum.NL

delivery_date = '24-12-2023'

opening_time = '09:00:00'

result = locations_controller.returns_pickup_locations_within_a_provided_area(
    latitude_north,
    longitude_west,
    latitude_south,
    longitude_east,
    country_code,
    delivery_date=delivery_date,
    opening_time=opening_time
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid request | [`LocationsResponseInvalidException`](../../doc/models/locations-response-invalid-exception.md) |
| 401 | Unauthorized | [`PostCIFLocationUnauthorizedException`](../../doc/models/post-cif-location-unauthorized-exception.md) |
| 405 | Method not allowed | [`PostCIFLocationMethodNotAllowedException`](../../doc/models/post-cif-location-method-not-allowed-exception.md) |
| 429 | Too many requests | [`PostCIFLocationTooManyRequestException`](../../doc/models/post-cif-location-too-many-request-exception.md) |
| 500 | Internal server error | [`LocationsResponseErrorException`](../../doc/models/locations-response-error-exception.md) |


# Returns a Specific Pickup Location

Request example:

```
curl -X GET "https://api-sandbox.postnl.nl/shipment/v2_1/locations/lookup?LocationCode=216877" \
 -H "Accept: application/json" \
 -H "apikey: APIKEY-HERE" 
```

```python
def returns_a_specific_pickup_location(self,
                                      location_code)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `location_code` | [`str`](../../doc/models/string-enum.md) | Query, Required | LocationCode information |

## Response Type

[`LocationResponse`](../../doc/models/location-response.md)

## Example Usage

```python
location_code = '216877'

result = locations_controller.returns_a_specific_pickup_location(location_code)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid request | [`LocationsResponseInvalidException`](../../doc/models/locations-response-invalid-exception.md) |
| 401 | Unauthorized | [`PostCIFLocationUnauthorizedException`](../../doc/models/post-cif-location-unauthorized-exception.md) |
| 405 | Method not allowed | [`PostCIFLocationMethodNotAllowedException`](../../doc/models/post-cif-location-method-not-allowed-exception.md) |
| 429 | Too many requests | [`PostCIFLocationTooManyRequestException`](../../doc/models/post-cif-location-too-many-request-exception.md) |
| 500 | Invalid request | [`LocationsResponseErrorException`](../../doc/models/locations-response-error-exception.md) |

