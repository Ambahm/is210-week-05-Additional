#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Temprature Conversion
   This program does emperature conversion for Fahrenheit to
   Celsius, Kelvin to Celsius and Kelvin to Fahrenheit.
   This function takes 2 input for tempraturet to be converted.
"""

import decimal

ABS_DIFF = decimal.Decimal('273.15')

def temp_convert(celsius, kelvin):
    """This module returns converted temprature in 3 scales.

    Args:
    celsius(mixed): Celsius to be converted to Fahrenheit
    kelvin(mixed): Kelvin to be converted to Celsius and Fahrenheit

    Returns:
        mixed: Prints converted temprature

    Examples:

        >>> temp_convert(100,373)

        Converted Temprature 
        -------------------------
        CELCIUS TO FAHRENHEIT:212
        KELVIN TO CELCIUS    :99.85
        KELVIN TO FAHRENHEIT :211.73

        >>> temp_convert(0,0)

        Converted Temprature 
        -------------------------
        CELCIUS TO FAHRENHEIT: 32
        KELVIN TO CELCIUS    :-273.15
        KELVIN TO FAHRENHEIT :-459.67

    """

    celsfht = ((decimal.Decimal(celsius) * 9) / 5) + 32

    kelvincels = decimal.Decimal(kelvin) - ABS_DIFF

    kelvinfht = ((decimal.Decimal(kelvincels) * 9) / 5) + 32

    temprature_result = ('\nConverted Temprature \n{}\n{:>2}{:>3}'
                         '\n{:>2}{:>4}\n'
                         '{:>2}{:>6}').format('-'*25,
                                              'CELCIUS_FAHRENHEIT:', celsfht,
                                              'KELVIN_CELCIUS    :', kelvincels,
                                              'KELVIN_FAHRENHEIT :', kelvinfht)
    print temprature_result

