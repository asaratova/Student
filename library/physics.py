"""
Copyright MIT and Harvey Mudd College
MIT License
Summer 2020

Contains the Physics module of the racecar_core library
"""

import abc
import numpy as np
from nptyping import NDArray


class Physics(abc.ABC):
    """
    Returns IMU data on linear acceleration and angular velocity.
    """

    @abc.abstractmethod
    def get_linear_acceleration(self) -> NDArray[3, np.float32]:
        """
        Returns a three element array representing the car's linear acceleration.

        Returns:
            (1D numpy array of 3 floats): The average linear acceleration of the car
            along the (x, y, z) axes during the last frame in m/s^2.

        Example:
            # Initialize accel with the average acceleration over the frame
            accel = rc.physics.get_linear_acceleration()
        """
        pass

    @abc.abstractmethod
    def get_angular_velocity(self) -> NDArray[3, np.float32]:
        """
        Returns a three element array representing the car's angular velocity.

        Returns:
            (1D numpy array of 3 floats): The average angular velocity of the car
            along the (x, y, z) axes during the last frame in rad/s.

        Example:
            # Initialize ang_vel with the average angular velocity over the frame
            ang_vel = rc.physics.get_angular_velocity()
        """
        pass
