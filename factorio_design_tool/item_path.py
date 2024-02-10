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

    def export_edge_to_dot(self, dot, ignore_node_ids: list) -> None:
        for child in self.children:
            if (self.node_id, child.item_path.node_id) not in ignore_node_ids:  # 同一ノード同士のエッジを重複して出力しない
                dot.edge(self.node_id, child.item_path.node_id, label=f"{child.amount}/s")
                ignore_node_ids.append((self.node_id, child.item_path.node_id))
            child.item_path.export_edge_to_dot(dot, ignore_node_ids)
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
    def node_id(self) -> str:
        return f"{self.area_id}_{self.item}"

    @property
    def available_production_per_second(self) -> float:
        return self.production_per_second - self.used_production_per_second


# 加工工程の子要素への参照を保持するクラス
class ItemPathLink():
    def __init__(self, item_path: ItemPath, amount: float) -> None:
        self.item_path = item_path
        self.amount = amount
        return
