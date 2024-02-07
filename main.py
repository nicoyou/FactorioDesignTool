from factorio_design_tool import Item, Language, World

if __name__ == "__main__":
    world = World(Language.japanese)

    area1 = world.create_area("area1")
    area1_resource_iron_ore = area1.create_resource(Item.iron_ore, 70)
    area1_resource_copper_ore = area1.create_resource(Item.copper_ore, 20)
    area1_resource_coal = area1.create_resource(Item.coal, 10)

    area2 = world.create_area("area2")
    area2_resource_iron_ore = area2.create_resource(Item.copper_ore, 30)

    world.export_factory_blueprint()
