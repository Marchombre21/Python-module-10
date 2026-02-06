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
    """nonlocal is necessary for all non-mutable variables. When the variable
    is stored in cell object in __closure__ variable and it has to be modified,
    with nonlocal, Python understand that it have to modify the value inside
    existing cell in __closure__ and reassign the variable name to the new
    created value.
    """
    count: int = 0

    def counter_function() -> int:
        nonlocal count
        count += 1
        return count
    return counter_function


def spell_accumulator(initial_power: int) -> Callable:
    power: int = initial_power

    def add_power(value: int) -> int:
        nonlocal power
        power += value
        return power
    return add_power


def enchantment_factory(enchantment_type: str) -> Callable:

    def apply_enchantments(word: str) -> str:
        return enchantment_type + " " + word
    return apply_enchantments


def memory_vault() -> dict[str, Callable]:
    """When memory_vault function finish, its attributes (stored_values) are
    stored in __closure__ variable  of returned closures.
    So they can access to these variables even after function is closed.
    """
    stored_values: dict = {}

    def store(key: str, value: int) -> None:
        stored_values[key] = value

    def recall(key: str) -> int | str:
        return stored_values.get(key, "Memory not found")
    return {"store": store, "recall": recall}


def main():

    # Test two first functions
    print("="*60)
    mage_function = mage_counter()
    spell_function = spell_accumulator(5)
    for n in range(5):
        print("Mage:", mage_function())
        print("Spell:", spell_function(n))
    print()

    # Test enchantments factory
    print("="*60)
    frozen = enchantment_factory("Frozen")
    fire = enchantment_factory("Fire")
    earth = enchantment_factory("Earth")
    print(frozen("Hammer"))
    print(fire("Sword"))
    print(earth("Stone"))
    print()

    # Test stored functions
    print("="*60)
    dict_functions = memory_vault()
    # I store three keys/values
    dict_functions["store"]("ok", 1)
    dict_functions["store"]("ko", 5)
    dict_functions["store"]("un", 59)
    print(dict_functions["recall"]("un"))
    # I try to get an unknow key
    print(dict_functions["recall"]("deux"))
    # I store this key and try to recall it
    dict_functions["store"]("deux", 41)
    print(dict_functions["recall"]("deux"))
    # I change the value of an existing key
    dict_functions["store"]("un", 69)
    print(dict_functions["recall"]("un"))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
