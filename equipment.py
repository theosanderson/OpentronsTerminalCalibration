
from opentrons import robot, containers, instruments

def getEquipment():
        equipment={}

        #DECK:
        equipment['trash']=containers.load('point', "C1","trash")
        equipment['p200rack'] = containers.load('tiprack-200ul', 'E2', 'tiprack200')
        equipment['p1000rack'] = containers.load('tiprack-1000ul', 'A1', 'tiprack1000')
        equipment['TubMedia']=containers.load('epmotion30', "D1","TubMedia")


        #PIPETTE(S)
        equipment['p1000'] = instruments.Pipette(
            name="P1000",
            axis="b",
            min_volume=20,
            max_volume=1000,
            tip_racks=[equipment['p1000rack']],
            trash_container=equipment['trash']
        )


        equipment['p200x8'] = instruments.Pipette(
            name="p200x8",
            axis="a",
            min_volume=20,
            max_volume=200,
            trash_container=equipment['trash'],
            channels=8
        )
        return(equipment)


