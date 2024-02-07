import graphviz

from .area import Area
from .define import Language, ITEM_DATA


# ワールド全体の情報を管理するクラス
class World():
    def __init__(self, language: Language = Language.english) -> None:
        self.language = language
        self.areas: list[Area] = []
        return

    def create_area(self, name: str) -> Area:
        if any(area.name == name for area in self.areas):
            raise ValueError(f"Area {name} already exists")
        area = Area(name)
        self.areas.append(area)
        return area

    def export_factory_blueprint(self) -> None:
        dot = graphviz.Digraph("recipe_tree", comment="Recipe", format="png", engine="dot")
        dot.attr("graph", rankdir="BT")
        dot.attr("node", fontname="MS Gothic", shape="box")
        for area in self.areas:
            subgraph = graphviz.Digraph(name=f"cluster_{area.name}")
            subgraph.attr(label=area.name)
            subgraph.attr(color="grey")
            for resource in area.resources:
                subgraph.node(f"{area.name}_{resource.item}", f"{ITEM_DATA[resource.item].name[self.language]}: {resource.production_per_second}/s")
            dot.subgraph(subgraph)
        dot.render(directory="data", view=True)
        return
