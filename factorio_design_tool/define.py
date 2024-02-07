import enum


# 存在するアイテムの一覧
class Item(enum.Enum):
    # 資源
    wood = enum.auto()          # 木材
    coal = enum.auto()          # 石炭
    iron_ore = enum.auto()      # 鉄鉱石
    copper_ore = enum.auto()    # 銅鉱石
    stone = enum.auto()         # 石
    crude_oil = enum.auto()     # 原油
    raw_fish = enum.auto()      # 生魚
    water = enum.auto()         # 水
    steam = enum.auto()         # 蒸気
    uranium_ore = enum.auto()   # ウラン鉱石

    # 素材
    iron_plate = enum.auto()                    # 鉄板
    copper_plate = enum.auto()                  # 銅板
    steel_plate = enum.auto()                   # 鋼材
    sulfur = enum.auto()                        # 硫黄
    plastic_bar = enum.auto()                   # プラスチック棒
    empty_barrel = enum.auto()                  # 空のドラム缶
    iron_stick = enum.auto()                    # 鉄筋
    iron_gear_wheel = enum.auto()               # 鉄の歯車
    copper_cable = enum.auto()                  # 銅線
    electronic_circuit = enum.auto()            # 電子基板
    advanced_circuit = enum.auto()              # 発展基板
    processing_unit = enum.auto()               # 制御基板
    engine_unit = enum.auto()                   # エンジンユニット
    electric_engine_unit = enum.auto()          # 電気エンジンユニット
    explosives = enum.auto()                    # 爆薬
    battery = enum.auto()                       # 電池
    flying_robot_frame = enum.auto()            # 飛行用ロボットフレーム
    automation_science_pack = enum.auto()       # 自動化サイエンスパック
    logistic_science_pack = enum.auto()         # 物流サイエンスパック
    chemical_science_pack = enum.auto()         # 化学サイエンスパック
    military_science_pack = enum.auto()         # 軍事サイエンスパック
    production_science_pack = enum.auto()       # 製造サイエンスパック
    utility_science_pack = enum.auto()          # ユーティリティーサイエンスパック
    space_science_pack = enum.auto()            # スペースサイエンスパック
    solid_fuel = enum.auto()                    # 固形燃料
    low_density_structure = enum.auto()         # 軽量化素材
    rocket_fuel = enum.auto()                   # ロケット燃料
    nuclear_fuel = enum.auto()                  # 核燃料
    rocket_control_unit = enum.auto()           # ロケット制御装置
    satellite = enum.auto()                     # 衛星
    uranium_235 = enum.auto()                   # ウラン-235
    uranium_238 = enum.auto()                   # ウラン-238
    used_up_uranium_fuel_cell = enum.auto()     # 使用済み核燃料棒
    uranium_fuel_cell = enum.auto()             # 核燃料棒


# 対応する言語一覧
class Language(enum.Enum):
    english = enum.auto()
    japanese = enum.auto()


# アイテム単位の入出力情報を保持するクラス
class ItemIO():
    def __init__(self, item: Item, amount: int) -> None:
        self.item = item
        self.amount = amount
        return


# レシピの情報を保持するクラス
class Recipe():
    def __init__(self, inputs: list[ItemIO], outputs: list[ItemIO], time: float) -> None:
        self.inputs = inputs
        self.outputs = outputs
        self.time = time
        return


# アイテムの情報を保持するクラス
class ItemData():
    def __init__(self, name: str, name_japanese: str) -> None:
        self.name = {
            Language.english: name,
            Language.japanese: name_japanese,
        }
        return


RECIPES = [
    Recipe([ItemIO(Item.iron_ore, 1)], [ItemIO(Item.iron_plate, 1)], 3.2),                                          # 鉄板
    Recipe([ItemIO(Item.copper_ore, 1)], [ItemIO(Item.copper_plate, 1)], 3.2),                                      # 銅板
    Recipe([ItemIO(Item.iron_plate, 5)], [ItemIO(Item.steel_plate, 1)], 16),                                        # 鋼材
    Recipe([ItemIO(Item.steel_plate, 1)], [ItemIO(Item.empty_barrel, 1)], 1),                                       # 空のドラム缶
    Recipe([ItemIO(Item.iron_plate, 1)], [ItemIO(Item.iron_stick, 2)], 0.5),                                        # 鉄筋
    Recipe([ItemIO(Item.iron_plate, 2)], [ItemIO(Item.iron_gear_wheel, 1)], 0.5),                                   # 鉄の歯車
    Recipe([ItemIO(Item.copper_plate, 1)], [ItemIO(Item.copper_cable, 2)], 0.5),                                    # 銅線
    Recipe([ItemIO(Item.iron_plate, 1), ItemIO(Item.copper_cable, 3)], [ItemIO(Item.electronic_circuit, 1)], 0.5),  # 電子基板
]

