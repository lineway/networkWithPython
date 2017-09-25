from pygeocoder import Geocoder

if __name__ == '__main__':
    address = '207N. Definance St, Archbold, OH'
    print(Geocoder.geocode(address)[0].coordinates)