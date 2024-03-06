class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.budget = budget
        self.animal_capacity = animal_capacity
        self.workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price: int) -> str:
        if self.animal_capacity > len(self.animals):
            if self.budget < price:
                return "Not enough budget"
            self.animals.append(animal)
            self.budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        return f"Not enough space for animal"

    def hire_worker(self, worker) -> str:
        if self.workers_capacity > len(self.workers):
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
        total_salary = 0
        for worker in self.workers:
            total_salary += worker.salary

        if self.budget >= total_salary:
            self.budget -= total_salary
            return f"You payed your workers. They are happy. Budget left: {self.budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        total_tend = 0
        for animal in self.animals:
            total_tend += animal.money_for_care

        if total_tend <= self.budget:
            self.budget -= total_tend
            return f"You tended all the animals. They are happy. Budget left: {self.budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int) -> None:
        self.budget += amount

    def animals_status(self) -> str:
        lions_data = '\n'.join(animal.__repr__ for animal in self.animals if animal == "Lion")
        tigers_data = '\n'.join(animal.__repr__ for animal in self.animals if animal == 'Tiger')
        cheetahs_data = '\n'.join(animal.__repr__ for animal in self.animals if animal == 'Cheetah')

        return f"You have {len(self.animals)} animals\n" \
               f"----- {len([animal for animal in self.animals if animal.__class__.__name__ == 'Lion'])} Lions:\n" \
               f"{lions_data}\n" \
               f"----- {len([animal for animal in self.animals if animal.__class__.__name__ == 'Tiger'])} Tigers:\n" \
               f"{tigers_data}\n" \
               f"----- {len([animal for animal in self.animals if animal.__class__.__name__ == 'Cheetah'])} Cheetahs:\n" \
               f"{cheetahs_data}\n"

    def workers_status(self) -> str:
        caretakers_data = [worker for worker in self.workers if worker.__class__.__name__ == 'Caretaker']
        keepers_data = [worker for worker in self.workers if worker.__class__.__name__ == 'Keeper']
        vets_data = [worker for worker in self.workers if worker.__class__.__name__ == 'Vet']

        keepers_result = "\n".join(keeper for keeper in self.workers if keeper.__class__.__name__ == 'Keeper')
        return f"You have {len(self.animals)} animals\n" \
               f"----- {len(keepers_data)} Keepers:\n" \
               f"{keepers_result}" \
               f"----- {len(caretakers_data)} Caretakers:\n" \
               f"" \
               f"----- {len(vets_data)} Vets:\n" \
               f""
