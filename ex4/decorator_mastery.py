# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    decorator_mastery.py                               :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: bfitte <bfitte@student.42lyon.fr>          +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/02/05 10:43:48 by bfitte            #+#    #+#             #
#    Updated: 2026/02/05 10:43:49 by bfitte           ###   ########lyon.fr   #
#                                                                             #
# ****************************************************************************#

from typing import Callable
from functools import wraps
from time import time
from inspect import signature, Signature, BoundArguments


def spell_timer(func: Callable) -> Callable:
    """A custom decorator which will receive the next function as argument when
    interpretor will read it. The interpretor will register a new callable with
    the return which will be called when the function is called. The decorator
    @wraps from functools copy all metadatas from the original function to the
    wrapper (wrapper.__name__ = func.__name__).
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}")
        start_time: float = time()
        result = func(*args, **kwargs)
        end_time: float = time()
        print(f"Spell completed in {end_time - start_time:.2f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    """Signature function from inspect module will return the signature of
    wrapped function (self, spell_name: str, power: int). Bind function will
    test if signature and args match and return an object (BoundArgument)
    (since python 3.9) which has an attribute which is a dict with argument's
    name as key and argument as value.
    Apply_default function get the default values applied and add them to the
    dict (power: int = 10 in signature for example).
    """
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            func_sign: Signature = signature(func)
            sign_dict: BoundArguments = func_sign.bind(*args, **kwargs)
            sign_dict.apply_defaults()
            power: int = sign_dict.arguments.get("power")
            if power >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:

    def retry_decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            for n in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print("Spell failed, retrying..."
                          f" (attempt {n + 1}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return retry_decorator


class MageGuild:
    power_valid: Callable = power_validator(15)
    retry: Callable = retry_spell(5)

    @spell_timer
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) > 2 and all(x.isalpha() or x.isspace() for x in name):
            return True
        return False

    @power_valid
    @retry
    def cast_spell(self, spell_name: str, power: int) -> str:
        if power > 50:
            raise Exception("Just to raise an exception")
        return f"Successfully cast {spell_name} with {power} power"


def main():
    print("="*60)
    print("Henry:", MageGuild.validate_mage_name("Henry"))
    print("he:", MageGuild.validate_mage_name("he"))
    print("Henry Delacroix:", MageGuild.validate_mage_name("Henry Delacroix"))
    print("Henry 2lacroix:", MageGuild.validate_mage_name("Henry 2lacroix"))
    print()

    print("="*60)
    guilde: MageGuild = MageGuild()
    print(guilde.cast_spell("Fireball", 2))
    print(guilde.cast_spell("Fireball", 22))
    print(guilde.cast_spell("Fireball", 54))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
