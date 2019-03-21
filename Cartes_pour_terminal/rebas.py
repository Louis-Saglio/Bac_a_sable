from sys import argv

nom_classe = argv[1]
attribute_name = argv[2]


def create_getter(attribute_name, tab="    "):
    return "def get_{attribute_name}(self):\n{tab}return self.{attribute_name}".format(
        attribute_name=attribute_name, tab=tab
    )


def create_setter(attribute_name, tab="    "):
    return "def set_{attribute_name}(self, new_{attribute_name}):\n{tab}self.{attribute_name} = new_{attribute_name}".format(
        attribute_name=attribute_name, tab=tab
    )


with open("buffer.py", "w") as fichier:
    fichier.write(create_getter(attribute_name))
    fichier.write("\n\n")
    fichier.write(create_setter(attribute_name))
