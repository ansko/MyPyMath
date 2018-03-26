from mypymath.geometry.figures.polygon_regular import PolygonRegular


class PrismRegular:
    def __init__(self,
                 param1, param2): # (top_facet, bottom_facet)
        if (isinstance(param1, PolygonRegular) and
              isinstance(param2, PolygonRegular)):
            top_facet = param1
            bottom_facet = param2
            self.__init_primitive(top_facet, bottom_facet)
            return
        else:
            print('Error in RegularPrism.__init__:',
                  'incorrect argumetns')
            return None

    def __init_primitive(self, top_facet, bot_facet):
        self.top_facet = top_facet
        self.bot_facet = bot_facet
