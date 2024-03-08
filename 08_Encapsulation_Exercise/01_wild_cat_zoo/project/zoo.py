from typing import List

from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price: int) -> str:
        if self.__animal_capacity > len(self.animals):
            if self.__budget < price:
                return "Not enough budget"
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        return f"Not enough space for animal"

    def hire_worker(self, worker: Worker) -> str:
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name: str) -> str:
        try:
            worker = next(filter(lambda w: w.name == worker_name, self.workers))
        except StopIteration:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(worker)
        return f"{worker_name} fired successfully"

    def pay_workers(self) -> str:
        total_salary = sum([w.salary for w in self.workers])

        if self.__budget >= total_salary:
            self.__budget -= total_salary
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        total_tend = sum([a.money_for_care for a in self.animals])

        if total_tend <= self.__budget:
            self.__budget -= total_tend
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int) -> None:
        self.__budget += amount

    def animals_status(self) -> str:
        result = f"You have {len(self.animals)} animals\n"
        lions = [a for a in self.animals if a.__class__.__name__ == 'Lion']
        result += f"----- {len(lions)} Lions:\n"
        for lion in lions:
            result += f"{lion}\n"

        tigers = [animal for animal in self.animals if animal.__class__.__name__ == 'Tiger']
        result += f"----- {len(tigers)} Tigers:\n"
        for tiger in tigers:
            result += f"{tiger}\n"

        cheetahs = [animal for animal in self.animals if animal.__class__.__name__ == 'Cheetah']
        result += f"----- {len(cheetahs)} Cheetahs:\n"
        for cheetah in cheetahs:
            result += f"{cheetah}\n"

        return result[:-1]

    def workers_status(self) -> str:
        result = f"You have {len(self.workers)} workers\n"
        keepers_data = [worker for worker in self.workers if worker.__class__.__name__ == 'Keeper']
        result += f"----- {len(keepers_data)} Keepers:\n"
        for keeper in keepers_data:
            result += f"{keeper}\n"

        caretakers_data = [worker for worker in self.workers if worker.__class__.__name__ == 'Caretaker']
        result += f"----- {len(caretakers_data)} Caretakers:\n"
        for caretaker in caretakers_data:
            result += f"{caretaker}\n"

        vets_data = [worker for worker in self.workers if worker.__class__.__name__ == 'Vet']
        result += f"----- {len(vets_data)} Vets:\n"
        for vet in vets_data:
            result += f"{vet}\n"

        return result[:-1]
