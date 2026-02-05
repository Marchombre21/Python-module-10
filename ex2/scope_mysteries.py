# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    scope_mysteries.py                                 :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: bfitte <bfitte@student.42lyon.fr>          +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/02/04 10:12:07 by bfitte            #+#    #+#             #
#    Updated: 2026/02/04 10:12:08 by bfitte           ###   ########lyon.fr   #
#                                                                             #
# ****************************************************************************#

from typing import Callable


def mage_counter() -> Callable:
    count: int = 0

    def counter_function() -> Callable:
        nonlocal count
        count += 1
        return count
    return counter_function


def spell_accumulator(initial_power: int) -> Callable:
    power: int = initial_power

    def add_power(value: int) -> Callable:
        nonlocal power
        power += value
        return power
    return add_power


def enchantment_factory(enchantment_type: str) -> Callable:

    def apply_enchantments(word: str) -> str:
        return enchantment_type + " " + word
    return apply_enchantments


def memory_vault() -> dict[str, Callable]:
    stored_values: dict = {}

    def store(key: str, value: int):
        stored_values[key] = value
        return stored_values

    # Apparently I have to maintain private memory storage
    def recall(key: str):
        return stored_values.get(key, "Memory not found")
    return {"store": store, "recall": recall}


def main():
    mage_function = mage_counter()
    spell_function = spell_accumulator(5)
    for n in range(5):
        print("Mage:", mage_function())
        print("Spell:", spell_function(n))
    frozen = enchantment_factory("Frozen")
    fire = enchantment_factory("Fire")
    earth = enchantment_factory("Earth")
    print(frozen("Hammer"))
    print(fire("Sword"))
    print(earth("Stone"))
    dict_functions = memory_vault()
    dict_functions["store"]("ok", 1)
    dict_functions["store"]("ko", 5)
    dict_functions["store"]("un", 59)
    print(dict_functions["recall"]("un"))
    print(dict_functions["recall"]("deux"))
    dict_functions["store"]("deux", 41)
    print(dict_functions["recall"]("deux"))
    dict_functions["store"]("un", 69)
    print(dict_functions["recall"]("un"))


if __name__ == "__main__":
    main()
