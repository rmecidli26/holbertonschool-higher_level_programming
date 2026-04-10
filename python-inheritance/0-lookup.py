#!/usr/bin/python3
"""
Bu modul obyektlərin atributlarını və metodlarını
axtarmaq üçün funksiyanı ehtiva edir.
"""


def lookup(obj):
    """Obyektin mövcud atribut və metodlarının siyahısını qaytarır"""
    return dir(obj)
