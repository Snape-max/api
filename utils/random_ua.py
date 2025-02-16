import random
from .config import USER_AGENTS

def RandomUserAgent() -> str:
    """
    随机获取User-Agent
    """
    return random.choice(USER_AGENTS)