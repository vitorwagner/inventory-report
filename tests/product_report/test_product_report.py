from inventory_report.product import Product


def test_product_report() -> None:
    product = Product(
        "1",
        "HMS Erebus",
        "Pembroke Dock",
        "07/06/1826",
        "22/04/1848",
        "1",
        "Keep in a cool and dry place",
    )
    assert (
        str(product)
        == "The product 1 - HMS Erebus "
        "with serial number 1 "
        "manufactured on 07/06/1826 "
        "by the company Pembroke Dock "
        "valid until 22/04/1848 "
        "must be stored according to the following instructions: "
        "Keep in a cool and dry place."
    )
