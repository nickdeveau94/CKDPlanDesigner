import yaml
import pathlib
import os

from CKDPlanDesigner.models import interventions as ix

yaml_path = os.path.join(pathlib.Path(__file__).parent.absolute(),
                         '../configs/ix_config.yaml')
ix_config_yaml = open(yaml_path)
ix_config = yaml.load(ix_config_yaml, Loader=yaml.FullLoader)

#### CAREPLANS ####
class CareManagementPlan(object):
    """
    Base care management plan object. Interventions are categorized as either
    physiological, demographic or behavioral and are automatically added to the
    plan object based off of specific dimensions of a patient record.

    """
    def __init__(self, patient_config: dict):
        """
        Args:
            patient_config [dict] : dictonary containing information necessary
            for intervention selection.
        """

    # def __init__(self, patient_config: dict):
        
        self.patient_config = patient_config

        self.physio_components = []
        self.demo_components = []
        self.behavior_components = []

        if self.patient_config.get('race') != 'white':
            self.demo_components.append(ix.AdditionalTimeHealthEquity())

        self.savings = 1

    def consolidate_components(self):
        """
        Combines all interventions into a complete and unified set of 
        interventions.
        """
        self.all_components = []
        self.all_components = self.physio_components + \
                              self.demo_components +  \
                              self.behavior_components
        
    def list_components(self, show_savings=True):
        self.consolidate_components()

        print('Plan Components')
        if show_savings:
            return [(comp.desc, 'Cost Reduction: {}'.format(comp.est_savings))
                    for comp in self.all_components]
        else:
            return [comp.desc for comp in self.all_components]


    def get_savings(self):
        for comp in self.all_components:
            self.savings *= comp.est_savings
        return self.savings
    
class EarlyDelayPlan(CareManagementPlan):
    def __init__(self, patient_config):
        super().__init__(patient_config=patient_config)

        self.plan_name = 'Plan: Delay'

        if self.patient_config.get('hypertension'):
            self.physio_components.append(ix.Hypertension())
        if self.patient_config.get('t2d'):
            self.physio_components.append(ix.Type2D()) 

        if self.patient_config.get('depression'):
            self.behavior_components.append(ix.DepressionTreatment())
        if self.patient_config.get('bmi'):
            self.behavior_components.append(ix.DietaryProgram())

            # pulls in user-configurable content contained within ix_config.yaml
            educate_content = ix_config['desc_long']['educate_engage']['delay_plan']
            self.behavior_components.append(ix.EducationEngagement(desc_long=educate_content))

        self.consolidate_components()

class PrepTransitionPlan(CareManagementPlan):
    def __init__(self, patient_config):
        super().__init__(patient_config)
        
        self.plan_name = 'Plan: Prep Transition'
        if self.patient_config.get('eGFR') <= 20 :
            self.physio_components.append(ix.VascularAccess())
            self.physio_components.append(ix.Peritoneal()) # either this or hemo
            self.physio_components.append(ix.Hemodialysis()) # either this or peri
        
        educate_content = ix_config['desc_long']['educate_engage']['transition_plan']
        self.behavior_components.append(ix.EducationEngagement(desc_long=educate_content))

        nephro_content = ix_config['desc_long']['nephro_engage']['transition_plan']
        self.behavior_components.append(ix.NephroEngagement(desc_long=nephro_content))

        self.consolidate_components()
        
class SmartDialysisPlan(CareManagementPlan):
    def __init__(self, patient_config):
        super().__init__(patient_config)
        self.plan_name = 'Plan: Smart Dialysis'

        self.physio_components.append(ix.Dialysis())
        educate_content = ix_config['desc_long']['educate_engage']['smart_dialysis_plan']
        self.behavior_components.append(ix.EducationEngagement(desc_long=educate_content))

        nephro_content = ix_config['desc_long']['nephro_engage']['smart_dialysis_plan']
        self.behavior_components.append(ix.NephroEngagement(desc_long=nephro_content))

class PalliativeCarePlan(CareManagementPlan):
    def __init__(self, patient_config):
        super().__init__(patient_config)
        self.plan_name = 'Plan: Palliative Care'

        self.physio_components.append(ix.ComfortAndPain())