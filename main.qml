import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
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
            update_accel_break_display()
        }
        RowLayout {
            spacing: 20
            Column {
                width: 400
                spacing: 15
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

            Row {
                id: accel_brake_display
                spacing: 10

                Column{
                    width: 70
                    Label {
                        id: brake_display
                        text: 'Brake: NaN'
                    }
                    Item{
                        anchors.horizontalCenter: parent.horizontalCenter
                        anchors.top: parent.bottom
                        Rectangle {
                            id: brake_display_background
                            width: 10
                            height: 180
                            radius: 5
                            z: 0
                            color: "#DDD"
                        }
                        Rectangle {
                            anchors.bottom: brake_display_background.bottom
                            height: brake_display_background.height * mybackend.fh5_data['Brake'] / 255
                            radius: brake_display_background.radius
                            width: brake_display_background.width
                            z: brake_display_background.z + 1
                            color: "#d45a5a"
                        }
                    }
                }

                Column{
                    width: 70
                    Label {
                        id: accel_display
                        text: 'Accel: NaN'
                    }
                    Item{
                        anchors.horizontalCenter: parent.horizontalCenter
                        anchors.top: parent.bottom
                        Rectangle {
                            id: accel_display_background
                            width: 10
                            height: 180
                            radius: 5
                            z: 0
                            color: "#DDD"
                        }
                        Rectangle {
                            anchors.bottom: accel_display_background.bottom
                            height: accel_display_background.height * mybackend.fh5_data['Accel'] / 255
                            radius: accel_display_background.radius
                            width: accel_display_background.width
                            z: accel_display_background.z + 1
                            color: "#5a95d4"
                        }
                    }
                }
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

        function update_accel_break_display() {
            var accel = mybackend.fh5_data['Accel']
            var brake = mybackend.fh5_data['Brake']
            accel_display.text = `Accel: ${accel}`
            brake_display.text = `Brake: ${brake}`
        }

    }
}