class Animal:
    """
    Represents an animal with a species and name.
    """

    def __init__(self, species, name):
        """
        Initializes an Animal object.

        Args:
            species (str): The species of the animal.
            name (str): The name of the animal.
        """
        self.species = species
        self.name = name


class AnimalShelter:
    """
    Represents an animal shelter that holds dogs and cats using a FIFO approach.
    """

    def __init__(self):
        """
        Initializes an AnimalShelter object.
        """
        self.dog_queue = []
        self.cat_queue = []

    def enqueue(self, animal):
        """
        Adds an animal to the animal shelter.

        Args:
            animal (Animal): The animal to be added to the shelter.
        """
        if animal.species == "dog":
            self.dog_queue.append(animal)
        elif animal.species == "cat":
            self.cat_queue.append(animal)

    def dequeue(self, pref):
        """
        Removes and returns an animal from the animal shelter based on the preference.

        Args:
             The preference for a dog or a cat.

        Returns:
            Animal or None: The dequeued animal matching the preference, or None if no matching animal found.

        """
        if pref == "dog":
            if self.dog_queue:
                return self.dog_queue.pop(0)
        elif pref == "cat":
            if self.cat_queue:
                return self.cat_queue.pop(0)
        return None


# Example usage
shelter = AnimalShelter()
dog1 = Animal("dog", "Buddy")
shelter.enqueue(dog1)

cat1 = Animal("cat", "Whiskers")
shelter.enqueue(cat1)

dog2 = Animal("dog", "Max")
shelter.enqueue(dog2)

pref = "dog"
adopted_dog = shelter.dequeue(pref)
if adopted_dog:
    print(f"Adopted a {adopted_dog.species} named {adopted_dog.name}")
else:
    print("No dogs available ")

pref = "cat"
adopted_cat = shelter.dequeue(pref)
if adopted_cat:
    print(f"Adopted a {adopted_cat.species} named {adopted_cat.name}")
else:
    print("No cats available ")
