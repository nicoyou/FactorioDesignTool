from .define import Item


# 資源からアイテムを作るまでの加工工程を保持するクラス
class ItemPath():
    def __init__(self, item: Item, production_per_second: int) -> None:
        self.item = item
        self.production_per_second = production_per_second
        return
