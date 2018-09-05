import cobble

from . import html


def path(elements):
    return HtmlPath(elements)


def element(names, class_names=None, fresh=None, separator=None):
    if class_names is None:
        class_names = []
    if fresh is None:
        fresh = False
    if class_names:
        attributes = {"class": " ".join(class_names)}
    else:
        attributes = {}
    return HtmlPathElement(html.tag(
        tag_names=names,
        attributes=attributes,
        collapsible=not fresh,
        separator=separator,
    ))


@cobble.data
class HtmlPath(object):
    elements = cobble.field()
    
    def wrap(self, generate_nodes):
        nodes = generate_nodes()

        for element in reversed(self.elements):
            nodes = element.wrap_nodes(nodes)
        
        return nodes


@cobble.data
class HtmlPathElement(object):
    tag = cobble.field()

    def wrap(self, generate_nodes):
        return self.wrap_nodes(generate_nodes())

    def wrap_nodes(self, nodes):
        element = html.Element(self.tag, nodes)
        return [element]

    def add_class_attribute(self, cls):
        try:
            my_cls = self.tag.attributes["class"].split(" ")
        except KeyError:
            my_cls = []
        my_cls.extend(cls.split(" "))
        new_cls = ' '.join(my_cls)
        self.tag.attributes["class"] = new_cls

empty = path([])


class ignore(object):
    @staticmethod
    def wrap(generate_nodes):
        return []
