# import socket
#
# def get_ip_by_hostname():
#     hostname = input("Please enter a website address(URL): ")
#
#     try:
#        return f'Hostname: {hostname}\nIP address: {socket.gethostbyname(hostname)}'
#     except socket.gaierror as error:
#         return f'Invalid hostname - {error}'
#
# def main():
#     print(get_ip_by_hostname())
#
# if __name__ == "__main__":
#     main()
# 45.10.55.152


#         area = folium.Map(location=[response.get('lat'), response.get('lon')])
# folium.Marker([response.get('lat'), response.get('lon')]).add_to(area)
# area.save(f'{response.get("query")}_{response.get("city")}.html')

import requests
from pyfiglet import Figlet
import folium


def get_info_ip(ip='127.0.0.0'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()

        data = {
            '[IP]': response.get("query"),
            '[ISP]': response.get("isp"),
            '[COUNTRY]': response.get("country"),
            '[CITY]': response.get("city"),
            '[ORG]': response.get("org"),
            '[LAT]': response.get("lat"),
            '[LON]': response.get("lon"),
        }

        area = folium.Map(location=[response.get("lat"),response.get("lon")])
        folium.Marker([response.get('lat'), response.get('lon')]).add_to(area)
        area.save(f'{response.get("query")}_{response.get("country")}.html')

        for k, v in data.items():
            print(f'{k}:{v}')
    except ConnectionError:
        print("[!] Please check your connection")


def main():
    preview_text = Figlet(font='slant')
    print(preview_text.renderText('IP INFO'))
    ip = input("Type IP address: ")
    get_info_ip(ip=ip)


if __name__ == '__main__':
    main()
