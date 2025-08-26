class Pet:
    # pass
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []  # track all pet instances

    def __init__(self, name: str, pet_type: str, owner=None):
        if not isinstance(name, str) or not name.strip():
            raise Exception("Pet name must be a non-empty string")
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type. Must be one of {Pet.PET_TYPES}")
        if owner is not None and not isinstance(owner, Owner):
            raise Exception("Owner must be an instance of Owner or None")

        self._name = name.strip()
        self._pet_type = pet_type
        self._owner = owner
        Pet.all.append(self)

    @property
    def name(self):
        return self._name

    @property
    def pet_type(self):
        return self._pet_type

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        if not isinstance(value, Owner):
            raise Exception("Owner must be an instance of Owner")
        self._owner = value

    def __repr__(self):
        return f"Pet(name='{self.name}', pet_type='{self.pet_type}', owner={self.owner.name if self.owner else None})"

class Owner:
    # pass
    def __init__(self, name: str):
        if not isinstance(name, str) or not name.strip():
            raise Exception("Owner name must be a non-empty string")
        self._name = name.strip()

    @property
    def name(self):
        return self._name

    def pets(self):
        """Return all pets that belong to this owner"""
        return [pet for pet in Pet.all if pet.owner is self]

    def add_pet(self, pet):
        """Add a pet to this owner"""
        if not isinstance(pet, Pet):
            raise Exception("Argument must be an instance of Pet")
        pet.owner = self  # assign ownership

    def get_sorted_pets(self):
        """Return a sorted list of this owner's pets by their names"""
        return sorted(self.pets(), key=lambda pet: pet.name)

    def __repr__(self):
        return f"Owner(name='{self.name}')"
