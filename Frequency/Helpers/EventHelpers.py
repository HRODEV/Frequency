import pygame


def EventExist(eventList, eventType):
    for event in eventList:
        if event.type == eventType:
            return True
    return False