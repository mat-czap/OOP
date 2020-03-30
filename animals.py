from dataclasses import dataclass
from typing import List, Dict
from typing_extensions import Protocol
import pprint


@dataclass
class GeneralInfo:
    name: str
    animal_type: str
    species: str
    mass: str


@dataclass
class AnimalRecord:
    general_info: GeneralInfo
    additional_info: str


# Interface for class instances
class IAnimal(Protocol):
    def get_mass(self) -> int: pass

    def get_species(self) -> str: pass

    def get_special(self) -> str: pass

    def get_name(self) -> str: pass

# Abstract class
class Animals:
    def __init__(self, animal_record: AnimalRecord):
        self.name = animal_record.general_info.name
        self.animal_type = animal_record.general_info.animal_type
        self.species = animal_record.general_info.species
        self.mass = int(animal_record.general_info.mass)

    def __repr__(self):
        return f'animal {self.name}'

    def get_mass(self) -> int:
        return self.mass

    def get_species(self) -> str:
        return self.species

    def get_name(self) -> str:
        return self.name


class Reptiles(Animals):
    def __init__(self, animal_record: AnimalRecord):
        super().__init__(animal_record)
        self.isVen: bool = True if animal_record.additional_info == "Venomous" else False

    def get_special(self) -> str:
        return f"isVen: {str(self.isVen)}"


class Mammals(Animals):
    def __init__(self, animal_record: AnimalRecord):
        super().__init__(animal_record)
        self.LitterSize: int = int(animal_record.additional_info)

    def get_special(self) -> str:
        return f"LitterSize: {str(self.LitterSize)}"


class Birds(Animals):
    def __init__(self, animal_record: AnimalRecord):
        super().__init__(animal_record)
        self.wingspan: int = int(animal_record.additional_info[0])
        self.isTalk: bool = True if animal_record.additional_info[1] == "Talks" else False

    def get_special(self) -> str:
        return f"Wingspan: {str(self.wingspan)}, isTalk: {str(self.isTalk)}"


# class Birds(Animals):
#     def __init__(self, line):
#         super().__init__(line)
#         self.wingspan: int = False
#         self.TalksOrMute = False

with open("animalsData.txt") as data:
    lines = [line.rstrip() for line in data.readlines()]
    print(lines)
    newList: List[AnimalRecord] = []
    for index in range(0, len(lines) - 1, 2):
        newList.append(AnimalRecord(GeneralInfo(*lines[index].split(" ")), lines[index + 1]))


# animals_obj =[]
# for x in newList:
#     animals_obj.append(Animals(x[0]))
#
# for Animal_properties in newList:
#     line = Animal_properties.general_info.split(" ")
#     spice = line[1]
#     print(spice)


# print(animals_obj[0])

def Factory(el: AnimalRecord) -> IAnimal:
    if el.general_info.animal_type == "Mammal":
        return Mammals(el)
    if el.general_info.animal_type == "Reptile":
        return Reptiles(el)
    if el.general_info.animal_type == "Bird":
        return Birds(el)


name_to_animal: Dict[str, IAnimal] = {}
for line in newList:
    new_animal_instance = Factory(line)
    name_to_animal[new_animal_instance.get_name()] = new_animal_instance

pprint.pprint(name_to_animal)

# names = [name for name in name_to_animal.keys()]
# pprint.pprint(names)
#
# name = input(f"pass the name of animal {list(name_to_animal.keys())}:\n")
# requestedAnimal = name_to_animal[name]
# print(requestedAnimal)
# method = input("pass the method:\n")


# print(requestedAnimal)

test_list = [x for x in range(10)]
print(test_list[::-2])
