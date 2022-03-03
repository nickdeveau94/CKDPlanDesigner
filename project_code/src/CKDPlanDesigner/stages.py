class CKDStage(object):
    def __init__(self, patient_config: dict, stage_num: float):
        self.stage_num = stage_num
        self.patient_config = patient_config
    
class Stage1(CKDStage):
    def __init__(self, patient_config, stage_num: float=1):
        super().__init__(patient_config, stage_num)
    
class Stage2(CKDStage):
    def __init__(self, patient_config, stage_num: float=2):
        super().__init__(patient_config, stage_num)
    
class Stage3A(CKDStage):
    def __init__(self, patient_config, stage_num: float=3.0):
        super().__init__(patient_config, stage_num)
    
class Stage3B(CKDStage):
    def __init__(self, patient_config, stage_num: float=3.5):
        super().__init__(patient_config, stage_num)
    
class Stage4(CKDStage):
    def __init__(self, patient_config, stage_num: float=4):
        super().__init__(patient_config, stage_num)
    
class Stage5(CKDStage):
    def __init__(self, patient_config, stage_num: float=5):
        super().__init__(patient_config, stage_num)
    