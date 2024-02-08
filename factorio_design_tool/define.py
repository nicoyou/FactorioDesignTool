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

    # 流体
    sulfuric_acid = enum.auto()     # 硫酸
    heavy_oil = enum.auto()         # 重油
    light_oil = enum.auto()         # 軽油
    petroleum_gas = enum.auto()     # 石油ガス
    lubricant = enum.auto()         # 潤滑油
    steam = enum.auto()             # 蒸気

    # 貯蔵
    wooden_chest = enum.auto()              # 木製チェスト
    iron_chest = enum.auto()                # 鉄製チェスト
    steel_chest = enum.auto()               # 鋼鉄製チェスト
    active_provider_chest = enum.auto()     # アクティブ供給チェスト
    buffer_chest = enum.auto()              # バッファーチェスト
    passive_provider_chest = enum.auto()    # パッシブ供給チェスト
    requester_chest = enum.auto()           # 要求チェスト
    storage_chest = enum.auto()             # 貯蔵チェスト
    storage_tank = enum.auto()              # 貯蔵タンク

    # 運送
    transport_belt = enum.auto()            # 搬送ベルト
    fast_transport_belt = enum.auto()       # 高速搬送ベルト
    express_transport_belt = enum.auto()    # 超高速搬送ベルト
    underground_belt = enum.auto()          # 地下搬送ベルト
    fast_underground_belt = enum.auto()     # 高速地下搬送ベルト
    express_underground_belt = enum.auto()  # 超高速地下搬送ベルト
    splitter = enum.auto()                  # 分配器
    fast_splitter = enum.auto()             # 高速分配器
    express_splitter = enum.auto()          # 超高速分配器
    pipe = enum.auto()                      # パイプ
    pipe_to_ground = enum.auto()            # 地下パイプ
    pump = enum.auto()                      # ポンプ

    # インサータ
    burner_inserter = enum.auto()       # 燃料式インサータ
    inserter = enum.auto()              # インサータ
    long_handed_inserter = enum.auto()  # ロングアームインサータ
    fast_inserter = enum.auto()         # 高速インサータ
    stack_inserter = enum.auto()        # スタックインサータ
    balk_inserter = enum.auto()         # バルクインサータ

    # 電柱・配線
    small_electric_pole = enum.auto()       # 小型電柱
    medium_electric_pole = enum.auto()      # 中型電柱
    big_electric_pole = enum.auto()         # 大型電柱
    substation = enum.auto()                # 広域電柱
    red_wire = enum.auto()                  # レッドケーブル
    green_wire = enum.auto()                # グリーンケーブル
    arithmetic_combinator = enum.auto()     # 算術回路
    decider_combinator = enum.auto()        # 条件回路
    constant_combinator = enum.auto()       # 定数回路
    power_switch = enum.auto()              # 電源スイッチ

    # 鉄道・車両
    rail = enum.auto()                  # レール
    train_stop = enum.auto()            # 駅
    rail_signal = enum.auto()           # 信号
    rail_chain_signal = enum.auto()     # 連動式列車用信号
    locomotive = enum.auto()            # 機関車
    artillery_wagon = enum.auto()       # 長距離砲車両
    cargo_wagon = enum.auto()           # 貨物車両
    fluid_wagon = enum.auto()           # タンク貨車
    car = enum.auto()                   # 自動車
    tank = enum.auto()                  # 戦車
    spidertron = enum.auto()            # スパイダートロン
    spidertron_remote = enum.auto()     # スパイダートロンリモコン

    # ロボ関連
    logistic_robot = enum.auto()        # 物流ロボット
    construction_robot = enum.auto()    # 建造ロボット
    roboport = enum.auto()              # ロボットステーション

    # 舗装道路・整地
    stone_brick = enum.auto()               # 石レンガ
    concrete = enum.auto()                  # コンクリート
    hazard_concrete = enum.auto()           # 警戒色コンクリート
    refined_concrete = enum.auto()          # 鉄筋コンクリート
    refined_hazard_concrete = enum.auto()   # 鉄筋警戒コンクリート
    landfill = enum.auto()                  # 埋立地
    cliff_explosives = enum.auto()          # 崖用爆薬

    # 採掘施設
    burner_mining_drill = enum.auto()       # 燃料式掘削機
    electric_mining_drill = enum.auto()     # 電動掘削機
    pump_jack = enum.auto()                 # 油井

    # 発電・蓄電施設
    offshore_pump = enum.auto()     # 汲み上げポンプ
    boiler = enum.auto()            # ボイラー
    steam_engine = enum.auto()      # 蒸気機関
    steam_turbine = enum.auto()     # 蒸気タービン
    solar_panel = enum.auto()       # ソーラーパネル
    accumulator = enum.auto()       # 蓄電池
    nuclear_reactor = enum.auto()   # 原子炉
    heat_exchanger = enum.auto()    # 熱交換器
    heat_pipe = enum.auto()         # ヒートパイプ
    centrifuge = enum.auto()        # 遠心分離機

    # 溶鉱炉
    stone_furnace = enum.auto()     # 石の炉
    steel_furnace = enum.auto()     # 鋼鉄の炉
    electric_furnace = enum.auto()  # 電気炉

    # 組立機
    assembling_machine_1 = enum.auto()  # 組立機1
    assembling_machine_2 = enum.auto()  # 組立機2
    assembling_machine_3 = enum.auto()  # 組立機3

    # 原油由来物精製施設
    oil_refinery = enum.auto()      # 原油精製所
    chemical_plant = enum.auto()    # 化学プラント

    # モジュール
    speed_module_1 = enum.auto()            # 生産速度モジュール1
    speed_module_2 = enum.auto()            # 生産速度モジュール2
    speed_module_3 = enum.auto()            # 生産速度モジュール3
    effectivity_module_1 = enum.auto()      # エネルギー効率モジュール1
    effectivity_module_2 = enum.auto()      # エネルギー効率モジュール2
    effectivity_module_3 = enum.auto()      # エネルギー効率モジュール3
    productivity_module_1 = enum.auto()     # 生産力モジュール1
    productivity_module_2 = enum.auto()     # 生産力モジュール2
    productivity_module_3 = enum.auto()     # 生産力モジュール3

    # 装備武器
    pistol = enum.auto()            # ハンドガン
    submachine_gun = enum.auto()    # サブマシンガン
    shotgun = enum.auto()           # ショットガン
    combat_shotgun = enum.auto()    # コンバットショットガン
    rocket_launcher = enum.auto()   # ロケットランチャー
    flamethrower = enum.auto()      # 火炎放射器

    # 弾薬
    firearm_magazine = enum.auto()                  # 通常弾薬
    piercing_rounds_magazine = enum.auto()          # 貫通弾薬
    uranium_rounds_magazine = enum.auto()           # 劣化ウラン弾薬
    shotgun_shell = enum.auto()                     # ショットガン弾薬
    piercing_shotgun_shell = enum.auto()            # 貫通ショットガン弾薬
    rocket = enum.auto()                            # ロケット弾
    explosive_rocket = enum.auto()                  # 炸裂ロケット弾
    atomic_bomb = enum.auto()                       # 原子爆弾
    cannon_shell = enum.auto()                      # 砲弾
    uranium_cannon_shell = enum.auto()              # 劣化ウラン砲弾
    explosive_cannon_shell = enum.auto()            # 炸裂砲弾
    explosive_uranium_cannon_shell = enum.auto()    # 炸裂ウラン砲弾
    artillery_shell = enum.auto()                   # 長距離砲弾
    flamethrower_ammo = enum.auto()                 # 火炎放射器用燃料

    # 投擲武器
    grenade = enum.auto()               # 手榴弾
    cluster_grenade = enum.auto()       # クラスターグレネード
    poison_capsule = enum.auto()        # 毒素カプセル
    slowdown_capsule = enum.auto()      # 粘着カプセル
    defender_capsule = enum.auto()      # ディフェンダーカプセル
    distractor_capsule = enum.auto()    # ディストラクターカプセル
    destroyer_capsule = enum.auto()     # デストロイヤーカプセル

    # 鎧
    light_armor = enum.auto()           # 軽鎧
    heavy_armor = enum.auto()           # 重鎧
    basic_modular_armor = enum.auto()   # モジュラーアーマー
    power_armor = enum.auto()           # パワーアーマー
    power_armor_mk2 = enum.auto()       # パワーアーマー MK2

    # アーマーモジュール
    portable_solar_panel = enum.auto()      # 携帯ソーラーパネルモジュール
    portable_fusion_reactor = enum.auto()   # 携帯核融合炉モジュール
    energy_shield = enum.auto()             # エネルギーシールドモジュール
    energy_shield_mk2 = enum.auto()         # エネルギーシールドモジュールMK2
    battery = enum.auto()                   # バッテリーモジュール
    battery_mk2 = enum.auto()               # バッテリーモジュールMK2
    personal_laser_defense = enum.auto()    # 携帯レーザー防御モジュール
    exoskeleton = enum.auto()               # 強化外骨格モジュール
    night_vision = enum.auto()              # 暗視モジュール
    discharge_defense = enum.auto()         # 携帯放電防御モジュール
    personal_roboport = enum.auto()         # 携帯ロボットステーション
    personal_roboport_mk2 = enum.auto()     # 携帯ロボットステーションMK2
    belt_immunity = enum.auto()             # ベルト移動耐性装備

    # タレット
    gun_turret = enum.auto()            # ガンタレット
    laser_turret = enum.auto()          # レーザータレット
    flamethrower_turret = enum.auto()   # 火炎放射タレット
    artillery_turret = enum.auto()      # 長距離砲タレット

    # その他軍用品
    land_mine = enum.auto()                                 # 地雷
    wall = enum.auto()                                      # 防壁
    gate = enum.auto()                                      # ゲート
    radar = enum.auto()                                     # レーダー
    basic_electric_discharge_defense_remote = enum.auto()   # 放電モジュール制御装置
    artillery_targeting_remote = enum.auto()                # 遠方照準器
    rocket_silo = enum.auto()                               # ロケットサイロ

    # その他
    rocket_part = enum.auto()   # ロケット部品


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
        if len(outputs) <= 0:
            raise ValueError("Output item is not found")
        return


