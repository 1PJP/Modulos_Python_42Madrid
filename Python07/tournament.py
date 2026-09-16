import ex0
import ex1
import ex2


def battle(opponents: list[tuple[ex0.CreatureFactory,
                                 ex2.BattleStrategy]]) -> None:
    len_op = len(opponents)
    try:
        print("*** Tournament ***")
        print(f"{len_op} opponents involved")
        for i in range(len_op):
            for j in range(i + 1, len_op):
                factory_one, strategy_one = opponents[i]
                factory_two, strategy_two = opponents[j]

                creature_one = factory_one.create_base()
                creature_two = factory_two.create_base()
                print()
                print("* Battle *")

                print(creature_one.describe())
                print(" vs.")
                print(creature_two.describe())
                print(" now fight!")

                actions_one = strategy_one.act(creature_one)
                actions_two = strategy_two.act(creature_two)

                for action in actions_one:
                    print(action)

                for action in actions_two:
                    print(action)
    except ex2.InvalidStrategy as e:
        print(f"Battle error, aborting tournament: {e}")


def main() -> None:
    aqua_factory = ex0.AquaFactory()
    flame_factory = ex0.FlameFactory()
    healing_factory = ex1.HealingCreatureFactory()
    transforming_factory = ex1.TransformCreatureFactory()
    normal_strategy = ex2.NormalStrategy()
    aggressive_strategy = ex2.AggressiveStrategy()
    defensive_strategy = ex2.DefensiveStrategy()

    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    opponents_one = [
        (flame_factory, normal_strategy),
        (healing_factory, defensive_strategy)
        ]
    battle(opponents_one)
    print()

    print("Tournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    opponents_two = [
        (flame_factory, aggressive_strategy),
        (healing_factory, defensive_strategy)
    ]
    battle(opponents_two)
    print()

    print("Tournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    opponents_three = [
        (aqua_factory, normal_strategy),
        (healing_factory, defensive_strategy),
        (transforming_factory, aggressive_strategy)
    ]
    battle(opponents_three)


if __name__ == "__main__":
    main()
