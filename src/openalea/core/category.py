# -*- python -*-
#
#       OpenAlea.Core
#
#       Copyright 2006-2008 INRIA - CIRAD - INRA  
#
#       File author(s): Thomas Cokelaer <cokelaer@gmail.fr>
#                       Christophe Pradal <christophe.prada@cirad.fr>
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
# 
#       OpenAlea WebSite : http://openalea.gforge.inria.fr
#
###############################################################################

__doc__="""
This module defines the category keywords to be used within __wralea__.py files
"""

__license__= "Cecill-C"
__revision__=" $Id: pkgmanager.py 1433 2008-11-27 08:52:19Z cokelaer $ "

import openalea

import sys
import os
import glob



###############################################################################

class PackageManagerCategory():
    """
    The PackageManagerCategory is a Dictionary of keywords and categories
    It is used by PackageManager to create the list of category in visualea.
    """

    def __init__ (self):
        """ Constructor """

        self.keywords = { 
            'image':        'proposal.Image Processing.standard', 
            'svg':          'proposal.Image Processing.svg', 
            'datatype':     'proposal.Python Functionalities.Datatype', 
            'type':         'proposal.Python Functionalities.Datatype', 
            'functional':   'proposal.Python Functionalities.functional', 
            'math':         'proposal.Python Functionalities.math', 
            'python':       'proposal.Python Functionalities.standard', 
            'data':         'proposal.Raw Data (txt,geom,png,etc)', 
            'tutorial':     'proposal.Tutorial', 
            'workflow':     'proposal.Workflow', 
            'flow control': 'proposal.Workflow', 
            'system':       'proposal.System Interaction', 
            'io':           'proposal.Data I/O', 
            'file':         'proposal.Data I/O', 
            'test':         'proposal.Test', 
            'misc':         'proposal.Miscellaneous', 
            'plot':         'proposal.Visualisation', 
            'graphics':     'proposal.Visualisation', 
            'graphic':      'proposal.Visualisation', 
            'visualization':'proposal.Visualisation', 
            'visualisation':'proposal.Visualisation', 
            'spatial':      'proposal.Scene Design', 
            'scene':        'proposal.Scene Design', 
            'light':        'proposal.Scene Design', 
            'PGL Object Generator':'proposal.Scene Design', 
            'fractal analysis':'proposal.Fractal Analysis', 
            'demo':         'proposal.Demo', 
            'composite':    'proposal.Composite', 
            'descriptive':  'proposal.Data Processing.statistics', 
            'stat':         'proposal.Data Processing.statistics', 
            'regression':   'proposal.Data Processing.regression', 
            'fitting':      'proposal.Data Processing.fitting', 
            'distribution': 'proposal.Data Processing.distribution', 
            'test':         'proposal.Data Processing.statistical tests', 
            'datamine':     'proposal.Data processing.Data Manipulation and Transformation',
            'codec':        'proposal.Data processing.Data Manipulation and Transformation'}
        