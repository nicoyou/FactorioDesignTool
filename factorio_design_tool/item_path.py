from typing import Self

from .define import Item


# 資源からアイテムを作るまでの加工工程を保持するクラス
class ItemPath():
    def __init__(self, item: Item, production_per_second: float, area_id: str) -> None:
        self.item = item
        self.production_per_second = production_per_second
        self.used_production_per_second = 0.0
        self.children: list[ItemPathLink] = []
        self.area_id = area_id
        return

    def export_edge_to_dot(self, dot) -> None:
        for child in self.children:
            dot.edge(f"{self.area_id}_{self.item}", f"{child.item_path.area_id}_{child.item_path.item}", label=f"{child.amount}/s")
            child.item_path.export_edge_to_dot(dot)
        return

    def use_production_per_second(self, amount: float, children: list[Self]) -> float:
        result_amount = amount

        if self.available_production_per_second >= amount:
            self.used_production_per_second += amount
            result_amount = 0
        else:
            result_amount -= self.available_production_per_second
            self.used_production_per_second += self.available_production_per_second
        self.children += [ItemPathLink(row, amount - result_amount if i == 0 else 0) for i, row in enumerate(children)]
        return result_amount    # 使い切れなかった分を返す

    @property
    def available_production_per_second(self) -> float:
        return self.production_per_second - self.used_production_per_second


class ItemPathLink():
    def __init__(self, item_path: ItemPath, amount: float) -> None:
        self.item_path = item_path
        self.amount = amount
        return
