from controller import Robot, DistanceSensor, Motor
MAX_SPEED = 4
robot = Robot()
ps = []
for i in range(8):
    ps.append(robot.getDevice(f"ps{str(i)}"))
    ps[i].enable(64)
leftMotor = robot.getDevice('left wheel motor')
rightMotor = robot.getDevice('right wheel motor')
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))
leftMotor.setVelocity(0.0)
rightMotor.setVelocity(0.0)
while (robot.step(64) != -1):
    if (ps[7].getValue() > 80):
        leftSpeed = MAX_SPEED
        rightSpeed = -MAX_SPEED
    else:
        if (ps[5].getValue() > 80):
            leftSpeed = MAX_SPEED
            rightSpeed = MAX_SPEED
        else:
            leftSpeed = (MAX_SPEED/8)
            rightSpeed = MAX_SPEED
        if (ps[6].getValue() > 80):
            leftSpeed = MAX_SPEED
            rightSpeed = (MAX_SPEED/8)
    leftMotor.setVelocity(leftSpeed)
    rightMotor.setVelocity(rightSpeed)