class Employee:
    def __init__(self, name: str, salary: float):
        self._name = name
        self._salary = float(salary)

    @property
    def name(self) -> str:
        return self._name

    @property
    def salary(self) -> float:
        return self._salary

    def increase_salary(self, percent: float) -> None:
        if percent < -100:
            raise ValueError("percent decrease cannot be less than -100")
        self._salary += self._salary * (percent / 100)

    def __str__(self) -> str:
        return f"Employee: {self._name} salary: {self._salary}"


employee1 = Employee("John", 1000)
print(employee1)
employee1.increase_salary(10)

employee2 = Employee("Jane", 1500)
print(employee2)
employee2.increase_salary(10)




