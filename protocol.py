
from opentrons import robot, containers, instruments
from equipment import getEquipment
robot.connect(robot.get_serial_ports_list()[0])
if not robot.is_connected():
        raise Exception('Did not connect')
equipment=getEquipment()

robot.home()
equipment['p1000'].pick_up_tip()
equipment['p1000'].aspirate(500,equipment['TubMedia'])
equipment['p1000'].dispense(500,equipment['CulturePlate'].wells("A1"))
equipment['p1000'].drop_tip()
