# IP-location-tracker

This is an IP location tracker made in Python 3.6, using the [urllib.request](https://docs.python.org/3/library/urllib.request.html)
 module and the [GeoJs](https://www.geojs.io/) API to get geolocation data.
 
 ## Usage
 
 `geo` is pretty simple to use and can provide with all the necessary details about an IP address such as:
 - Country (both abbreviation and full name).
 - Region (the area within a country in which the IP address is located).
 - City.
 - Timezone.
 - Latitude.
 - Longitude.
 - Organization name.
 
Below there are some examples that demonstrate `geo`'s usage:

__Getting IP address of host:__
```
import geo

ip = geo.getIP()
```
__Getting country origin of IP address:__

(The address below is one of the IP address range that Google uses.)


This will return plain text by default, as we haven't set the second argument.

```
country = geo.getCountry('216.239.32.0')
```
Result:
```
US
```
This will return the country's full name.
```
country = geo.getCountry('216.239.32.0', 'plainfull')
```
Result: 
```
United States
```
This will return a json response which will contains all formats of country's name and the responding IP address.
```
country = geo.getCountry('216.239.32.0', 'json')
```
Result: 
```
{'country': 'US', 'country_3': 'USA', 'ip': '216.239.32.0', 'name': 'United States'}
```

__Getting geolocation data of IP address:__
```
geoData = geo.getGeoData('216.239.32.0')
```
Returns:
```
{'organization_name': 'Google LLC', 'region': 'California', 'accuracy': 1000, 'asn': 15169, 'organization': 'AS15169 Google LLC', 'timezone': 'America/Los_Angeles', 'longitude': '-122.2971', 'country_code3': 'USA', 'area_code': '0', 'ip': '216.239.32.0', 'city': 'San Mateo', 'country': 'United States', 'continent_code': 'NA', 'country_code': 'US', 'latitude': '37.5428'}
```

__Getting a summary of all information about an IP address:__
```
geo.showIpDetails('216.239.32.0')
```
The output will be:
```
----------------------------------------------------------------------
                             HOST DETAILS
----------------------------------------------------------------------
Country:                                          United States
Organization name:                                Google LLC
Region:                                           California
Accuracy:                                         1000
Asn:                                              15169
Organization:                                     AS15169 Google LLC
Timezone:                                         America/Los_Angeles
Longitude:                                        -122.2971
Country code3:                                    USA
Area code:                                        0
Ip:                                               216.239.32.0
City:                                             San Mateo
Country:                                          United States
Continent code:                                   NA
Country code:                                     US
Latitude:                                         37.5428
----------------------------------------------------------------------
```
__Getting country details for an IP address:__
```
geo.showCountryDetails('216.239.32.0')
```
This will return:
```
----------------------------------------------------------------------
                           COUNTRY DETAILS
----------------------------------------------------------------------
Country:                                          US
Country 3:                                        USA
Ip:                                               216.239.32.0
Name:                                             United States
----------------------------------------------------------------------
```





