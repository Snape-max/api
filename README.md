# Qiumo API

Qiumo API 是一个轻量级、模块化的 API 系统，旨在为开发者提供便捷的接口服务。目前支持小红书图片解析等功能，未来将逐步扩展更多实用工具。

---

## 特点

- **高性能**: 基于 FastAPI 构建，充分利用异步编程的优势。
- **易用性**: 交互式文档页面（`/docs`），方便快速测试和集成。
- **模块化设计**: 每个功能独立封装，便于维护和扩展。
- **可定制化**: 支持自定义标题、样式和文档页面。
- **安全性**: 支持跨域配置和身份验证机制。

---

## 快速开始

1. 克隆项目：
   ```bash
   git clone https://github.com/Snape-max/api.git
   cd api
   ```

2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

3. 启动应用：
   ```bash
   uvicorn app:app --reload
   ```

4. 访问以下链接：
   - 主页: [http://127.0.0.1:8000](http://127.0.0.1:8000)
   - 文档: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 功能列表

- **小红书图片解析**:
  - 请求示例: `/xiaohongshu/image?url=<URL>`
  - 文档: [/docs#/XiaoHongShu/parse_image_xiaohongshu_image_get](http://127.0.0.1:8000/docs#/XiaoHongShu/parse_image_xiaohongshu_image_get)

- **其他功能**: 敬请期待！

---

## 拓展性

Qiumo API 的设计遵循模块化原则，具有高度的可扩展性。以下是其拓展性的具体体现以及如何进行扩展的说明：

### 1. 添加新功能

新增功能非常简单，只需在 `routers` 文件夹下创建新的子文件夹，并按照以下步骤操作：

#### 示例：添加微博内容解析功能

1. **创建模块文件夹**:
   在 `routers` 文件夹下创建 `weibo` 文件夹：
   ```
   routers/
   ├── weibo/
   │   ├── __init__.py
   │   └── content.py
   ```

2. **定义路由**:
   在 `content.py` 中定义新的 API 路由：
   ```python
   from fastapi import APIRouter

   router = APIRouter(prefix="/content", tags=["Weibo Content Parsing"])

   @router.get("/")
   async def parse_weibo_content(url: str):
       """
       解析微博内容
       :param url: 微博页面链接
       """
       result = WeiboParser(url)
       return result
   ```

3. **初始化模块**:
   在 `weibo/__init__.py` 中初始化路由器：
   ```python
   from fastapi import APIRouter
   from .content import router as content_router

   router = APIRouter(tags=["Weibo API"])
   router.include_router(content_router)
   ```

4. **测试新功能**:
   启动应用后，访问以下 URL 测试新功能：
   ```
   http://127.0.0.1:8000/weibo/content?url=<微博链接>
   ```

### 2. 集成外部工具

可以通过依赖注入的方式集成外部工具或服务（如数据库、缓存等）。例如：
```python
from fastapi import Depends

def get_db():
    db = "Database Connection"
    return db

@app.get("/example-with-db")
async def example_with_db(db=Depends(get_db)):
    return {"db": db}
```

### 3. 自定义文档

为新功能添加详细的文档说明，可以在路由定义中使用 `description` 和 `summary` 参数：
```python
@router.get("/", summary="解析微博内容", description="根据提供的微博链接解析内容")
async def parse_weibo_content(url: str):
    ...
```

---

## 未来计划

- 添加更多实用工具（如视频解析、文本翻译等）。
- 集成第三方服务（如支付网关、短信通知等）。
- 提供更强大的安全机制（如 OAuth2 认证、JWT 令牌）。
- 支持分布式部署和负载均衡。

---

## 贡献指南

欢迎提交 Issue 或 Pull Request！如果你有任何问题或建议，请随时联系我。

---

## 许可证

本项目采用 [MIT 许可证](LICENSE)。