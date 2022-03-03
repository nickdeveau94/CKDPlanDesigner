class RiskFactor(object):
    def __init__(self, name):
        self.name = name

  
#### BEHAVIORAL RISK FACTORS ######    
class BehavioralRiskFactor(RiskFactor):
    def __init__(self, name):
        super().__init__(name)
        
class Depression(BehavioralRiskFactor):
    def __init__(self, name):
        super().__init__(name)
        
class EngagedWithNephro(BehavioralRiskFactor):
    def __init__(self, name):
        super().__init__(name)
        
class PoorDiet(BehavioralRiskFactor):
    def __init__(self, name):
        super().__init__(name)
        
        
#### DEMOGRAPHIC RISK FACTORS ######    
class DemographicRiskFactor(RiskFactor):
    def __init__(self, name):
        super().__init__(name)
        
class CKDLiterate(DemographicRiskFactor):
    def __init__(self, name):
        super().__init__(name)
        
class Race(DemographicRiskFactor):
    def __init__(self, name):
        super().__init__(name)
        
        
#### PHYSIO RISK FACTORS ######
class PhysioRiskFactor(RiskFactor):
    def __init__(self, name):
        super().__init__(name)
        
class Diabetes(PhysioRiskFactor):
    def __init__(self, name):
        super().__init__(name)

class eGFR(PhysioRiskFactor):
    def __init__(self, name):
        super().__init__(name)

class Hypertension(PhysioRiskFactor):
    def __init__(self, name):
        super().__init__(name)
        
class Malnourished(PhysioRiskFactor):
    def __init__(self, name):
        super().__init__(name)
        
class Obesity(PhysioRiskFactor):
    def __init__(self, name):
        super().__init__(name)
        
class Smoking(PhysioRiskFactor):
    def __init__(self, name):
        super().__init__(name)