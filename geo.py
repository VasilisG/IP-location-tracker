import urllib.request
import json

# Header declarations for output print.
hostTitle = "HOST DETAILS\n"
countryTitle = "COUNTRY DETAILS\n"

# Format printing constants.
dotNumber = 70
countryPadding = 50
detailsPadding = 40

'''
All available types of responses for IP along with their urls.
'''

ipValidTypes = ['plain', 'json', 'jsonp']
ipPlain = 'https://get.geojs.io/v1/ip'
ipJson = 'https://get.geojs.io/v1/ip.json'
ipLookup = {'plain' : ipPlain, 'json' : ipJson}

'''
All available types of responses for country along with their urls.
'''

countryValidTypes = ['plain', 'plainfull', 'json', 'jsonp']
countryPlain = 'https://get.geojs.io/v1/ip/country'
countryFullPlain = 'https://get.geojs.io/v1/ip/country/full'
countryJson = 'https://get.geojs.io/v1/ip/country/{ip address}.json'
countryLookup = {'plain' : countryPlain, 'plainfull' : countryFullPlain, 'json' : countryJson}

'''
All available types of responses for all geo data along with their urls.
'''
geoJson = 'https://get.geojs.io/v1/ip/geo/{ip address}.json'

'''
All available types of responses for DNS PTR records.
'''
ptrPlain = 'https://get.geojs.io/v1/dns/ptr'

# Gets the response of a url that returns plain text as response.
def getPlainResponse(url):
    return urllib.request.urlopen(url).read().decode().strip()

# Gets the response of a url that returns json as response and replaces the default argument '{ip address}' with the IP address whose country we're looking
def getJsonResponse(url, ipAddress):
    response = urllib.request.urlopen(url.replace('{ip address}',ipAddress)).read().decode()
    outDict = json.loads(response)
    return outDict

# Gets host's IP address, having default 'returnType' as 'plain', which can be changed accordingly.
def getIP(returnType = 'plain'):
    if isinstance(returnType,str):
        returnType = returnType.lower()
        if returnType in ipValidTypes:
            if returnType == 'plain':
                return getPlainResponse(ipLookup[returnType])
            else:
                return getJsonResponse(ipLookup[returnType],'')
        else:
            raise ValueError('\'returnType\' does not belong in valid types: ' + str(ipValidTypes))
    else:
        raise TypeError('\'returnType\' must be of type \'str\'(' + type(returnType).__name__ + ' was given).')

# Gets the country of a specific IP address.
def getCountry(ipAddress, returnType = 'plain'):
    if not isinstance(ipAddress,str):
        raise TypeError('\'ipAddress\' is not an instance of \'str\'('+ type(ipAddress).__name__ + ' was given).')
    if isinstance(returnType,str):
        returnType = returnType.lower()
        if returnType in countryValidTypes:
            if returnType == 'plain':
                return getPlainResponse(countryLookup[returnType] + '/' + ipAddress)
            elif returnType == 'plainfull':
                return getPlainResponse(countryLookup[returnType] + '/' + ipAddress)
            else:
                return getJsonResponse(countryLookup[returnType], ipAddress)
        else:
            raise ValueError('\'returnType\' does not belong in valid types: ' + str(countryValidTypes))
    else:
        raise TypeError('\'returnType\' must be of type \'str\'(' + type(returnType).__name__ + ' was given).')

# Gets all available geodata for a specific IP address.  
def getGeoData(ipAddress):
    if isinstance(ipAddress, str):
        return getJsonResponse(geoJson, ipAddress)
    else:
        raise TypeError("\'ipAddress\' is not an instance of list.")

# Gets the DNS PTR record of an IP address, if possible.
def getPTR(ipAddress):
    if not isinstance(ipAddress, str):
        raise TypeError("\'ipAddress\' is not an instance of list.")
    return getPlainResponse(ptrPlain)

# Gets all country information for an IP address.
def showCountryDetails(ip=''):
    result = ""
    if ip == '':
        ip = getIP('plain')
    countryData = getCountry(ip, 'json')
    result += '-' * dotNumber + '\n'
    result += (dotNumber//2 - len(countryTitle)//2) * ' ' + countryTitle
    result += '-' * dotNumber + '\n'
    for key, value in countryData.items():
        cleanKey = key.replace('_',' ').capitalize() + ':'
        cleanKey = cleanKey.ljust(countryPadding, ' ')
        result += cleanKey + str(value) + '\n'
    result += '-' * dotNumber + '\n'
    print(result)

# Get all available information provided for a specific IP address (country, location, region, etc.).
def showIpDetails(ip=''):
    result = ""
    if ip == '':
        ip = getIP('plain')
    country = getCountry(ip, 'plainFull')
    result += '-' * dotNumber + '\n'
    result += (dotNumber//2 - len(hostTitle)//2) * ' ' + hostTitle
    result += '-' * dotNumber + '\n'
    result += 'Country: '.ljust(countryPadding,' ') + country + '\n'
    geoData = getGeoData(ip)
    ptrData = getPTR(ip)
    for key, value in geoData.items():
        cleanKey = key.replace('_',' ').capitalize() + ':'
        cleanKey = cleanKey.ljust(countryPadding,' ')
        result += cleanKey + str(value) + '\n'
    result += '-' * dotNumber + '\n'
    print(result)