# 全アイテムの情報を保持する辞書
ITEM_DATA = {
                                                                                        # 資源
    Item.wood: ItemData("Wood", "木材"),
    Item.coal: ItemData("Coal", "石炭"),
    Item.iron_ore: ItemData("Iron ore", "鉄鉱石"),
    Item.copper_ore: ItemData("Copper ore", "銅鉱石"),
    Item.stone: ItemData("Stone", "石"),
    Item.crude_oil: ItemData("Crude oil", "原油"),
    Item.raw_fish: ItemData("Raw fish", "生魚"),
    Item.water: ItemData("Water", "水"),
    Item.steam: ItemData("Steam", "蒸気"),
    Item.uranium_ore: ItemData("Uranium ore", "ウラン鉱石"),

                                                                                        # 素材
    Item.iron_plate: ItemData("Iron plate", "鉄板"),
    Item.copper_plate: ItemData("Copper plate", "銅板"),
    Item.steel_plate: ItemData("Steel plate", "鋼材"),
    Item.sulfur: ItemData("Sulfur", "硫黄"),
    Item.plastic_bar: ItemData("Plastic bar", "プラスチック棒"),
    Item.empty_barrel: ItemData("Empty barrel", "空のドラム缶"),
    Item.iron_stick: ItemData("Iron stick", "鉄筋"),
    Item.iron_gear_wheel: ItemData("Iron gear wheel", "鉄の歯車"),
    Item.copper_cable: ItemData("Copper cable", "銅線"),
    Item.electronic_circuit: ItemData("Electronic circuit", "電子基板"),
    Item.advanced_circuit: ItemData("Advanced circuit", "発展基板"),
    Item.processing_unit: ItemData("Processing unit", "制御基板"),
    Item.engine_unit: ItemData("Engine unit", "エンジンユニット"),
    Item.electric_engine_unit: ItemData("Electric engine unit", "電気エンジンユニット"),
    Item.explosives: ItemData("Explosives", "爆薬"),
    Item.battery: ItemData("Battery", "電池"),
    Item.flying_robot_frame: ItemData("Flying robot frame", "飛行用ロボットフレーム"),
    Item.automation_science_pack: ItemData("Automation science pack", "自動化サイエンスパック"),
    Item.logistic_science_pack: ItemData("Logistic science pack", "物流サイエンスパック"),
    Item.chemical_science_pack: ItemData("Chemical science pack", "化学サイエンスパック"),
    Item.military_science_pack: ItemData("Military science pack", "軍事サイエンスパック"),
    Item.production_science_pack: ItemData("Production science pack", "製造サイエンスパック"),
    Item.utility_science_pack: ItemData("Utility science pack", "ユーティリティーサイエンスパック"),
    Item.space_science_pack: ItemData("Space science pack", "スペースサイエンスパック"),
    Item.solid_fuel: ItemData("Solid fuel", "固形燃料"),
    Item.low_density_structure: ItemData("Low density structure", "軽量化素材"),
    Item.rocket_fuel: ItemData("Rocket fuel", "ロケット燃料"),
    Item.nuclear_fuel: ItemData("Nuclear fuel", "核燃料"),
    Item.rocket_control_unit: ItemData("Rocket control unit", "ロケット制御装置"),
    Item.satellite: ItemData("Satellite", "衛星"),
    Item.uranium_235: ItemData("Uranium-235", "ウラン-235"),
    Item.uranium_238: ItemData("Uranium-238", "ウラン-238"),
    Item.used_up_uranium_fuel_cell: ItemData("Used up uranium fuel cell", "使用済み核燃料棒"),
    Item.uranium_fuel_cell: ItemData("Uranium fuel cell", "核燃料棒"),
}