# アイテムの情報を保持するクラス
class ItemData():
    def __init__(self, name: str, name_japanese: str) -> None:
        self.name = {
            Language.english: name,
            Language.japanese: name_japanese,
        }
        return


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

                                                                                        # 流体
    Item.sulfuric_acid: ItemData("Sulfuric acid", "硫酸"),
    Item.heavy_oil: ItemData("Heavy oil", "重油"),
    Item.light_oil: ItemData("Light oil", "軽油"),
    Item.petroleum_gas: ItemData("Petroleum gas", "石油ガス"),
    Item.lubricant: ItemData("Lubricant", "潤滑油"),
    Item.steam: ItemData("Steam", "蒸気"),
    Item.water: ItemData("Water", "水"),

                                                                                        # 貯蔵
    Item.wooden_chest: ItemData("Wooden chest", "木製チェスト"),
    Item.iron_chest: ItemData("Iron chest", "鉄製チェスト"),
    Item.steel_chest: ItemData("Steel chest", "鋼鉄製チェスト"),
    Item.active_provider_chest: ItemData("Active provider chest", "アクティブ供給チェスト"),
    Item.buffer_chest: ItemData("Buffer chest", "バッファーチェスト"),
    Item.passive_provider_chest: ItemData("Passive provider chest", "パッシブ供給チェスト"),
    Item.requester_chest: ItemData("Requester chest", "要求チェスト"),
    Item.storage_chest: ItemData("Storage chest", "貯蔵チェスト"),
    Item.storage_tank: ItemData("Storage tank", "貯蔵タンク"),

                                                                                        # 運送
    Item.transport_belt: ItemData("Transport belt", "搬送ベルト"),
    Item.fast_transport_belt: ItemData("Fast transport belt", "高速搬送ベルト"),
    Item.express_transport_belt: ItemData("Express transport belt", "超高速搬送ベルト"),
    Item.underground_belt: ItemData("Underground belt", "地下搬送ベルト"),
    Item.fast_underground_belt: ItemData("Fast underground belt", "高速地下搬送ベルト"),
    Item.express_underground_belt: ItemData("Express underground belt", "超高速地下搬送ベルト"),
    Item.splitter: ItemData("Splitter", "分配器"),
    Item.fast_splitter: ItemData("Fast splitter", "高速分配器"),
    Item.express_splitter: ItemData("Express splitter", "超高速分配器"),
    Item.pipe: ItemData("Pipe", "パイプ"),
    Item.pipe_to_ground: ItemData("Pipe to ground", "地下パイプ"),
    Item.pump: ItemData("Pump", "ポンプ"),

                                                                                        # インサータ
    Item.burner_inserter: ItemData("Burner inserter", "燃料式インサータ"),
    Item.inserter: ItemData("Inserter", "インサータ"),
    Item.long_handed_inserter: ItemData("Long handed inserter", "ロングアームインサータ"),
    Item.fast_inserter: ItemData("Fast inserter", "高速インサータ"),
    Item.stack_inserter: ItemData("Stack inserter", "スタックインサータ"),
    Item.balk_inserter: ItemData("Balk inserter", "バルクインサータ"),

                                                                                        # 電柱・配線
    Item.small_electric_pole: ItemData("Small electric pole", "小型電柱"),
    Item.medium_electric_pole: ItemData("Medium electric pole", "中型電柱"),
    Item.big_electric_pole: ItemData("Big electric pole", "大型電柱"),
    Item.substation: ItemData("Substation", "広域電柱"),
    Item.red_wire: ItemData("Red wire", "レッドケーブル"),
    Item.green_wire: ItemData("Green wire", "グリーンケーブル"),
    Item.arithmetic_combinator: ItemData("Arithmetic combinator", "算術回路"),
    Item.decider_combinator: ItemData("Decider combinator", "条件回路"),
    Item.constant_combinator: ItemData("Constant combinator", "定数回路"),
    Item.power_switch: ItemData("Power switch", "電源スイッチ"),

                                                                                        # 鉄道・車両
    Item.rail: ItemData("Rail", "レール"),
    Item.train_stop: ItemData("Train stop", "駅"),
    Item.rail_signal: ItemData("Rail signal", "信号"),
    Item.rail_chain_signal: ItemData("Rail chain signal", "連動式列車用信号"),
    Item.locomotive: ItemData("Locomotive", "機関車"),
    Item.artillery_wagon: ItemData("Artillery wagon", "長距離砲車両"),
    Item.cargo_wagon: ItemData("Cargo wagon", "貨物車両"),
    Item.fluid_wagon: ItemData("Fluid wagon", "タンク貨車"),
    Item.car: ItemData("Car", "自動車"),
    Item.tank: ItemData("Tank", "戦車"),
    Item.spidertron: ItemData("Spidertron", "スパイダートロン"),
    Item.spidertron_remote: ItemData("Spidertron remote", "スパイダートロンリモコン"),

                                                                                        # ロボ関連
    Item.logistic_robot: ItemData("Logistic robot", "物流ロボット"),
    Item.construction_robot: ItemData("Construction robot", "建造ロボット"),
    Item.roboport: ItemData("Roboport", "ロボットステーション"),

                                                                                        # 舗装道路・整地
    Item.stone_brick: ItemData("Stone brick", "石レンガ"),
    Item.concrete: ItemData("Concrete", "コンクリート"),
    Item.hazard_concrete: ItemData("Hazard concrete", "警戒色コンクリート"),
    Item.refined_concrete: ItemData("Refined concrete", "鉄筋コンクリート"),
    Item.refined_hazard_concrete: ItemData("Refined hazard concrete", "鉄筋警戒コンクリート"),
    Item.landfill: ItemData("Landfill", "埋立地"),
    Item.cliff_explosives: ItemData("Cliff explosives", "崖用爆薬"),

                                                                                        # 採掘施設
    Item.burner_mining_drill: ItemData("Burner mining drill", "燃料式掘削機"),
    Item.electric_mining_drill: ItemData("Electric mining drill", "電動掘削機"),
    Item.pump_jack: ItemData("Pump jack", "油井"),

                                                                                        # 発電・蓄電施設
    Item.offshore_pump: ItemData("Offshore pump", "汲み上げポンプ"),
    Item.boiler: ItemData("Boiler", "ボイラー"),
    Item.steam_engine: ItemData("Steam engine", "蒸気機関"),
    Item.steam_turbine: ItemData("Steam turbine", "蒸気タービン"),
    Item.solar_panel: ItemData("Solar panel", "ソーラーパネル"),
    Item.accumulator: ItemData("Accumulator", "蓄電池"),
    Item.nuclear_reactor: ItemData("Nuclear reactor", "原子炉"),
    Item.heat_exchanger: ItemData("Heat exchanger", "熱交換器"),
    Item.heat_pipe: ItemData("Heat pipe", "ヒートパイプ"),
    Item.centrifuge: ItemData("Centrifuge", "遠心分離機"),

                                                                                        # 溶鉱炉
    Item.stone_furnace: ItemData("Stone furnace", "石の炉"),
    Item.steel_furnace: ItemData("Steel furnace", "鋼鉄の炉"),
    Item.electric_furnace: ItemData("Electric furnace", "電気炉"),

                                                                                        # 組立機
    Item.assembling_machine_1: ItemData("Assembling machine 1", "組立機1"),
    Item.assembling_machine_2: ItemData("Assembling machine 2", "組立機2"),
    Item.assembling_machine_3: ItemData("Assembling machine 3", "組立機3"),

                                                                                        # 原油由来物精製施設
    Item.oil_refinery: ItemData("Oil refinery", "原油精製所"),
    Item.chemical_plant: ItemData("Chemical plant", "化学プラント"),

                                                                                        # モジュール
    Item.speed_module_1: ItemData("Speed module 1", "生産速度モジュール1"),
    Item.speed_module_2: ItemData("Speed module 2", "生産速度モジュール2"),
    Item.speed_module_3: ItemData("Speed module 3", "生産速度モジュール3"),
    Item.effectivity_module_1: ItemData("Effectivity module 1", "エネルギー効率モジュール1"),
    Item.effectivity_module_2: ItemData("Effectivity module 2", "エネルギー効率モジュール2"),
    Item.effectivity_module_3: ItemData("Effectivity module 3", "エネルギー効率モジュール3"),
    Item.productivity_module_1: ItemData("Productivity module 1", "生産力モジュール1"),
    Item.productivity_module_2: ItemData("Productivity module 2", "生産力モジュール2"),
    Item.productivity_module_3: ItemData("Productivity module 3", "生産力モジュール3"),

                                                                                        # 装備武器
    Item.pistol: ItemData("Pistol", "ハンドガン"),
    Item.submachine_gun: ItemData("Submachine gun", "サブマシンガン"),
    Item.shotgun: ItemData("Shotgun", "ショットガン"),
    Item.combat_shotgun: ItemData("Combat shotgun", "コンバットショットガン"),
    Item.rocket_launcher: ItemData("Rocket launcher", "ロケットランチャー"),
    Item.flamethrower: ItemData("Flamethrower", "火炎放射器"),

                                                                                        # 弾薬
    Item.firearm_magazine: ItemData("Firearm magazine", "通常弾薬"),
    Item.piercing_rounds_magazine: ItemData("Piercing rounds magazine", "貫通弾薬"),
    Item.uranium_rounds_magazine: ItemData("Uranium rounds magazine", "劣化ウラン弾薬"),
    Item.shotgun_shell: ItemData("Shotgun shell", "ショットガン弾薬"),
    Item.piercing_shotgun_shell: ItemData("Piercing shotgun shell", "貫通ショットガン弾薬"),
    Item.rocket: ItemData("Rocket", "ロケット弾"),
    Item.explosive_rocket: ItemData("Explosive rocket", "炸裂ロケット弾"),
    Item.atomic_bomb: ItemData("Atomic bomb", "原子爆弾"),
    Item.cannon_shell: ItemData("Cannon shell", "砲弾"),
    Item.uranium_cannon_shell: ItemData("Uranium cannon shell", "劣化ウラン砲弾"),
    Item.explosive_cannon_shell: ItemData("Explosive cannon shell", "炸裂砲弾"),
    Item.explosive_uranium_cannon_shell: ItemData("Explosive uranium cannon shell", "炸裂ウラン砲弾"),
    Item.artillery_shell: ItemData("Artillery shell", "長距離砲弾"),
    Item.flamethrower_ammo: ItemData("Flamethrower ammo", "火炎放射器用燃料"),

                                                                                        # 投擲武器
    Item.grenade: ItemData("Grenade", "手榴弾"),
    Item.cluster_grenade: ItemData("Cluster grenade", "クラスターグレネード"),
    Item.poison_capsule: ItemData("Poison capsule", "毒素カプセル"),
    Item.slowdown_capsule: ItemData("Slowdown capsule", "粘着カプセル"),
    Item.defender_capsule: ItemData("Defender capsule", "ディフェンダーカプセル"),
    Item.distractor_capsule: ItemData("Distractor capsule", "ディストラクターカプセル"),
    Item.destroyer_capsule: ItemData("Destroyer capsule", "デストロイヤーカプセル"),

                                                                                        # 鎧
    Item.light_armor: ItemData("Light armor", "軽鎧"),
    Item.heavy_armor: ItemData("Heavy armor", "重鎧"),
    Item.basic_modular_armor: ItemData("Basic modular armor", "モジュラーアーマー"),
    Item.power_armor: ItemData("Power armor", "パワーアーマー"),
    Item.power_armor_mk2: ItemData("Power armor MK2", "パワーアーマー MK2"),

                                                                                        # アーマーモジュール
    Item.portable_solar_panel: ItemData("Portable solar panel", "携帯ソーラーパネルモジュール"),
    Item.portable_fusion_reactor: ItemData("Portable fusion reactor", "携帯核融合炉モジュール"),
    Item.energy_shield: ItemData("Energy shield", "エネルギーシールドモジュール"),
    Item.energy_shield_mk2: ItemData("Energy shield MK2", "エネルギーシールドモジュールMK2"),
    Item.battery: ItemData("Battery", "バッテリーモジュール"),
    Item.battery_mk2: ItemData("Battery MK2", "バッテリーモジュールMK2"),
    Item.personal_laser_defense: ItemData("Personal laser defense", "携帯レーザー防御モジュール"),
    Item.exoskeleton: ItemData("Exoskeleton", "強化外骨格モジュール"),
    Item.night_vision: ItemData("Night vision", "暗視モジュール"),
    Item.discharge_defense: ItemData("Discharge defense", "携帯放電防御モジュール"),
    Item.personal_roboport: ItemData("Personal roboport", "携帯ロボットステーション"),
    Item.personal_roboport_mk2: ItemData("Personal roboport MK2", "携帯ロボットステーションMK2"),
    Item.belt_immunity: ItemData("Belt immunity", "ベルト移動耐性装備"),

                                                                                        # タレット
    Item.gun_turret: ItemData("Gun turret", "ガンタレット"),
    Item.laser_turret: ItemData("Laser turret", "レーザータレット"),
    Item.flamethrower_turret: ItemData("Flamethrower turret", "火炎放射タレット"),
    Item.artillery_turret: ItemData("Artillery turret", "長距離砲タレット"),

                                                                                        # その他軍用品
    Item.land_mine: ItemData("Land mine", "地雷"),
    Item.wall: ItemData("Wall", "防壁"),
    Item.gate: ItemData("Gate", "ゲート"),
    Item.radar: ItemData("Radar", "レーダー"),
    Item.basic_electric_discharge_defense_remote: ItemData("Basic electric discharge defense remote", "放電モジュール制御装置"),
    Item.artillery_targeting_remote: ItemData("Artillery targeting remote", "遠方照準器"),
    Item.rocket_silo: ItemData("Rocket silo", "ロケットサイロ"),

                                                                                        # その他
    Item.rocket_part: ItemData("Rocket part", "ロケット部品"),
}

