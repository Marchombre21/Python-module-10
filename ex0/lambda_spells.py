# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    lambda_spells.py                                   :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: bfitte <bfitte@student.42lyon.fr>          +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/02/03 15:54:09 by bfitte            #+#    #+#             #
#    Updated: 2026/02/03 15:54:10 by bfitte           ###   ########lyon.fr   #
#                                                                             #
# ****************************************************************************#

def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: "*" + x + "*", spells))


def mage_stats(mages: list[dict]) -> dict:
    powers: list = [mage["power"] for mage in mages]
    return {'max_power': (lambda x: max(x))(powers),
            'min_power': (lambda x: min(x))(powers),
            'avg_power': round(sum(powers) / len(powers), 2)}


def main():
    artifacts = [
        {'name': 'Ice Wand', 'power': 104, 'type': 'armor'},
        {'name': 'Lightning Rod', 'power': 67, 'type': 'relic'},
        {'name': 'Ice Wand', 'power': 77, 'type': 'armor'},
        {'name': 'Water Chalice', 'power': 91, 'type': 'accessory'}
        ]
    mages = [
        {'name': 'Storm', 'power': 88, 'element': 'ice'},
        {'name': 'Luna', 'power': 72, 'element': 'earth'},
        {'name': 'Riley', 'power': 79, 'element': 'light'},
        {'name': 'Ember', 'power': 94, 'element': 'ice'},
        {'name': 'Riley', 'power': 91, 'element': 'lightning'}
        ]
    spells = ['darkness', 'flash', 'earthquake', 'fireball']
    print("\nArtifact:", artifact_sorter(artifacts))
    print()
    print("power:", power_filter(mages, 80))
    print()
    print("spell:", spell_transformer(spells))
    print()
    print("mage:", mage_stats(mages))


if __name__ == "__main__":
    main()
