# Componente base
class Pizza:
    """
    Classe base abstrata para todos os tipos de pizza.
    """

    def _init_(self):
        pass

    def get_description(self) -> str:
        """
        Retorna a descrição da pizza.
        """
        raise NotImplementedError("Método não implementado")

    def cost(self) -> float:
        """
        Retorna o custo da pizza.
        """
        raise NotImplementedError("Método não implementado")


# Implementação concreta do componente base
class PlainPizza(Pizza):
    """
    Implementação concreta de uma pizza simples.
    """

    def _init_(self):
        super()._init_()

    def get_description(self) -> str:
        return "Massa da pizza"

    def cost(self) -> float:
        return 5.00  # Preço base


# Decorator base
class PizzaDecorator(Pizza):
    """
    Decorator base para pizzas, que permite adicionar ingredientes dinamicamente.
    """

    def _init_(self, pizza: Pizza):
        super()._init_()
        self._pizza = pizza

    def get_description(self) -> str:
        raise NotImplementedError("Método não implementado")

    def cost(self) -> float:
        raise NotImplementedError("Método não implementado")


# Implementações concretas dos decorators
class Cheese(PizzaDecorator):
    """
    Decorator para adicionar queijo à pizza.
    """

    def _init_(self, pizza: Pizza):
        super()._init_(pizza)

    def get_description(self) -> str:
        return self._pizza.get_description() + ", Cheese"

    def cost(self) -> float:
        return self._pizza.cost() + 1.25


class Pepperoni(PizzaDecorator):
    """
    Decorator para adicionar pepperoni à pizza.
    """

    def _init_(self, pizza: Pizza):
        super()._init_(pizza)

    def get_description(self) -> str:
        return self._pizza.get_description() + ", Pepperoni"

    def cost(self) -> float:
        return self._pizza.cost() + 1.50


class Olives(PizzaDecorator):
    """
    Decorator para adicionar azeitonas à pizza.
    """

    def _init_(self, pizza: Pizza):
        super()._init_(pizza)

    def get_description(self) -> str:
        return self._pizza.get_description() + ", Olives"

    def cost(self) -> float:
        return self._pizza.cost() + 0.75


class Ham(PizzaDecorator):
    """
    Decorator para adicionar presunto à pizza.
    """

    def _init_(self, pizza: Pizza):
        super()._init_(pizza)

    def get_description(self) -> str:
        return self._pizza.get_description() + ", Presunto"

    def cost(self) -> float:
        return self._pizza.cost() + 1.00


# Exemplo de uso
if _name_ == "_main_":
    pizza = PlainPizza()
    print(f"{pizza.get_description()} - ${pizza.cost():.2f}")

    pizza = Cheese(pizza)
    print(f"{pizza.get_description()} - ${pizza.cost():.2f}")

    pizza = Pepperoni(pizza)
    print(f"{pizza.get_description()} - ${pizza.cost():.2f}")

    pizza = Olives(pizza)
    print(f"{pizza.get_description()} - ${pizza.cost():.2f}")

    pizza = Ham(pizza)
    print(f"{pizza.get_description()} - ${pizza.cost():.2f}")
