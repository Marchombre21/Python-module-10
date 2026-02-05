# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    higher_magic.py                                    :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: bfitte <bfitte@student.42lyon.fr>          +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/02/04 07:45:46 by bfitte            #+#    #+#             #
#    Updated: 2026/02/04 07:45:47 by bfitte           ###   ########lyon.fr   #
#                                                                             #
# ****************************************************************************#

from typing import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    return lambda x: (spell1(x), spell2(x))


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    return lambda x: base_spell(x) * multiplier


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    return lambda x: spell(x) if condition(x) else\
            "Spell fizzled"


def spell_sequence(spells: list[Callable]) -> Callable:
    return lambda x: [spell(x) for spell in spells]


def plus_one(arg: int) -> int:
    return arg + 1


def minus_two(arg: int) -> int:
    return arg - 2


def conditional_function(arg: int) -> bool:
    return arg < 100


def main():
    combined_function: Callable = spell_combiner(plus_one, minus_two)
    print("Combined result:", combined_function(5))
    amplifier: Callable = power_amplifier(plus_one, 3)
    print("Amplifier result:", amplifier(5))
    conditional: Callable = conditional_caster(conditional_function, minus_two)
    print("Conditional result:", conditional(105))
    spell_list: list[Callable] = [combined_function, amplifier, conditional]
    sequence: Callable = spell_sequence(spell_list)
    print("Sequence result:", sequence(5))


if __name__ == "__main__":
    main()
