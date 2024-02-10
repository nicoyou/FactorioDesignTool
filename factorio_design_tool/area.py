from .define import Item, Recipe
from .item_path import ItemPath


# ワールド内のエリアの情報を管理するクラス
class Area():
    def __init__(self, name: str, mining_productivity: float) -> None:
        self.name = name                                # エリア名
        self.mining_productivity = mining_productivity  # 採掘量倍率
        self.resources: list[ItemPath] = []             # このエリアで得られる資源
        self.inputs: list[ItemPath] = []                # 他のエリアで作られたアイテム
        self.processes: list[ItemPath] = []             # このエリアで行われる加工工程
        return

    def create_resource(self, recipe: Recipe, machine_num: int) -> ItemPath:
        if recipe.inputs:
            raise ValueError("Resource recipe has inputs")
        if len(recipe.outputs) != 1:
            raise ValueError("Resource recipe has multiple outputs")
        mag = 1.0
        if recipe.outputs[0].item in (Item.coal, Item.iron_ore, Item.copper_ore, Item.stone, Item.uranium_ore):
            mag *= self.mining_productivity
        resource = ItemPath(recipe.outputs[0].item, (machine_num * recipe.outputs[0].amount * mag) / recipe.time, self.name)
        self.resources.append(resource)
        return resource

    def add_processing_item_path(self, recipe: Recipe, machine_num: int) -> list[ItemPath]:
        # レシピの入力に必要な全てのアイテムがエリア内に存在するか確認
        for recipe_input in recipe.inputs:
            recipe_input_required = recipe_input.amount * machine_num
            if self.get_resource_amount(recipe_input.item) < recipe_input_required:
                raise ValueError(f"Item {recipe_input.item} is not enough [required: {recipe_input_required}, actual: {self.get_resource_amount(recipe_input.item)}]")

        # 完成物のアイテムパスを作成
        outputs = []
        for recipe_output in recipe.outputs:
            outputs.append(ItemPath(recipe_output.item, recipe_output.amount * machine_num, self.name))
        self.processes += outputs
        # 渡されたレシピのアイテムパスを作成
        for recipe_input in recipe.inputs:
            self.sub_resource_amount(recipe_input.item, recipe_input.amount * machine_num, outputs)
        return outputs

    def get_resource_amount(self, item: Item) -> float:
        return sum(resource.production_per_second for resource in (self.resources + self.inputs + self.processes) if resource.item == item)

    def sub_resource_amount(self, item: Item, amount: float, resource_use_children: list[ItemPath]) -> None:
        for resource in (self.resources + self.processes + self.inputs):    # エリア内の素材を優先して消費する
            if resource.item == item and resource.available_production_per_second > 0:
                amount = resource.use_production_per_second(amount, resource_use_children)
            if amount == 0:
                return
        raise ValueError(f"Item {item} not found")
