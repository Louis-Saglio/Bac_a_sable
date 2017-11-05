def get(obj, index):
    try:
        return obj[index]
    except IndexError:
        pass
    except TypeError:
        pass
    return None


class Mere:

    def __init__(self):  # todo: ajouter **kwargs
        self.filles = []
        self.garcons = []
        self.class_name = str(self.__class__).split('.')[-1][:-2]

    def add_child(self, child, field=None, child_mother_name=None):
        if child_mother_name is None:
            # todo: find_mother_field_name dans child ?
            child_mother_name = self.class_name
        if field is None:
            field = self._find_list_field_name_for_new_child(child)
        child.__dict__[child_mother_name] = self  # todo: choisir le nom du mother field
        self.__dict__[field].append(child)  # todo: autre methode que append

    def __find_list_field_name_for_new_child_by_class_name(self, child):
        if hasattr(child, "class_name"):
            return child.class_name
        return str(child.__class__).split('.')[-1][:-2].lower() + 's'

    def _find_list_field_name_for_new_child(self, child):
        list_field_names = [""] * 3
        names = self.__find_list_field_name_for_new_child_by_class_name(child)
        list_field_names[0], list_field_names[2] = names[0], names[1]  # errors
        for attr_name, attr in self.__dict__.items():
            if get(attr, 0).__class__ is type(child):
                list_field_names[1] = attr_name
        for list_field_name in list_field_names:
            if hasattr(self, list_field_name):
                return list_field_name
        raise ValueError(f"Impossible de déterminer automatiquement l'attribut ou ranger {child}"
                         f"Nom(s) testé(s) : {[name for name in list_field_names if name]}")

    def find_item_from_child_list_field_by_field(self, list_field_name, child_field_name, matching_value):
        for item in self.__dict__[list_field_name]:
            if item.__dict__[child_field_name] == matching_value:
                return item


class Child:

    def __init__(self, mother=None):  # todo: dans le __init__ par defaut ou non initialisé ?
        self.class_name = str(self.__class__).split('.')[-1][:-2]
        if mother is not None:
            mother.add_child(self)


class Fille(Child):
    pass


class Test:
    def __repr__(self):
        return str(self.__dict__)
