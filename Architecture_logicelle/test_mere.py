from unittest import TestCase
import Architecture_logicelle.mere as mere


class TestMere(TestCase):
    def test_add_child(self):
        mother = mere.Mere()
        self.assertEqual(mother.class_name, "Mere")

    def test__find_list_field_name_for_new_child(self):
        mother = mere.Mere()
        mother.filles = []
        fille = mere.Test()
        fille.class_name = "Fille"
        self.assertEqual(mother._find_list_field_name_for_new_child(fille), "filles")
        mother.tests = []
        test = mere.Test()
        self.assertEqual(mother._find_list_field_name_for_new_child(test), "tests")
        mother.items = [mere.Test()]
        self.assertEqual(mother._find_list_field_name_for_new_child(mere.Test()), "items")

    def test_find_item_from_child_list_field_by_field(self):
        mother = mere.Mere()
        t1 = mere.Test()
        t2 = mere.Test()
        t1.name = "abc"
        t2.name = "cde"
        mother.filles = [t1, t2]
        found = mother.find_item_from_child_list_field_by_field("filles", "name", "cde")
        self.assertIs(found, t2)
