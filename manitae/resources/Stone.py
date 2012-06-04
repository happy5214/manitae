#   Copyright (C) 2012 Alexander Jones
#
#   This file is part of Manitae.
#
#   Manitae is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   Manitae is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with Manitae.  If not, see <http://www.gnu.org/licenses/>.

from manitae.resources.base.PrimitiveResource import PrimitiveResource

class Stone(PrimitiveResource):
    """A :class:`~resources.base.PrimitiveResource.PrimitiveResource` produced by :class:`Units <core.basetypes.Unit.Unit>` such as :class:`~units.StoneGatherer.StoneGatherer`.
    
    Stone is used as a construction material of buildings and :class:`Compound Resources <resources.base.CompoundResource.CompoundResource>` such as :class:`Tools <resources.Tool.Tool>`
    
    This resource type...
    
    * is found natively on most :class:`tiles <maps.MapTile.MapTile>` in finite amounts, depending on the tile's :attr:`~maps.MapTile.MapTile.tile_type`
    """
    
    def __init__(self):
        super(Stone, self).__init__()
