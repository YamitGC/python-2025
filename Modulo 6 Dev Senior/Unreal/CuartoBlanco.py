import unreal

# Asegúrate de que el editor de Unreal esté abierto y con un nivel.

# Obtener el mundo actual
world = unreal.get_editor_world()

# Rutas a los Static Meshes básicos de Unreal (pueden variar según la versión)
# Puedes usar un cubo como base y escalarlo
cube_mesh_path = "/Engine/BasicShapes/Cube.Cube"
cube_mesh = unreal.load_asset(cube_mesh_path, unreal.StaticMesh)

if cube_mesh is None:
    print("No se pudo cargar el Static Mesh del cubo. Asegúrate de que la ruta sea correcta.")
else:
    # Crear el suelo
    floor_actor = world.spawn_actor(unreal.StaticMeshActor, unreal.Transform(location=unreal.Vector(0.0, 0.0, -100.0), scale=unreal.Vector(10.0, 10.0, 0.1))) # Z -100 para estar bajo el origen
    floor_actor.set_static_mesh(cube_mesh)
    floor_actor.set_actor_label("Floor")

    # Crear las paredes
    # Pared frontal
    wall_front_actor = world.spawn_actor(unreal.StaticMeshActor, unreal.Transform(location=unreal.Vector(0.0, 500.0, 250.0), scale=unreal.Vector(10.0, 0.1, 5.0)))
    wall_front_actor.set_static_mesh(cube_mesh)
    wall_front_actor.set_actor_label("Wall_Front")

    # Pared trasera
    wall_back_actor = world.spawn_actor(unreal.StaticMeshActor, unreal.Transform(location=unreal.Vector(0.0, -500.0, 250.0), scale=unreal.Vector(10.0, 0.1, 5.0)))
    wall_back_actor.set_static_mesh(cube_mesh)
    wall_back_actor.set_actor_label("Wall_Back")

    # Pared izquierda
    wall_left_actor = world.spawn_actor(unreal.StaticMeshActor, unreal.Transform(location=unreal.Vector(-500.0, 0.0, 250.0), scale=unreal.Vector(0.1, 10.0, 5.0)))
    wall_left_actor.set_static_mesh(cube_mesh)
    wall_left_actor.set_actor_label("Wall_Left")

    # Pared derecha
    wall_right_actor = world.spawn_actor(unreal.StaticMeshActor, unreal.Transform(location=unreal.Vector(500.0, 0.0, 250.0), scale=unreal.Vector(0.1, 10.0, 5.0)))
    wall_right_actor.set_static_mesh(cube_mesh)
    wall_right_actor.set_actor_label("Wall_Right")

    # Techo
    ceiling_actor = world.spawn_actor(unreal.StaticMeshActor, unreal.Transform(location=unreal.Vector(0.0, 0.0, 500.0), scale=unreal.Vector(10.0, 10.0, 0.1)))
    ceiling_actor.set_static_mesh(cube_mesh)
    ceiling_actor.set_actor_label("Ceiling")

    print("Cuarto vacío creado en Unreal Engine con Python.")

# Opcional: Seleccionar los actores creados en el editor
# created_actors = [floor_actor, wall_front_actor, wall_back_actor, wall_left_actor, wall_right_actor, ceiling_actor]
# unreal.EditorLevelLibrary.set_selected_level_actors(created_actors)