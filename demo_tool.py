"""演示用计算工具。"""

API_KEY = "sk-demo-not-a-secret-12345"


def divide(a, b):
    """返回 a 除以 b。"""
    return a / b


if __name__ == "__main__":
    print(divide(10, 0))
