class CssColors(object):
    def __init__(self, color=None, highlight=None, run=None):
        self.prefix = {}
        self.prefix.update({'color': 'mcolor-'})
        self.prefix.update({'highlight': 'mhighlight-'})
        self.colors = {}
        self.colors.update({'color': color})
        self.colors.update({'highlight': highlight})
        if run:
            if run.color:
                self.colors.update({'color':run.color})
            if run.highlight:
                self.colors.update({'highlight': run.highlight})

    def _get_cls(self,tipe):
        prefix = self.prefix[tipe]

        try:
            value = self.colors[tipe]
        except KeyError:
            return None

        if value:
            r = "{}{}".format(prefix, value)
            return r
        return None

    def __str__(self):
        classes = []
        for t in ['color', 'highlight']:
            cls = self._get_cls(t)
            if cls:
                classes.append(cls)
        if classes:
            return " ".join(classes)
        return ""

    def __repr__(self):
        r = self.__str__()
        return r