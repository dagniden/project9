from typing import Generator


def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    for item in range(start, end):
        card_nums = str(item)
        nums_len = len(card_nums)
        zeros_amount = 16 - nums_len
        lead_zeros = "".join(["0" for _ in range(zeros_amount)])
        card = lead_zeros + card_nums
        card_groups = split_groups(card, 4)
        card = " ".join(card_groups)
        yield card


def split_groups(text: str, size: int) -> list[str]:
    iterations = int(len(text) / size)
    return [text[i * size : (i + 1) * size] for i in range(iterations)]


def transaction_descriptions() -> None:
    pass


def filter_by_currency() -> None:
    pass


if __name__ == "__main__":
    pass
