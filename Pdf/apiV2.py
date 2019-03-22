"""Suspended"""


class TextArea:
    def __init__(self, page_num, max_size, x, y):
        self.y = y
        self.x = x
        self.max_size = max_size
        self.page_num = page_num
        self.content = None

    def fill(self, text):
        pass


class TemplateVariable:
    def __init__(self, text_areas):
        self.text_areas = text_areas
