# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    functools_artifacts.py                             :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: bfitte <bfitte@student.42lyon.fr>          +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/02/04 13:32:37 by bfitte            #+#    #+#             #
#    Updated: 2026/02/04 13:32:38 by bfitte           ###   ########lyon.fr   #
#                                                                             #
# ****************************************************************************#

import operator
from time import time
from functools import (
    reduce,
    partial,
    lru_cache,
    singledispatch
)
from typing import Callable


def spell_reducer(spells: list[int], operation: str) -> int:
    """Reducer tool is used to apply a function of two arguments to the
    elements of an iterable. At the end, it will reduce the iterable to a
    single value.

    Returns:
        int: A single value, result of iteration through elements of iterable.
    """
    match operation:
        case "add":
            return reduce(operator.add, spells, 0)
        case "multiply":
            return reduce(operator.mul, spells)
        case "max":
            return reduce(max, spells)
        case "min":
            return reduce(min, spells)


def base_enchantment(power: int, element: str, target: str):
    return {"Power": power, "Element": element, "target": target}


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    """A partial is an callable object. When called, works like the function
    passed as first parameter at the creation of the object.At the creation
    we can 'pre-pass' some arguments to 'register' them in partial.
    """
    fire = partial(base_enchantment, 50, "fire")
    ice = partial(base_enchantment, 50, "ice")
    lightning = partial(base_enchantment, 50, "lightning")
    return {"fire_enchant": fire, "ice_enchant": ice,
            "lightning_enchant": lightning}


@lru_cache(maxsize=128)
def memoized_fibonacci(n: int) -> int:
    """The lru_cache decorator (Least Recently Used) store the results of the
    called function in order to recover them if the same function is called
    with the exact same args. It avoids the calculation process and saves time.
    If the maxsize isn't None, the cache will can contain maximum maxsize
    results. After that it will remove from cache the leastest recently used
    result.
    """
    if n < 2:
        return n
    return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)


def memoized_fibonacci_no_lru(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci_no_lru(n-1) + memoized_fibonacci_no_lru(n-2)


def spell_dispatcher() -> Callable:
    """The singledispatch decorator transforms a function into a generic
    function, which can have different behaviours depending upon the type of
    its first argument. The register() attribute of the generic function is a
    decorator, taking a type parameter and decorating a function implementing
    the operation for that type.
    """
    @singledispatch
    def cast_spell(spell) -> str | int:
        return "Unknow type spell"

    @cast_spell.register(int)
    def _(spell) -> int:
        return spell * 2

    @cast_spell.register(str)
    def _(spell) -> str:
        return f"The enchantment is {spell}"

    @cast_spell.register(list)
    def _(spells) -> str:
        results: list = list(map(cast_spell, spells))
        return f"The list of results is {results}"
    return cast_spell


def main():
    # Spell reducer tests
    print("="*60)
    print(spell_reducer(range(5), "add"))
    print(spell_reducer(range(2, 5), "multiply"))
    print(spell_reducer(range(5), "max"))
    print(spell_reducer(range(5), "min"))
    print()

    # Partial function tests
    print("="*60)
    dictionnary: dict = partial_enchanter(base_enchantment)
    print(dictionnary.get("fire_enchant")("plant"))
    print(dictionnary.get("ice_enchant")("dragon"))
    print(dictionnary.get("lightning_enchant")("darkness"))
    print()

    # lru_cache tests
    print("="*60)
    start_time: float = time()
    print(f"{memoized_fibonacci(30)} ", end="")
    end_time: float = time()
    print(f"LRU time: {end_time - start_time}")
    print(memoized_fibonacci.cache_info())
    start_time: float = time()
    print(f"{memoized_fibonacci_no_lru(30)} ", end="")
    end_time: float = time()
    print(f"No LRU time: {end_time - start_time}")
    print()

    # single_dispatch tests
    print("="*60)
    dispatcher: Callable = spell_dispatcher()
    print("dispatch int:", dispatcher(15))
    print("dispatch str:", dispatcher("I'm an enchantment"))
    list_spells: list = [25, "truc", 2, "Le dernier"]
    print("dispatch list:", dispatcher(list_spells))
    print("unregistered type:", dispatcher({"type": "dictionnary"}))
    print()


if __name__ == "__main__":
    main()
