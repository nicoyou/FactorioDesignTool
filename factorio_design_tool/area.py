import math

from .define import Item, Recipe, get_main_recipe
from .item_path import ItemPath

# 資源として無から生成可能なアイテム
RESOURCE_ITEMS = (Item.coal, Item.iron_ore, Item.copper_ore, Item.stone, Item.uranium_ore, Item.crude_oil)


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
        if recipe.outputs[0].item in RESOURCE_ITEMS:
            mag *= self.mining_productivity
        new_resource = ItemPath(recipe.outputs[0].item, (machine_num * recipe.outputs[0].amount * mag) / recipe.time, self.name)
        # すでに存在するリソース
        existing_resources = [row for row in self.resources if new_resource.item == row.item]
        if len(existing_resources) > 0:
            existing_resources[0].production_per_second += new_resource.production_per_second
            return existing_resources[0]

        self.resources.append(new_resource)
        return new_resource

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

        for output in outputs:
            for process in self.processes:      # self.processes に同じアイテムがあれば結合する
                if process.item == output.item:
                    process.production_per_second += output.production_per_second
                    break
            else:
                self.processes.append(output)   # self.processes に outputs を追加する

        # 渡されたレシピのアイテムパスリンクを作成
        for recipe_input in recipe.inputs:
            self.sub_resource_amount(recipe_input.item, recipe_input.amount * machine_num, outputs)
        return outputs

    def add_processing_item_path_replenish_material(self, recipe: Recipe, machine_num: int) -> list[ItemPath]:
        # レシピの入力に必要な全てのアイテムがエリア内に存在するか確認し、存在しなければ補填する
        # 複数中間素材が必要なレシピで、一つ目の素材と二つ目の中間素材の素材が同じ場合に、一つ目の素材が補填されたあとにそれを二つ目の中間素材として使用されてしまう
        # そのため for ですべての input に対して補填が起きなくなるまで繰り返す
        for i in range(10):
            replenish_material_flag = False     # 足りない素材の補填を行ったフラグ

            for recipe_input in recipe.inputs:
                recipe_input_required = recipe_input.amount * machine_num
                if self.get_resource_amount(recipe_input.item) < recipe_input_required:
                    need_machine_num = math.ceil((recipe_input_required - self.get_resource_amount(recipe_input.item)) /
                                                 [row for row in get_main_recipe(recipe_input.item).outputs if row.item == recipe_input.item][0].amount)
                    self.add_processing_item_path_replenish_material(get_main_recipe(recipe_input.item), need_machine_num)
                    replenish_material_flag = True
            if not replenish_material_flag:
                break
        else:
            raise ValueError(f"unknown error")

        if len(recipe.inputs) == 0 and len(recipe.outputs) == 1 and recipe.outputs[0].item in RESOURCE_ITEMS:   # 指定されたレシピが資源の場合は create_resource を呼ぶ
            return [self.create_resource(recipe, math.ceil(machine_num * recipe.time / self.mining_productivity))]
        return self.add_processing_item_path(recipe, machine_num)

    def get_resource_amount(self, item: Item) -> float:
        return sum(resource.available_production_per_second for resource in (self.resources + self.inputs + self.processes) if resource.item == item)

    def sub_resource_amount(self, item: Item, amount: float, resource_use_children: list[ItemPath]) -> None:
        for resource in (self.resources + self.processes + self.inputs):    # エリア内の素材を優先して消費する
            if resource.item == item and resource.available_production_per_second > 0:
                amount = resource.use_production_per_second(amount, resource_use_children)
            if amount == 0:
                return
        raise ValueError(f"Item {item} not found or not enough available [required: {amount}, actual: {self.get_resource_amount(item)}]")
