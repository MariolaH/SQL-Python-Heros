  SELECT name, about_me, biography, name.ability_types
        from heroes
        join ability_types
            on heroes.id = ability_types.id 