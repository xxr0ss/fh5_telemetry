import QtQuick
import QtQuick.Controls
import BackendPlugin


ApplicationWindow {
    visible: true
    
    id: wnd
    width: 600
    height: 400

    Backend {
        anchors.fill: parent
        id: mybackend

        onDataUpdated: {
            update_speed_display()
            update_engine_display()
            update_gear_display()
        }

        Column {
            width: 400
            spacing: 15
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.verticalCenter: parent.verticalCenter
            Label {
                id: speed_display
                text: 'Speed: NaN'
            }
            Item {
                id: engine_display
                property var cur_rpm: 0.0
                property var max_rpm: 0.0
                width: 400
                height: 30
                Rectangle {
                    id: engine_display_foreground
                    height: parent.height
                    radius: engine_display_background.radius
                    width: engine_display.cur_rpm / engine_display.max_rpm * parent.width
                    z: engine_display_background.z + 1
                    color: "blue"
                }
                Rectangle {
                    id: engine_display_background
                    width: parent.width
                    height: parent.height
                    radius: 5
                    z: 0
                    color: "#DDD"
                }
                Label {
                    anchors.horizontalCenter: parent.horizontalCenter
                    anchors.verticalCenter: parent.verticalCenter
                    z: engine_display_foreground.z + 2
                    text: `${engine_display.cur_rpm} / ${engine_display.max_rpm} `
                }
            }
            Label {
                id: gear_display
                text: 'Gear: NaN'
            }
        }


        function update_speed_display() {
            var speed_ms = mybackend.fh5_data['Speed']
            var speed_kmh = speed_ms * 3.6
            speed_display.text = `Speed: ${Math.round(speed_kmh)} km/h`
        }

        function update_engine_display() {
            engine_display.cur_rpm = Math.round(mybackend.fh5_data['CurrentEngineRpm'])
            engine_display.max_rpm = Math.round(mybackend.fh5_data['EngineMaxRpm'])
            var ratio = engine_display.cur_rpm / engine_display.max_rpm
            engine_display_foreground.color = Qt.rgba(ratio * ratio, 0.4 - ratio * ratio * 0.2, 0.1, 1)
        }

        function update_gear_display() {
            var gear = mybackend.fh5_data['Gear']
            var gear_name
            if (gear == 0)
                gear_name = 'R'
            else if(gear == -1)
                gear_name = 'N'
            else
                gear_name = gear.toString()

            gear_display.text = `Gear: ${gear_name}`
        }

    }
}