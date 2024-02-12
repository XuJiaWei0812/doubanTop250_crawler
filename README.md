# 異步爬蟲練習:豆瓣電影Top250

這個 Python 程序能夠抓取豆瓣電影網站Top250電影的資料，並將其保存到Excel文件中。該程序使用的是異步請求來爬取網站，本程序只供學習用途。

## 功能介紹
這個 Python 程序能夠從豆瓣電影網站抓取Top250電影的資料，並將其保存到Excel文件中。它利用異步請求來提高數據抓取的效率。

**異步抓取豆瓣電影Top 250的信息。**

**提取每部電影的排名、片名、評分、評論人數和詳情頁面連結。**

**將抓取的數據保存到Excel文件。**

## 安裝需求

要運行此腳本，您需要安裝以下套件：

- `aiohttp`
- `BeautifulSoup4`
- `openpyxl`
- `fake_useragent`

您可以使用以下命令安裝這些套件：

```bash
pip install aiohttp beautifulsoup4 openpyxl fake_useragent
```

## 使用方法

1. 確保您已安裝所有套件。
2. 將程序下載到您的本地機器。
3. 在程序的所在目錄中打開終端。
4. 執行腳本：

    ```bash
    python douban_top250_scraper.py
    ```

5. 腳本運行完成後，您將在腳本的同一目錄下找到名為 `豆瓣電影Top250.xlsx` 的Excel文件。
