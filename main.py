from factorio_design_tool import Item, Language, World, get_main_recipe

if __name__ == "__main__":
    world = World(Language.japanese)

    area1 = world.create_area("area1")
    area1_resource_iron_ore = area1.create_resource(get_main_recipe(Item.iron_ore), 70)
    area1_resource_copper_ore = area1.create_resource(get_main_recipe(Item.copper_ore), 20)
    area1_resource_coal = area1.create_resource(get_main_recipe(Item.coal), 10)
    area1.set_processing_line(get_main_recipe(Item.iron_plate), 60)
    area1.set_processing_line(get_main_recipe(Item.iron_stick), 30)
    area1.set_processing_line(get_main_recipe(Item.iron_gear_wheel), 15)

    area2 = world.create_area("area2")
    area2_resource_copper_ore = area2.create_resource(get_main_recipe(Item.copper_ore), 30)

    area3 = world.create_area("area3")
    area3_resource_copper_ore = area3.create_resource(get_main_recipe(Item.copper_ore), 30)

    area1.inputs.append(area2_resource_copper_ore)
    area1.set_processing_line(get_main_recipe(Item.copper_plate), 30)
    world.export_factory_blueprint()
