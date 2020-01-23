from python_course.W07.Projectile import *


def getInputs():
    angle = eval(input('Enter the launch angle (in degrees): '))
    velocity = eval(input('Enter the initial velocity (in meters/second): '))
    height = eval(input('Enter the initial height (in meters): '))
    time = eval(input('Enter the time interval (in seconds): '))
    return angle, velocity, height, time


def main():
    angle, velocity, height, time = getInputs()
    shot = Projectile(angle, velocity, height)
    while shot.getY() >= 0:
        shot.update(time)
    print('\nDistance traveled: {x: 0.1f} meters.'.format(x=shot.getX()))


if __name__ == '__main__':
    main()
