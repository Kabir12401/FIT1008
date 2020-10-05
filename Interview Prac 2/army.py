"""
The below is created for the creation of an army elements. It has the Soldier, Archer and cavalry classes that inherit from a 
a fighter class with the abstract method defend.


"""

__author__ = "Ashwin Sarith"


# implemented classes and their methods below here
from abc import ABC, abstractmethod


class Fighter(ABC):
    # Initialised common values for the subclasses
    experience = 0
    damage = 0
    life = 0 

    def __init__(self, life: int, experience: int):
        """ Initialise life and experience of the fighter in 
        
        :pre: life and experience must be >= 0 
        :return: None
        """
        self.life = life
        self.experience = experience
        assert self.life >= 0 , " life cant be negative"
        assert self.experience >= 0 , "experience cant be negative"
           

    
    def is_alive(self):
        """  Checks if the fighter is alive via a boolean 
        :return: Boolean
        :complexity: Best and worst case is both O(1)
        """
        if self.life>0:
            return True 
        return False

    def lose_life(self, lost_life: int):
        """Here health deduction is implemented, lost life will be a result of damage
        
        :param lost_life: life to be deducted from the life of the specific fighter
        :return: None
        """
        self.lost_life = lost_life
        if lost_life<=0:
            raise ValueError("Needs to be a positive value")
        else:
            self.life = self.life - self.lost_life
            
        
    
    def gain_experience(self, gained_experience: int):
        """Unit experience increased  by the value gained_experience

        :pre: gained_experience >= 0
        :post: experience added and greater
        :param gained_experience: The experience to be added to fighter's experience
        :return: the integer value for lifge of the fighter"""
        
        if gained_experience<=0:
            raise ValueError("Experience cannot be negative")
        else:
            self.experience += gained_experience


    def get_life(self):
        """returns the fighters life

        :return: the integer value for life of the fighter"""
        return self.life


    def get_experience(self):
        """returns fighters experience

        :return: the integer value for experience of the fighter"""
        return self.experience

        
    def get_cost(self):
        """returns fighters cost

        :return: the integer value for cost of the fighter"""
        return self.cost

    def get_attack_damage(self):
        """returns attack damage

        :return: the int value for damage with respect to the experience.
        """
        self.damage = 1 + self.experience
        return self.damage
    
    def get_unit_type(self):
        """returns the string unit type
        
        :return: str unit_type
        """
        return self.unit_type 

    @abstractmethod
    def get_speed(self):
        """is an abstract method"""
        pass
    
    @abstractmethod
    def defend(self, damage: int):
        """is an abstract method"""
        pass

    def __str__(self):
        """just for the classes description"""
        val= self.unit_type +"'s life = "+str(self.life)+" and experience = "+str(self.experience)
        return val
        

"======================Soldier====================================="

class Soldier(Fighter):
    unit_type = "Soldier"
    cost = 1
    
    def __init__(self):
        """retrieves init method from Fighter and is initialised with the fighters value
        
        :return: None
        """
        super().__init__(3,0)
    
    def get_speed(self):
        """returns the speed of a soldier with respect to its experience
        
        :returns: integer value for speed
        """
        return 1 + self.experience

    def defend(self, damage: int):
        """ A method to invoke defense with damage as input
        :param damage: is the integer for damage thats inflicted on the unit
        :returns: None
        """
        if damage>self.experience:
           self.life -= 1




"======================Archer====================================="



class Archer(Fighter):

    unit_type = "Archer"
    cost = 2

    def __init__(self):
        """retrieves init method from Fighter and is initialised with the fighters value
        
        :return: None
        """
        super().__init__(3,0)
             
    def get_speed(self):
        """returns the speed of a soldier with respect to its experience
        
        :returns: integer value for speed
        """
        return 3

    def defend(self, damage: int):
        """ A method to invoke defense with damage as input
        :param damage: is the integer for damage thats inflicted on the unit
        :returns: None
        """
        if damage>0:
            self.life -=1



"======================Cavalry====================================="

class Cavalry(Fighter):
    unit_type = "Cavalry"
    cost = 3

    def __init__(self):
        """retrieves init method from Fighter and is initialised with the fighters value
        
        :return: None
        """
        super().__init__(4,0)

    def get_speed(self):
        """returns the speed of a soldier with respect to its experience
        
        :returns: integer value for speed
        """
        return 2

    def get_attack_damage(self):
        """Used to retrieve the attack damage for a class
        :returns: damage scaled to unit experience """
        return (2*self.experience) + 1 

    def defend(self, damage: int):
        if damage>(self.experience)//2:
            self.life -=1
            

# def main():
    #testing speed

    # s1 = Soldier()
    # print(s1.get_attack_damage())
    # s2 = Archer()
    # print(s2.get_attack_damage())
    # s3 = Cavalry()
    # print(s3.get_attack_damage())

    # s1 = Soldier()
    # print(s1.get_life())
    # s2 = Archer()
    # print(s2.get_life())
    # s3 = Cavalry()
    # print(s3.get_life())
    
    # s1 = Soldier()
    # print(s1.get_experience())
    # s2 = Archer()
    # print(s2.get_experience())
    # s3 = Cavalry()
    
    
    # s1 = Soldier()
    # s1.defend(1)
    # print(s1.get_life())
    # print(str(s1))
    
    # s2 = Archer()
    # print(str(s2))

    # s3 = Cavalry()
    # print(str(s3))
    

# if __name__ == "__main__":
#     main()



# Future implmentations

# class Army:


      

    

