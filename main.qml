import QtQuick
import QtQuick.Controls
import BackendPlugin


ApplicationWindow {
    visible: true
    
    width: 600
    height: 400

    Backend {
        id: mybackend
        Column {
            Label {
                text: `Speed: ${Math.round(mybackend.fh5_data['Speed'])} km/h`
            }
            Label {
                text: `Gear: ${mybackend.fh5_data['Gear']}`
            }
            Label {
                text: `Engine: ${Math.round(mybackend.fh5_data['CurrentEngineRpm'])}/${Math.round(mybackend.fh5_data['EngineMaxRpm'])}`
            }
        }
    }
}