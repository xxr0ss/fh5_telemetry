# Generated by dev_tool.py

from dataclasses import dataclass
from ctypes import (
    c_uint8, c_uint16, c_uint32, c_uint64,
    c_int8, c_int16, c_int32, c_int64,
    c_float, c_double,
    cast, POINTER, c_buffer, Structure
)
from typing import Any

DATA_SIZE = 324
STRUCT_FMT = '<iIfffffffffffffffffffffffffffiiiiffffffffffffffffffffiiiiiiIIfffffffffffffffffHBBBBBBbbb'

@dataclass
class FH5_Data(Structure):
    """ Data class to store a piece of forza horizon data out """
    _fields_ = [
		('IsRaceOn', c_int32),
		('TimestampMS', c_uint32),
		('EngineMaxRpm', c_float),
		('EngineIdleRpm', c_float),
		('CurrentEngineRpm', c_float),
		('AccelerationX', c_float),
		('AccelerationY', c_float),
		('AccelerationZ', c_float),
		('VelocityX', c_float),
		('VelocityY', c_float),
		('VelocityZ', c_float),
		('AngularVelocityX', c_float),
		('AngularVelocityY', c_float),
		('AngularVelocityZ', c_float),
		('Yaw', c_float),
		('Pitch', c_float),
		('Roll', c_float),
		('NormalizedSuspensionTravelFrontLeft', c_float),
		('NormalizedSuspensionTravelFrontRight', c_float),
		('NormalizedSuspensionTravelRearLeft', c_float),
		('NormalizedSuspensionTravelRearRight', c_float),
		('TireSlipRatioFrontLeft', c_float),
		('TireSlipRatioFrontRight', c_float),
		('TireSlipRatioRearLeft', c_float),
		('TireSlipRatioRearRight', c_float),
		('WheelRotationSpeedFrontLeft', c_float),
		('WheelRotationSpeedFrontRight', c_float),
		('WheelRotationSpeedRearLeft', c_float),
		('WheelRotationSpeedRearRight', c_float),
		('WheelOnRumbleStripFrontLeft', c_int32),
		('WheelOnRumbleStripFrontRight', c_int32),
		('WheelOnRumbleStripRearLeft', c_int32),
		('WheelOnRumbleStripRearRight', c_int32),
		('WheelInPuddleDepthFrontLeft', c_float),
		('WheelInPuddleDepthFrontRight', c_float),
		('WheelInPuddleDepthRearLeft', c_float),
		('WheelInPuddleDepthRearRight', c_float),
		('SurfaceRumbleFrontLeft', c_float),
		('SurfaceRumbleFrontRight', c_float),
		('SurfaceRumbleRearLeft', c_float),
		('SurfaceRumbleRearRight', c_float),
		('TireSlipAngleFrontLeft', c_float),
		('TireSlipAngleFrontRight', c_float),
		('TireSlipAngleRearLeft', c_float),
		('TireSlipAngleRearRight', c_float),
		('TireCombinedSlipFrontLeft', c_float),
		('TireCombinedSlipFrontRight', c_float),
		('TireCombinedSlipRearLeft', c_float),
		('TireCombinedSlipRearRight', c_float),
		('SuspensionTravelMetersFrontLeft', c_float),
		('SuspensionTravelMetersFrontRight', c_float),
		('SuspensionTravelMetersRearLeft', c_float),
		('SuspensionTravelMetersRearRight', c_float),
		('CarOrdinal', c_int32),
		('CarClass', c_int32),
		('CarPerformanceIndex', c_int32),
		('DrivetrainType', c_int32),
		('NumCylinders', c_int32),
		('HorizonPlaceholder0', c_int32),
		('HorizonPlaceholder1', c_uint32),
		('HorizonPlaceholder2', c_uint32),
		('PositionX', c_float),
		('PositionY', c_float),
		('PositionZ', c_float),
		('Speed', c_float),
		('Power', c_float),
		('Torque', c_float),
		('TireTempFrontLeft', c_float),
		('TireTempFrontRight', c_float),
		('TireTempRearLeft', c_float),
		('TireTempRearRight', c_float),
		('Boost', c_float),
		('Fuel', c_float),
		('DistanceTraveled', c_float),
		('BestLap', c_float),
		('LastLap', c_float),
		('CurrentLap', c_float),
		('CurrentRaceTime', c_float),
		('LapNumber', c_uint16),
		('RacePosition', c_uint8),
		('Accel', c_uint8),
		('Brake', c_uint8),
		('Clutch', c_uint8),
		('HandBrake', c_uint8),
		('Gear', c_uint8),
		('Steer', c_int8),
		('NormalizedDrivingLine', c_int8),
		('NormalizedAIBrakeDifference', c_int8)
    ]


class FH5_API:
    def __init__(self, raw_data: bytes=b'') -> None:
        if raw_data==b'':
            raw_data = b'\x00' * DATA_SIZE
        self._fh_data = FH5_Data.from_buffer_copy(raw_data)
    
    @property
    def fh_data(self):
        return self._fh_data
    
    @fh_data.setter
    def fh_data(self, data: bytes | FH5_Data):
        if isinstance(data, bytes):
            self._fh_data = FH5_Data.from_buffer_copy(data)
        else:
            self._fh_data = data
