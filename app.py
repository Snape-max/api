from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pathlib import Path

# 初始化 FastAPI 应用
app = FastAPI(
    redoc_url=None
)

# 配置跨域支持
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有域名访问
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 动态加载 routers 文件夹中的子文件夹
routers_dir = Path(__file__).parent / "routers"
print(f"Loading routers from {routers_dir}")
for router_folder in routers_dir.iterdir():
    if router_folder.is_dir() and "__init__.py" in [f.name for f in router_folder.iterdir()]:
        module_name = router_folder.name
        module = __import__(f"routers.{module_name}", fromlist=["router"])
        app.include_router(module.router, prefix=f"/{module_name}")
        print(f"Loaded router for {module_name}")
        
@app.get("/", response_class=HTMLResponse)
def index():
    return """
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Qiumo API</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f9f9f9;
                color: #333;
                line-height: 1.6;
            }
            header, footer {
                background-color: #4CAF50;
                color: white;
                text-align: center;
                padding: 1rem 0;
            }
            main {
                max-width: 800px;
                margin: 2rem auto;
                padding: 1rem;
                background: white;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            }
            h1, h2 {
                color: #4CAF50;
            }
            code {
                background-color: #f4f4f4;
                padding: 0.2rem 0.5rem;
                border-radius: 4px;
                font-family: monospace;
            }
            a {
                color: #4CAF50;
                text-decoration: none;
            }
            a:hover {
                text-decoration: underline;
            }
            footer p {
                margin: 0;
                font-size: 0.9rem;
            }
            @media (max-width: 600px) {
                main {
                    padding: 1rem;
                }
                h1 {
                    font-size: 1.5rem;
                }
                h2 {
                    font-size: 1.2rem;
                }
            }
        </style>
    </head>
    <body>
        <header>
            <h1>Qiumo API</h1>
        </header>
        <main>
            <center>
                <h2>小红书图片解析</h2>
                <p>请求：<code>/xiaohongshu/image?url={URL}</code></p>
            </center>
            <center>
                <h2>其他——敬请期待</h2>
            </center>
        </main>
        <footer>
            <p>Powered by <a href="https://github.com/qiumo/qiumo-api">Qiumo API</a></p>
        </footer>
    </body>
    </html>
    """