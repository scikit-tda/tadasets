class RotationAngleNotInRangeError(Exception):
    def __init__(self, angle, min_angle, max_angle, message="Angle {angle} not in range. Angle should be in the range {min_angle} <= angle <= {max_angle}"):
        self.angle = angle
        self.min_angle = min_angle
        self.max_angle = max_angle
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message.format(angle=self.angle, min_angle=self.min_angle, max_angle=self.max_angle)

class NotImplementedError(Exception):
    def __init__(self,message="Error: This part has not been implemented yet. "):
        self.message = message
        super().__init__(self.message)
