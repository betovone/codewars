import unittest
from sort_products import sort_products

class Section:
    
    def __init__(self, id, name, sequence) -> None:
        self.id = id
        self.name = name
        self.sequence = sequence
        

class Product:
    
    def __init__(self, id, name, sequence, item_from_template, section_id) -> None:
        self.id = id
        self.name = name
        self.sequence = sequence
        self.item_from_template = item_from_template
        self.section_id = section_id



class TestSortProducts(unittest.TestCase):
    
    def setUp(self) -> None:
        self.sections = [
            Section(29, "Monitoreo", 2),
            Section(33, "Basicas", 4)
        ]
        self.products = [
            Product(23, "Prod 1", 1, True, None),
            Product(24, "Prod 2", 3, True, None),
            Product(25, "Prod 3", 5, True, 33),
            Product(26, "Prod 4", 6, False, 29),
            Product(27, "Prod 5", 7, False, 29),
        ]
        self.sections2 = [
            Section(291, "Monitoreo", 1),
            Section(331, "Basicas", 5)
        ]
        self.products2 = [
            Product(231, "Prod 1", 2, True, None),
            Product(241, "Prod 2", 3, False, 291),
            Product(251, "Prod 3", 4, False, 291),
            Product(261, "Prod 4", 6, True, 331),
            Product(271, "Prod 5", 7, False, 291),
        ]
        
    
    def test_sort(self):
        print("test sort products")
        self.assertEqual(
            sort_products(self.sections, self.products), 
            {
                23:1,
                29:2,
                24:3,
                26:4,
                27:5,
                33:6,
                25:7
            }
        )
        self.assertEqual(
            sort_products(self.sections2, self.products2), 
            {
                291:1,
                231:2,
                241:5,
                251:6,
                271:7,
                331:8,
                261:9
            }
        )
        