from CKDPlanDesigner.models import stages, plans

class Patient(object):
    """
    Patient object that 1) stores key patient data and 2) contains logic that
    assigns careplans and personalized interventions to a patient.

    """
    def __init__(self, **patient_config):
        """  
        Args:
            eGFR [float] : estimated GFR

            patient_id [str] : unique patient identifier

            depression [bool] : does patient have a current depression diagnosis 

            bmi [bool] : does patient have an obese or higher BMI

            t2d [bool] : does patient have type 2 diabetes

            smoking [bool] : does patient have a history of smoking

            ethniciy [str] : patient's ethnicicty

            race [str] : patient's race

            gender [str] : patient's gender
        """

        self.eGFR = patient_config.get('eGFR')
        self.patient_id = patient_config.get('patient_id')

        self.hypertension = patient_config.get('hypertension')
        self.depression = patient_config.get('depression')
        self.bmi = patient_config.get('bmi')
        self.t2d = patient_config.get('t2d')
        self.smoking = patient_config.get('smoking')
        self.engagement = patient_config.get('engagement')
        self.ethnicity = patient_config.get('ethnicity')
        self.race = patient_config.get('race')
        self.gender = patient_config.get('gender')

        self.patient_config = patient_config
        
        self.assign_stage()
        
        self.careplan = None

    def assign_stage(self):
        """
        Assigns a CKD stage based on eGFR

        """
        if self.eGFR <= 15:
            self.stage = stages.Stage5(self.patient_config)
        elif self.eGFR <= 29:
            self.stage = stages.Stage4(self.patient_config)
        elif self.eGFR <= 44:
            self.stage = stages.Stage3B(self.patient_config)
        elif self.eGFR <= 59:
            self.stage = stages.Stage3A(self.patient_config)
        elif self.eGFR <= 89:
            self.stage = stages.Stage2(self.patient_config)
        elif self.eGFR >= 90:
            self.stage = stages.Stage1(self.patient_config)
        
    def generate_careplan(self):
        """
        Instantiates a careplan on the patient object. The logic that
        personalizes interventions specific to the pattient exists within the
        plan objects in plans.py
        """
        if self.stage.stage_num <= 3:
            self.careplan = plans.EarlyDelayPlan(self.patient_config)
        elif self.stage.stage_num <= 4: # 3.5 = 3b
            self.careplan = plans.PrepTransitionPlan(self.patient_config)
        elif self.stage.stage_num == 5 \
            and self.patient_config['age'] >= 75 \
            and (self.patient_config['hypertension'] or self.patient_config['t2d']):
            self.careplan = plans.PalliativeCarePlan(self.patient_config)
        else:
            self.careplan = plans.SmartDialysisPlan(self.patient_config)
            
    def describe_plan_components(self):
        """
        Returns natural language descriptions of the components in English.
        """
        return [comp.desc for comp in self.careplan.components]   
