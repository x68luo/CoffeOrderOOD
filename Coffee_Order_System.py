from typing import Dict, List
from abc import ABC, abstractmethod


class Coffee(ABC):
    @abstractmethod
    def cost(self) -> int: pass

    @abstractmethod
    def describe(self) -> str: pass


class AddonDecorator(Coffee):
    def __init__(self, coffee: Coffee) -> None:
        self._coffee = coffee


class Latte(Coffee):
    SHOT_PRICE: Dict[int, float] = {1: 2.0, 2: 3.0, 3: 3.5}

    def __init__(self, shots: int = 1) -> None:
        self.shots = shots

    def cost(self) -> float:
        return self.SHOT_PRICE[self.shots]

    def describe(self) -> str:
        return f"Latte ({self.shots} shot)"


# ----- Milk -----
class MilkRegular(AddonDecorator):
    def cost(self) -> float:
        return self._coffee.cost()

    def describe(self) -> str:
        return self._coffee.describe() + ", Milk: Regular"


class MilkOat(AddonDecorator):
    def cost(self) -> float:
        return self._coffee.cost() + 1.0

    def describe(self) -> str:
        return self._coffee.describe() + ", Milk: Oat"


class MilkAlmond(AddonDecorator):
    def cost(self) -> float:
        return self._coffee.cost() + 1.25

    def describe(self) -> str:
        return self._coffee.describe() + ", Milk: Almond"

# --- Syrup-----


class SyrupVanilla(AddonDecorator):
    def cost(self) -> float:
        return self._coffee.cost() + 0.10

    def describe(self) -> str:
        return self._coffee.describe() + ", Syrup: Vanilla"


class SyrupChocolate(AddonDecorator):
    def cost(self) -> float:
        return self._coffee.cost() + 0.10

    def describe(self) -> str:
        return self._coffee.describe() + ", Syrup: Chocolate"


class SyrupCaramel(AddonDecorator):
    def cost(self) -> float:
        return self._coffee.cost() + 0.15

    def describe(self) -> str:
        return self._coffee.describe() + ", Syrup: Caramel"


class SyrupLavender(AddonDecorator):
    def cost(self) -> float:
        return self._coffee.cost() + 0.15

    def describe(self) -> str:
        return self._coffee.describe() + ", Syrup: Lavender"

# --- Spice ---


class SpiceNutmeg(AddonDecorator):
    def cost(self) -> float:
        return self._coffee.cost() + 0.15

    def describe(self) -> str:
        return self._coffee.describe() + ", Spice: Nutmeg"


class SpiceCinnamon(AddonDecorator):
    def cost(self) -> float:
        return self._coffee.cost() + 0.10

    def describe(self) -> str:
        return self._coffee.describe() + ", Spice: Cinnamon"

# --- Size ---


class SizeSmall(AddonDecorator):
    FACTOR = 0.75

    def cost(self) -> float:
        return round(self._coffee.cost() * self.FACTOR, 2)

    def describe(self) -> str:
        return self._coffee.describe() + ", Size: Small"


class SizeMedium(AddonDecorator):
    FACTOR = 1.0

    def cost(self) -> float:
        return round(self._coffee.cost() * self.FACTOR, 2)

    def describe(self) -> str:
        return self._coffee.describe() + ", Size: Medium"


class SizeLarge(AddonDecorator):
    FACTOR = 1.25

    def cost(self) -> float:
        return round(self._coffee.cost() * self.FACTOR, 2)

    def describe(self) -> str:
        return self._coffee.describe() + ", Size: Large"


class CoffeeOrderSystem:
    _counter = 1000  # order number

    def __init__(self) -> None:
        self._orders: Dict[int, Coffee] = {}

    def place_order(self, coffee: Coffee) -> int:
        CoffeeOrderSystem._counter += 1
        oid = CoffeeOrderSystem._counter
        self._orders[oid] = coffee
        return oid

    def show_detail(self, order_num: int) -> None:
        coffee = self._orders[order_num]
        print(f"Order {order_num}: {coffee.describe()} -> ${coffee.cost():.2f}")


if __name__ == "__main__":
    # 2 shot Latte + Oat Milk + Caramel Syrup + Cinnamon Spice，Large
    drink = SizeLarge(SpiceCinnamon(SyrupCaramel(MilkOat(Latte(shots=2)))))

    print(drink.describe())
    print(f"Price: ${drink.cost():.2f}")  # Price: $5.31

    system = CoffeeOrderSystem()
    order_id = system.place_order(drink)
    system.show_detail(order_id)
