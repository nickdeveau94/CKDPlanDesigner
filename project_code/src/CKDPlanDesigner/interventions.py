import yaml
import pathlib
import os

yaml_path = os.path.join(pathlib.Path(__file__).parent.absolute(),
                         'configs/ix_config.yaml')

ix_config_yaml = open(yaml_path)
ix_config = yaml.load(ix_config_yaml, Loader=yaml.FullLoader)

#### PLAN COMPONENTS ####
class Intervention(object):
    def __init__(self,
                 est_savings: float=1,
                 freq='weekly'):
        self.est_savings = est_savings
        self.freq = freq


class DepressionTreatment(Intervention):
    def __init__(self,
                 est_savings: float=ix_config['savings'].get('depression', 1),
                 freq='daily'):
        super().__init__(est_savings,
                         freq)
        self.desc = 'Depression Treatment'


##### DIALYSIS #####
class Dialysis(Intervention):
    def __init__(self,
                 est_savings: float=ix_config['savings'].get('dialysis', 1)):
        super().__init__(est_savings)
        self.desc = 'Dialysis'

class Hemodialysis(Dialysis):
    def __init__(self,
                 est_savings: float=ix_config['savings'].get('hemodialysis', 1)):
        super().__init__(est_savings)
        self.desc = 'Hemodialysis'

class Peritoneal(Dialysis):
    def __init__(self,
                 est_savings: float=ix_config['savings'].get('peritoneal', 1)):
        super().__init__(est_savings)
        self.desc = 'Peritoneal Dialysis'


 ##### Dietary Program ######       
class DietaryProgram(Intervention):
    def __init__(self,
                 est_savings: float=.7):
        super().__init__(est_savings)
        self.desc = 'Dietary Program'

class DDiet(DietaryProgram):
    def __init__(self,
                 est_savings: float=ix_config['savings'].get('d-diet', 1)):
        super().__init__(est_savings)
        self.desc = 'D-Diet'

class NutritionSupplementation(DietaryProgram):
    def __init__(self,
                 est_savings: float=ix_config['savings'].get('nutr_supp', 1)):
        super().__init__(est_savings)
        self.desc = 'Nutrition Supplementation'
        
##### Education & Engagement ######  
class EducationEngagement(Intervention):
    def __init__(self,
                 est_savings: float=ix_config['savings'].get('educate_engage', 1)):
        super().__init__(est_savings)
        self.desc = 'Education and Engagement'

class AdditionalTimeHealthEquity(Intervention):
    def __init__(self,
                 est_savings: float=ix_config['savings'].get('equity_time', 1)):
        super().__init__(est_savings)
        self.desc = 'Additional Time - Health Equity'

##### Wrap Around Services ######        
class WrapAround(Intervention):
    def __init__(self,
                 est_savings: float=ix_config['savings'].get('wrap_around', 1)):
        super().__init__(est_savings)
        self.desc = 'High Acuity Wrap-Around Services'

class HomeNursing(WrapAround):
    def __init__(self,
                 est_savings: float=ix_config['savings'].get('home_nursing', 1)):
        super().__init__(est_savings)
        self.desc = 'Home Nursing Care'
        
##### MTM #####
class MTM(Intervention):
    def __init__(self,
                 est_savings: float=1):
        super().__init__(est_savings)
        self.desc = 'MTM'

class Hypertension(MTM):
    def __init__(self,
                 est_savings: float=ix_config['savings'].get('ht', 1)):
        super().__init__(est_savings)
        self.desc = 'Hypertension Management'

class CaSupp(MTM):
    def __init__(self,
                 est_savings: float=ix_config['savings'].get('ca_supp', 1)):
        super().__init__(est_savings)
        self.desc = 'Calcium Supplementation'

class ESA(MTM):
    def __init__(self,
                 est_savings: float=ix_config['savings'].get('esa', 1)):
        super().__init__(est_savings)
        self.desc = 'ESA'

class IronSupp(MTM):
    def __init__(self,
                 est_savings: float=ix_config['savings'].get('iron_supp', 1)):
        super().__init__(est_savings)
        self.desc = 'Iron Supplementation'

class Type2D(MTM):
    def __init__(self,
                 est_savings: float=ix_config['savings'].get('t2d', 1)):
        super().__init__(est_savings)
        self.desc = 'T2D Management'

##### Vascular Access
class VascularAccess(Intervention):
    def __init__(self,
                 est_savings: float=ix_config['savings'].get('vascular_access', 1)):
        super().__init__(est_savings)
        self.desc = 'Vascular Access'