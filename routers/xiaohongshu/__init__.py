from fastapi import APIRouter
from .image import image_router

# 小红书解析主路由
router = APIRouter(tags=["XiaoHongShu"])

# 注册解析子路由
router.include_router(image_router)

