import QtQuick 1.0

Rectangle {
    
    id: map
    
    signal mapClicked (int index);
    
    function resize(width, height) {
        map.width = width * 32
        map.height = height * 32
    }
    
    GridView {
        
        property bool tileSelected: false
        
        id: grid
        anchors.fill: parent
        flow: GridView.TopToBottom
        cellWidth: 32; cellHeight: 32
        interactive: false
        
        model: map_model
        delegate: Tile {}
        MouseArea {
            id: mouse_area
            anchors.fill: parent
            onClicked: {
                if (grid.tileSelected) {
                    grid.currentItem.mouse_enabled = true
                    grid.currentItem.border.width = 0
                    grid.currentItem.border.color = "black"
                } else {
                    grid.tileSelected = true
                }
                grid.currentIndex = grid.indexAt(mouse.x, mouse.y)
                map.mapClicked(grid.currentIndex)
                grid.currentItem.mouse_enabled = false
                grid.currentItem.border.width = 3
                grid.currentItem.border.color = "red"
            }
        }
    }
}
