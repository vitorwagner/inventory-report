from typing import Dict, List, Type
from inventory_report.product import Product
from abc import ABC, abstractmethod
import json


class Importer(ABC):
    def __init__(self, path: str) -> None:
        self.path = path

    @abstractmethod
    def import_data(self) -> List[Product]:
        ...


class JsonImporter(Importer):
    def import_data(self) -> List[Product]:
        products = []

        with open(self.path) as file:
            data = json.load(file)

        for product in data:
            products.append(Product(
                product["id"],
                product["product_name"],
                product["company_name"],
                product["manufacturing_date"],
                product["expiration_date"],
                product["serial_number"],
                product["storage_instructions"]
            ))

        return products


class CsvImporter(Importer):
    pass


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
