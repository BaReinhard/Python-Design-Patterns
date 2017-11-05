"""Create Factorys and Pass to Store to implement the Abstract Factory Design Pattern"""

from abstract_factory.abstract_factory import ComputerFactory, BestBuy, CellFactory

# Create Cell and Computer Factories
factory1 = CellFactory()
factory2 = ComputerFactory()

# Create Stores Holding Cell and Computer Factory
store1 = BestBuy(factory1)
store2 = BestBuy(factory2)

# Display Tech inside the stores
store1.show_tech()
store2.show_tech()
