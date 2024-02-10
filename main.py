from factorio_design_tool import Item, Language, World, get_main_recipe

if __name__ == "__main__":
    world = World(Language.japanese)

    area1 = world.create_area("Area1")
    area1.create_resource(get_main_recipe(Item.iron_ore), 90)
    area1.create_resource(get_main_recipe(Item.copper_ore), 60)
    area1.create_resource(get_main_recipe(Item.coal), 20)
    area1.add_processing_item_path(get_main_recipe(Item.iron_plate), 45)
    area1.add_processing_item_path(get_main_recipe(Item.copper_plate), 30)

    area2 = world.create_area("Area2")
    area2.create_resource(get_main_recipe(Item.iron_ore), 120)
    area2_iron_plate = area2.add_processing_item_path(get_main_recipe(Item.iron_plate), 60)[0]

    area1.inputs.append(area2_iron_plate)
    area1.add_processing_item_path(get_main_recipe(Item.iron_gear_wheel), 30)
    area1.add_processing_item_path(get_main_recipe(Item.automation_science_pack), 30)

    area3 = world.create_area("Area3")
    area3.inputs.append(area2_iron_plate)
    area3.create_resource(get_main_recipe(Item.iron_ore), 240)
    area3.create_resource(get_main_recipe(Item.copper_ore), 90)
    area3.add_processing_item_path(get_main_recipe(Item.iron_plate), 120)
    area3.add_processing_item_path(get_main_recipe(Item.iron_gear_wheel), 45)
    area3.add_processing_item_path(get_main_recipe(Item.copper_plate), 45)
    area3.add_processing_item_path(get_main_recipe(Item.copper_cable), 45)
    area3.add_processing_item_path(get_main_recipe(Item.electronic_circuit), 30)
    area3.add_processing_item_path(get_main_recipe(Item.inserter), 30)
    area3.add_processing_item_path(get_main_recipe(Item.transport_belt), 15)
    area3.add_processing_item_path(get_main_recipe(Item.logistic_science_pack), 30)

    world.export_factory_blueprint()
