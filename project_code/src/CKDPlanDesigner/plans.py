from CKDPlanDesigner import interventions as ix


#### CAREPLANS ####
class Careplan(object):
    def __init__(self,
                 patient_config: dict=None,
                 physio_components: list=[],
                 demo_components: list=[],
                 behavior_components: list=[]):
        
        self.patient_config = patient_config

        self.physio_components = physio_components
        self.demo_components = demo_components
        self.behavior_components = behavior_components
        self.consolidate_components()

        if patient_config.get('race') != 'white':
            self.demo_components.append(ix.AdditionalTimeHealthEquity())

        self.savings = 1

    def consolidate_components(self):
        self.all_components = self.physio_components + \
                              self.demo_components +  \
                              self.behavior_components
        
    def list_components(self):
        self.consolidate_components()
        return [comp for comp in self.all_components]
        
    def get_savings(self):
        for comp in self.components:
            self.savings *= comp.est_savings
        return self.savings
    
class DelayPlan(Careplan):
    def __init__(self, patient_config):
        print('instantiating delay plan')
        super().__init__(patient_config)

        self.name = 'Delay'

        if patient_config.get('hypertension'):
            self.physio_components.append(ix.Hypertension())
        if patient_config.get('t2d'):
            self.physio_components.append(ix.Type2D()) 

        if patient_config.get('depression'):
            self.behavior_components.append(ix.DepressionTreatment())
        if patient_config.get('bmi'):
            self.behavior_components.append(ix.DietaryProgram())

        self.consolidate_components()

class PrepTransitionPlan(Careplan):
    def __init__(self):
        super().__init__(patient_config,
                    physio_components=[ix.Hypertension(), ix.Type2D()],
                    behavior_components=[ix.DDiet(), 
                                        ix.NutritionSupplementation()])
        
        
        self.name = 'PrepTransition'
        
class ESRDPlan(Careplan):
    def __init__(self):
        super().__init__()
        self.components = [None]
        self.name = 'EndOfLife'