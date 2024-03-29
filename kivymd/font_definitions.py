"""
Themes/Font definitions
=======================

.. seealso::

   `Material Design spec, The type system <https://material.io/design/typography/the-type-system.html>`_
"""

from kivy.core.text import LabelBase
from kivy.metrics import sp

from kivymd import fonts_path

fonts = [
    {
        "name": "OPPOSans",
        "fn_regular": fonts_path + "OPPOSans-Regular.ttf",
        "fn_bold": fonts_path + "OPPOSans-Bold.ttf",
        "fn_italic": fonts_path + "OPPOSans-Regular.ttf",
        "fn_bolditalic": fonts_path + "OPPOSans20-Bold.ttf",
    },
    {
        "name": "OPPOSansThin",
        "fn_regular": fonts_path + "OPPOSans20-Light.ttf",
        "fn_italic": fonts_path + "OPPOSans20-Light.ttf",
    },
    {
        "name": "OPPOSansLight",
        "fn_regular": fonts_path + "OPPOSans20-Light.ttf",
        "fn_italic": fonts_path + "OPPOSans20-Light.ttf",
    },
    {
        "name": "OPPOSansMedium",
        "fn_regular": fonts_path + "OPPOSans-Medium.ttf",
        "fn_italic": fonts_path + "OPPOSans-Medium.ttf",
    },
    {
        "name": "OPPOSansBlack",
        "fn_regular": fonts_path + "OPPOSans-Regular.ttf",
        "fn_italic": fonts_path + "OPPOSans-Regular.ttf",
    },
    {
        "name": "Icons",
        "fn_regular": fonts_path + "materialdesignicons-webfont.ttf",
    },
]

for font in fonts:
    LabelBase.register(**font)

# TODO: Add `weight` properties.
theme_font_styles = {
    "Icon": {
        "large": {
            "line-height": 1,
            "font-name": "Icons",
            "font-size": sp(24),
        },
    },
    "Display": {
        "large": {
            "line-height": 1.64,
            "font-name": "OPPOSans",
            "font-size": sp(57),
        },
        "medium": {
            "line-height": 1.52,
            "font-name": "OPPOSans",
            "font-size": sp(45),
        },
        "small": {
            "line-height": 1.44,
            "font-name": "OPPOSans",
            "font-size": sp(36),
        },
    },
    "Headline": {
        "large": {
            "line-height": 1.40,
            "font-name": "OPPOSans",
            "font-size": sp(32),
        },
        "medium": {
            "line-height": 1.36,
            "font-name": "OPPOSans",
            "font-size": sp(28),
        },
        "small": {
            "line-height": 1.32,
            "font-name": "OPPOSans",
            "font-size": sp(24),
        },
    },
    "Title": {
        "large": {
            "line-height": 1.28,
            "font-name": "OPPOSans",
            "font-size": sp(22),
        },
        "medium": {
            "line-height": 1.24,
            "font-name": "OPPOSans",
            "font-size": sp(16),
        },
        "small": {
            "line-height": 1.20,
            "font-name": "OPPOSans",
            "font-size": sp(14),
        },
    },
    "Body": {
        "large": {
            "line-height": 1.24,
            "font-name": "OPPOSans",
            "font-size": sp(16),
        },
        "medium": {
            "line-height": 1.20,
            "font-name": "OPPOSans",
            "font-size": sp(14),
        },
        "small": {
            "line-height": 1.16,
            "font-name": "OPPOSans",
            "font-size": sp(12),
        },
    },
    "Label": {
        "large": {
            "line-height": 1.20,
            "font-name": "OPPOSans",
            "font-size": sp(14),
        },
        "medium": {
            "line-height": 1.16,
            "font-name": "OPPOSans",
            "font-size": sp(12),
        },
        "small": {
            "line-height": 1.16,
            "font-name": "OPPOSans",
            "font-size": sp(11),
        },
    },
}
"""
.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/label-font-style-preview.png
    :align: center
"""
