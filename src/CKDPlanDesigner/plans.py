#### CAREPLANS ####
class Careplan(object):
    def __init__(self,
                 components: list=None,
                 patient=None):
        
        self.components = components
        self.savings = 1
        self.patient = patient
        
    def get_components(self):
        return [comp for comp in self.components]
        
    def get_savings(self):
        for comp in self.components:
            self.savings *= comp.est_savings
        return self.savings
    
            

class DelayPlan(Careplan):
    def __init__(self):
        super().__init__()
        self.components = [InterventionA(),
                           InterventionB()]
        
        self.name = 'Delay'
        
class PrepTransitionPlan(Careplan):
    def __init__(self):
        super().__init__()
        self.components = [InterventionC()]
        
        self.name = 'PrepTransition'
        
class ESRDPlan(Careplan):
    def __init__(self):
        super().__init__()
        self.components = [PalliativeAction1()]
        self.name = 'EndOfLife'


#### PLAN COMPONENTS ####
class Intervention(object):
    def __init__(self,
                 est_savings: float=1,
                 freq='weekly'):
        self.est_savings = est_savings
        self.freq = freq


class DepressionTreatment(Intervention):
    def __init__(self,
                 est_savings: float=.5,
                 freq='daily'):
        super().__init__(est_savings,
                         freq)
        self.desc = 'Depression Treatment'


class Dialysis(Intervention):
    def __init__(self,
                 est_savings: float=.3):
        super().__init__(est_savings)
        self.desc = 'Dialysis'
        
class DietaryProgram(Intervention):
    def __init__(self,
                 est_savings: float=.7):
        super().__init__(est_savings)
        self.desc = 'Dietary Program'
        

class EducationEngagement(Intervention):
    def __init__(self,
                 est_savings: float=1):
        super().__init__(est_savings)
        self.desc = 'Education and Engagement'
        
class WrapAround(Intervention):
    def __init__(self,
                 est_savings: float=1):
        super().__init__(est_savings)
        self.desc = 'High Acuity Wrap-Around Services'
        
class MTM(Intervention):
    def __init__(self,
                 est_savings: float=1):
        super().__init__(est_savings)
        self.desc = 'MTM'
        
class VascularAccess(Intervention):
    def __init__(self,
                 est_savings: float=1):
        super().__init__(est_savings)
        self.desc = 'Vascular Access'