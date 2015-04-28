import QtQuick 1.0

Rectangle {
    property alias mouse_enabled: mouse_area.enabled
    
    id: tile
    
    width: 32; height: 32
    
    color: model.color
    
    Image {
        id: tile_image
        source: model.tile
        anchors.fill: parent
        fillMode: Image.PreserveAspectFit
    }
    
    MouseArea {
        id: mouse_area
        anchors.fill: parent
        hoverEnabled: true
        onEntered: tile.border.width = 2
        onExited: tile.border.width = 0
    }
}