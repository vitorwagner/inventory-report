from inventory_report.product import Product


def test_create_product() -> None:
    product = Product(
        "1",
        "HMS Erebus",
        "Pembroke Dock",
        "07/06/1826",
        "22/04/1848",
        "1",
        "Keep in a cool and dry place",
    )
    assert product.id == "1"
    assert product.product_name == "HMS Erebus"
    assert product.company_name == "Pembroke Dock"
    assert product.manufacturing_date == "07/06/1826"
    assert product.expiration_date == "22/04/1848"
    assert product.serial_number == "1"
    assert product.storage_instructions == "Keep in a cool and dry place"
