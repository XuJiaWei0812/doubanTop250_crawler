import asyncio
import aiohttp
from bs4 import BeautifulSoup
import openpyxl
from fake_useragent import UserAgent
import random
import time

async def request_douban(url, headers):
    """異步發送請求並獲取響應文本。"""
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url, headers=headers) as response:
                response.raise_for_status()
                return await response.text()
        except aiohttp.ClientError as e:
            print(f"發生客戶端錯誤: {e}")
        except Exception as err:
            print(f"發生錯誤: {err}")
        return None

def parse_html(html):
    """解析HTML並提取電影資訊。"""
    try:
        soup = BeautifulSoup(html, 'html.parser')
        list = soup.find(class_='grid_view').find_all('li')
        result = []
        for item in list:
            movie = {
                '排名': item.find(class_='pic').find('em').text,
                '片名': item.find(class_='info').find('a').find('span').text,
                '評分': item.find(class_='star').find(class_='rating_num').text,
                '評論人數': item.find(class_='star').find_all('span')[3].text[:-3],
                '連結': item.find(class_='hd').find('a').get('href'),
            }
            result.append(movie)
        return result
    except Exception as e:
        print(f"無法解析 HTML: {e}")
        return []

def save_to_excel(data, filename):
    """將電影資料保存到Excel檔案。"""
    try:
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.title = '豆瓣電影Top250'
        sheet.append(['排名', '片名', '評分', '評論人數', '連結'])
        for item in data:
            sheet.append([item['排名'], item['片名'], item['評分'], item['評論人數'], item['連結']])
        workbook.save(filename)
    except Exception as e:
        print(f"保存文件失敗: {e}")

async def main(base_url, filename):
    """主函數，執行豆瓣電影Top250的抓取和保存。"""
    start_time = time.time()

    top_movies = []
    ua = UserAgent()
    tasks = []
    for i in range(0, 250, 25):
        url = base_url.format(i)
        headers = {'User-Agent': ua.random}
        task = asyncio.create_task(request_douban(url, headers))
        tasks.append(task)
        await asyncio.sleep(random.randint(1, 3))
    responses = await asyncio.gather(*tasks)
    for html in responses:
        if html:
            top_movies.extend(parse_html(html))
    save_to_excel(top_movies, filename)
    
    end_time = time.time()
    print(f"豆瓣電影Top250程序在 {end_time - start_time} 秒内完成")

if __name__ == '__main__':
    base_url = 'https://movie.douban.com/top250?start={}'  # 可配置的URL模板
    filename = '豆瓣電影Top250.xlsx'  # 可配置的文件名
    asyncio.run(main(base_url, filename))