RECIPES = [
                                                                                                                                                                # 資源採取系
    Recipe([], [ItemIO(Item.coal, 1)], 2),                                                                                                                      # 石炭
    Recipe([], [ItemIO(Item.iron_ore, 1)], 2),                                                                                                                  # 鉄鉱石
    Recipe([], [ItemIO(Item.copper_ore, 1)], 2),                                                                                                                # 銅鉱石
    Recipe([], [ItemIO(Item.stone, 1)], 2),                                                                                                                     # 石
    Recipe([], [ItemIO(Item.uranium_ore, 1)], 2),                                                                                                               # ウラン鉱石
    Recipe([], [ItemIO(Item.water, 1200)], 1),                                                                                                                  # 水
    Recipe([], [ItemIO(Item.crude_oil, 2)], 1),                                                                                                                 # 原油

                                                                                                                                                                # 素材加工系
    Recipe([ItemIO(Item.iron_ore, 1)], [ItemIO(Item.iron_plate, 1)], 3.2),                                                                                      # 鉄板
    Recipe([ItemIO(Item.copper_ore, 1)], [ItemIO(Item.copper_plate, 1)], 3.2),                                                                                  # 銅板
    Recipe([ItemIO(Item.iron_plate, 5)], [ItemIO(Item.steel_plate, 1)], 16),                                                                                    # 鋼材
    Recipe([ItemIO(Item.water, 30), ItemIO(Item.petroleum_gas, 30)], [ItemIO(Item.sulfur, 2)], 1),                                                              # 硫黄
    Recipe([ItemIO(Item.petroleum_gas, 20), ItemIO(Item.coal, 1)], [ItemIO(Item.plastic_bar, 2)], 1),                                                           # プラスチック棒
    Recipe([ItemIO(Item.steel_plate, 1)], [ItemIO(Item.empty_barrel, 1)], 1),                                                                                   # 空のドラム缶
    Recipe([ItemIO(Item.iron_plate, 1)], [ItemIO(Item.iron_stick, 2)], 0.5),                                                                                    # 鉄筋
    Recipe([ItemIO(Item.iron_plate, 2)], [ItemIO(Item.iron_gear_wheel, 1)], 0.5),                                                                               # 鉄の歯車
    Recipe([ItemIO(Item.copper_plate, 1)], [ItemIO(Item.copper_cable, 2)], 0.5),                                                                                # 銅線
    Recipe([ItemIO(Item.iron_plate, 1), ItemIO(Item.copper_cable, 3)], [ItemIO(Item.electronic_circuit, 1)], 0.5),                                              # 電子基板
    Recipe([ItemIO(Item.electronic_circuit, 2), ItemIO(Item.plastic_bar, 2), ItemIO(Item.copper_cable, 4)], [ItemIO(Item.advanced_circuit, 1)], 6),             # 発展基板
    Recipe([ItemIO(Item.electronic_circuit, 20), ItemIO(Item.advanced_circuit, 2),
            ItemIO(Item.sulfuric_acid, 5)], [ItemIO(Item.processing_unit, 1)], 10),                                                                             # 制御基板
    Recipe([ItemIO(Item.steel_plate, 1), ItemIO(Item.iron_gear_wheel, 1), ItemIO(Item.pipe, 2)], [ItemIO(Item.engine_unit, 1)], 10),                            # エンジンユニット
    Recipe([ItemIO(Item.engine_unit, 1), ItemIO(Item.lubricant, 15), ItemIO(Item.electronic_circuit, 2)], [ItemIO(Item.electric_engine_unit, 1)], 10),          # 電気エンジンユニット
    Recipe([ItemIO(Item.sulfur, 1), ItemIO(Item.coal, 1), ItemIO(Item.water, 10)], [ItemIO(Item.explosives, 2)], 4),                                            # 爆薬
    Recipe([ItemIO(Item.sulfuric_acid, 20), ItemIO(Item.iron_plate, 1), ItemIO(Item.copper_plate, 1)], [ItemIO(Item.battery, 1)], 4),                           # 電池
    Recipe([ItemIO(Item.electric_engine_unit, 1), ItemIO(Item.battery, 2),
            ItemIO(Item.steel_plate, 1), ItemIO(Item.electronic_circuit, 3)], [ItemIO(Item.flying_robot_frame, 1)], 20),                                        # 飛行用ロボットフレーム
    Recipe([ItemIO(Item.copper_plate, 1), ItemIO(Item.iron_gear_wheel, 1)], [ItemIO(Item.automation_science_pack, 1)], 5),                                      # 自動化サイエンスパック
    Recipe([ItemIO(Item.inserter, 1), ItemIO(Item.transport_belt, 1)], [ItemIO(Item.logistic_science_pack, 1)], 6),                                             # 物流サイエンスパック
    Recipe([ItemIO(Item.engine_unit, 2), ItemIO(Item.advanced_circuit, 3), ItemIO(Item.sulfur, 1)], [ItemIO(Item.chemical_science_pack, 2)], 24),               # 化学サイエンスパック
    Recipe([ItemIO(Item.piercing_rounds_magazine, 1), ItemIO(Item.grenade, 1), ItemIO(Item.wall, 2)], [ItemIO(Item.military_science_pack, 2)], 10),             # 軍事サイエンスパック
    Recipe([ItemIO(Item.productivity_module_1, 1), ItemIO(Item.electric_furnace, 1), ItemIO(Item.rail, 30)], [ItemIO(Item.production_science_pack, 3)], 21),    # 製造サイエンスパック
    Recipe([ItemIO(Item.flying_robot_frame, 1), ItemIO(Item.processing_unit, 2),
            ItemIO(Item.low_density_structure, 3)], [ItemIO(Item.utility_science_pack, 3)], 21),                                                                # ユーティリティーサイエンスパック
    Recipe([ItemIO(Item.heavy_oil, 20)], [ItemIO(Item.solid_fuel, 1)], 2),                                                                                      # 固形燃料
    Recipe([ItemIO(Item.light_oil, 10)], [ItemIO(Item.solid_fuel, 1)], 2),                                                                                      # 固形燃料
    Recipe([ItemIO(Item.petroleum_gas, 20)], [ItemIO(Item.solid_fuel, 1)], 2),                                                                                  # 固形燃料
    Recipe([ItemIO(Item.steel_plate, 2), ItemIO(Item.copper_plate, 20), ItemIO(Item.plastic_bar, 5)], [ItemIO(Item.low_density_structure, 1)], 20),             # 軽量化素材
    Recipe([ItemIO(Item.solid_fuel, 10), ItemIO(Item.light_oil, 10)], [ItemIO(Item.rocket_fuel, 1)], 30),                                                       # ロケット燃料
    Recipe([ItemIO(Item.rocket_fuel, 1), ItemIO(Item.uranium_235, 1)], [ItemIO(Item.nuclear_fuel, 1)], 60),                                                     # 核燃料
    Recipe([ItemIO(Item.processing_unit, 1), ItemIO(Item.speed_module_1, 1)], [ItemIO(Item.rocket_control_unit, 1)], 30),                                       # ロケット制御装置
    Recipe([
        ItemIO(Item.low_density_structure, 100),
        ItemIO(Item.solar_panel, 100),
        ItemIO(Item.accumulator, 100),
        ItemIO(Item.radar, 5),
        ItemIO(Item.processing_unit, 100),
        ItemIO(Item.rocket_fuel, 50),
    ], [ItemIO(Item.satellite, 1)], 3),                                                                                                                         # 衛星
    Recipe([ItemIO(Item.iron_plate, 10), ItemIO(Item.uranium_235, 1), ItemIO(Item.uranium_238, 19)], [ItemIO(Item.uranium_fuel_cell, 10)], 10),                 # 核燃料棒

                                                                                                                                                                # 輸送系
    Recipe([ItemIO(Item.iron_plate, 1), ItemIO(Item.iron_gear_wheel, 1)], [ItemIO(Item.transport_belt, 2)], 0.5),                                               # 搬送ベルト
    Recipe([ItemIO(Item.iron_gear_wheel, 5), ItemIO(Item.transport_belt, 1)], [ItemIO(Item.fast_transport_belt, 1)], 0.5),                                      # 高速搬送ベルト
    Recipe(
        [ItemIO(Item.iron_gear_wheel, 10), ItemIO(Item.fast_transport_belt, 1), ItemIO(Item.lubricant, 20)], [ItemIO(Item.express_transport_belt, 1)], 0.5),    # 超高速搬送ベルト
    Recipe([ItemIO(Item.iron_plate, 10), ItemIO(Item.transport_belt, 5)], [ItemIO(Item.underground_belt, 2)], 1),                                               # 地下搬送ベルト
    Recipe([ItemIO(Item.iron_gear_wheel, 40), ItemIO(Item.underground_belt, 2)], [ItemIO(Item.fast_underground_belt, 2)], 2),                                   # 高速地下搬送ベルト
    Recipe([ItemIO(Item.iron_gear_wheel, 80), ItemIO(Item.fast_underground_belt, 2),
            ItemIO(Item.lubricant, 40)], [ItemIO(Item.express_underground_belt, 2)], 2),                                                                        # 超高速地下搬送ベルト
    Recipe([ItemIO(Item.electronic_circuit, 5), ItemIO(Item.iron_plate, 5), ItemIO(Item.transport_belt, 4)], [ItemIO(Item.splitter, 1)], 1),                    # 分配器
    Recipe([ItemIO(Item.splitter, 1), ItemIO(Item.iron_gear_wheel, 10), ItemIO(Item.electronic_circuit, 10)], [ItemIO(Item.fast_splitter, 1)], 2),              # 高速分配器
    Recipe([ItemIO(Item.fast_splitter, 1), ItemIO(Item.iron_gear_wheel, 10),
            ItemIO(Item.advanced_circuit, 10), ItemIO(Item.lubricant, 80)], [ItemIO(Item.express_splitter, 1)], 2),                                             # 超高速分配器
    Recipe([ItemIO(Item.iron_plate, 1)], [ItemIO(Item.pipe, 1)], 0.5),                                                                                          # パイプ
    Recipe([ItemIO(Item.pipe, 10), ItemIO(Item.iron_plate, 5)], [ItemIO(Item.pipe_to_ground, 2)], 0.5),                                                         # 地下パイプ
    Recipe([ItemIO(Item.engine_unit, 1), ItemIO(Item.steel_plate, 1), ItemIO(Item.pipe, 1)], [ItemIO(Item.pump, 1)], 2),                                        # ポンプ

                                                                                                                                                                # インサータ系
    Recipe([ItemIO(Item.iron_plate, 1), ItemIO(Item.iron_gear_wheel, 1)], [ItemIO(Item.burner_inserter, 1)], 0.5),                                              # 燃料式インサータ
    Recipe([ItemIO(Item.electronic_circuit, 1), ItemIO(Item.iron_gear_wheel, 1), ItemIO(Item.iron_plate, 1)], [ItemIO(Item.inserter, 1)], 0.5),                 # インサータ
    Recipe([ItemIO(Item.iron_gear_wheel, 1), ItemIO(Item.iron_plate, 1), ItemIO(Item.inserter, 1)], [ItemIO(Item.long_handed_inserter, 1)], 0.5),               # ロングアームインサータ
    Recipe([ItemIO(Item.electronic_circuit, 2), ItemIO(Item.iron_plate, 2), ItemIO(Item.inserter, 1)], [ItemIO(Item.fast_inserter, 1)], 0.5),                   # 高速インサータ
    Recipe([ItemIO(Item.fast_inserter, 1), ItemIO(Item.iron_gear_wheel, 15),
            ItemIO(Item.electronic_circuit, 15),
            ItemIO(Item.advanced_circuit, 1)], [ItemIO(Item.stack_inserter, 1)], 0.5),                                                                          # スタックインサータ
]


def get_main_recipe(item: Item) -> Recipe:
    for recipe in RECIPES:
        for output in recipe.outputs:
            if output.item == item:
                return recipe
    raise ValueError(f"Recipe not found for item {item}")
