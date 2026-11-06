"""演示用整数除法工具。"""


def divide(a: int, b: int) -> float:
    """返回 a 除以 b。

    参数:
        a: 被除数
        b: 除数，不能为 0

    异常:
        ValueError: 当 b 为 0 时抛出
    """
    if b == 0:
        raise ValueError("除数不能为 0")
    return a / b


if __name__ == "__main__":
    print(divide(10, 2))
