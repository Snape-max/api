from fastapi import APIRouter, Query
from utils.random_ua import RandomUserAgent
import requests as req
import re
from urllib.parse import unquote
import bs4

# 图片解析子路由
image_router = APIRouter(prefix="/image", tags=["Image Parsing"])

def HongshuParser(url: str) -> dict:
    try:
        url = unquote(url)
        headers = {
            'User-Agent': RandomUserAgent()  # 调用优化后的 RandomUA 函数
        }
        html = req.get(url, headers=headers)
        soup = bs4.BeautifulSoup(html.content.decode(), features="lxml")
        images = soup.find_all("meta", attrs={'name': "og:image"})
        descriptions = soup.find_all("meta", attrs={'name': "description"})
        urls = re.findall(r'content="([^"\']*)"', str(images))
        description = re.findall(r'<meta content="(.*?)" name="description"', str(descriptions))[0]
        images = []
        for s in urls:
            images.append(re.findall(r'/([^!/]+)!', s)[0])
        return {"images": images, "description": description}
    except Exception as e:
        return {"message": "Internal Server Error", "error": str(e), "url": url}

@image_router.get("/")
async def parse_image(url: str = Query(..., description="url编码后页面链接")):
    """
    小红书图片解析, 输入小红书url编码后页面链接，返回图片id和文章描述
    """
    res = HongshuParser(url)
    return res
    
