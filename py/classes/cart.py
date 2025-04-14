from dataclasses import dataclass
from typing import List, Dict
from datetime import date

@dataclass
class Cart:
    cartName : str
    shopLink : str
    stillOpen : bool
    cartOwner : Simp
    cartDateStart : date
    cartDatePlan : date
    cartDateEnd : date
    
    cartItems : Dict[Simp, List[Item]]
    costShipping : float

    def getTotalSimps() -> int:
        return len(cartItems)

    def getAllCost() -> float:
        total = 0.0
        total += costShipping
        for listItem in cartItems:
            for item in listItem:
                total += item.itemPriceSGD
        return total
    
    def getCostPerSimp(simpName : Simp) -> float:
        total = 0.0
        total += costShipping / self.getTotalSimps()
        for item in cartItems[simpName]:
            total += item.itemPriceSGD
        return total

    def closeCart() -> None:
        stillOpen = False
        cartDateEnd = date.today()
