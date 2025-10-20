from src.masks import get_mask_account
from src.masks import get_mask_card_number


def main() -> None:
    """Тестовый запуск функций маскировки."""
    print(get_mask_card_number(7000792289606361))
    print(get_mask_account(73654108430135874305))


if __name__ == "__main__":
    main()
