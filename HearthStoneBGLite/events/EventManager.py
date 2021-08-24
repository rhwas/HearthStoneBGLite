import pygame
from typing import Callable, Dict, List
from .EventEnums import EventEnums

class EventManager():
    # The subscribers dictionary is a hash list, whose keys are contant game event variables, of hash lists,
    # whose keys are random keys created by the subscriber so that they can unsubscribe, if need be.
    __subscribers: Dict[EventEnums, List[Callable[[any, float], None]]] = { enum.value : [] for enum in EventEnums }

    # Adds a listener to the subscribers dictionary and returns it's index
    def subscribe(self, event: EventEnums, listener: Callable[[any, float], None]) -> int:
        self.__subscribers[event.value].append(listener)
        # print(self.__subscribers)
        # print('***********************************************')
        return len(self.__subscribers) - 1

    # removes a listener from the subscribers
    def unsubscribe(self, event: EventEnums, listener: Callable[[any, float], None]):
        self.__subscribers[event.value].remove(listener)
        # print(self.__subscribers)
        # print('***********************************************')

    # calls all listeners
    def processEvents(self, events, dt: float):
        for event in events:    
            try:
                for listener in self.__subscribers[event.type]:
                    listener(event, dt)
            except KeyError:
                self.__subscribers[event.type] = []