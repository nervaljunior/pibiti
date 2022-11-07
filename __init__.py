# -*- coding: utf-8 -*-
"""
/***************************************************************************
 PIBITI
                                 A QGIS plugin
 PLUGIN PIBITI RODA LINK GEOGRAFICO VETORIAL
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2022-11-05
        copyright            : (C) 2022 by NERVAL DE JESUS SANTOS JUNIOR 
        email                : nerval1@hotmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load PIBITI class from file PIBITI.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .PIBITI import PIBITI
    return PIBITI(iface)
