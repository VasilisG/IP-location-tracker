import geo

ip = geo.getIP()
print(ip)

country = geo.getCountry(ip, 'plain')
print(country)

country = geo.getCountry(ip, 'json')
print(country)

geoData = geo.getGeoData(ip)
print(geoData)

ptrData = geo.getPTR(ip)
print(ptrData)

geo.showIpDetails('216.239.32.0')

geo.showCountryDetails('216.239.32.0')