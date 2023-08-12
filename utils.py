import requests

def get_user_points_level(n: int) -> list[int]:
    return [n//10, 10-n%10]

def get_user_appeals_level(n: int) -> list[int]:
    return [n//5, 5-n%5]

def get_user_cleaning_days_level(n: int) -> list[int]:
    return [n//5, 5-n%5]

def get_user_swaps(n: int) -> list[int]:
    return [n//5, 5-n%5]

# def parse_organization(coordinate: str) -> str|None:
#     x, y = coordinate.split(', ')
#     headers = {
#         'Connection': 'keep-alive',
#         'Cache-Control': 'max-age=0',
#         'Upgrade-Insecure-Requests': '1',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 OPR/40.0.2308.81',
#         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#         'DNT': '1',
#         'Accept-Encoding': 'gzip, deflate, lzma, sdch',
#         'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4'
#     }
#     url = f'https://egrp365.org/map/?x={x}&y={y}&zoom=15'
#     print(url)
#     print(requests.get(url, headers=headers))

# if __name__ == '__main__':
#     parse_organization('56.84167164304492, 60.59684586518415')