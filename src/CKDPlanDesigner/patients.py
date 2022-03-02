class Patient(object):
    def __init__(self,
                 patient_id: str,
                 eGFR: float,
                 dob: str=None,
                 dod: str=None,
                 ethnicity: str=None,
                 race: str=None,
                 gender: str=None,
                 zipcode: str=None):
        
        self.patient_id = patient_id
        
        self.eGFR = eGFR
        self.assign_stage()
        
        self.careplan = None
        self.low_SES = False

    def assign_stage(self):
        if self.eGFR < 15:
            self.ckd_stage = 5
        elif self.eGFR <= 29:
            self.ckd_stage = 4
        elif self.eGFR <= 44:
            self.ckd_stage = 3.5
        elif self.eGFR <= 59:
            self.ckd_stage = 3
        elif self.eGFR <= 89:
            self.ckd_stage = 2
        
    def generate_careplan(self, plan: Careplan=None):
        if self.ckd_stage <= 3:
            self.careplan = DelayPlan()
        elif self.ckd_stage <= 4:
            self.careplan = PrepTransitionPlan()
        elif self.ckd_stage <= 5:
            self.careplan = ESRDPlan()
            
    def describe_plan_components(self):
        return [comp.desc for comp in self.careplan.components]   
