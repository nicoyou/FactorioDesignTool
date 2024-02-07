from .define import Item
from .item_path import ItemPath


# ワールド内のエリアの情報を管理するクラス
class Area():
    def __init__(self, name: str) -> None:
        self.name = name
        self.resources: list[ItemPath] = []     # このエリアで得られる資源
        return

    def create_resource(self, item: Item, production_per_second: int) -> ItemPath:
        resource = ItemPath(item, production_per_second)
        self.resources.append(resource)
        return resource
