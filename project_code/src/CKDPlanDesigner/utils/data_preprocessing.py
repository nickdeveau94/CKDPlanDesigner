
import pandas as pd
import os


def preprocess_synthea_data(synthea_path):
    cond_df = pd.read_csv(os.path.join(synthea_path, 'conditions.csv'))
    depressions_desc = [val for val in set(cond_df.DESCRIPTION) if 'depr' in val]
    ht_desc = [val for val in set(cond_df.DESCRIPTION) if 'Hypertension' in val]
    bmi_desc = [val for val in set(cond_df.DESCRIPTION) if 'Body mass index' in val]
    diabet_desc = [val for val in set(cond_df.DESCRIPTION) if 'diabet' in val]

    cond_sel_vals = depressions_desc + \
                    ht_desc + \
                    bmi_desc + \
                    diabet_desc

    sel_cond_df = cond_df[cond_df.DESCRIPTION.isin(cond_sel_vals)]
    sel_cond_df['VALUE'] = 1
    sel_cond_df = sel_cond_df[['PATIENT', 'DESCRIPTION', 'VALUE']]
    cond_df_wide = pd.pivot(sel_cond_df, index='PATIENT', columns='DESCRIPTION', values='VALUE').fillna(0).reset_index()

    obs_df = pd.read_csv('../bmi210Project_data/synthea_data/observations.csv')
    smoking_desc  = [val for val in set(obs_df['DESCRIPTION']) if 'smok' in val]

    sel_obs_df = obs_df[obs_df.DESCRIPTION.isin(smoking_desc)].sort_values('DATE').drop_duplicates('PATIENT', keep='last')
    smoking_df = sel_obs_df[['PATIENT', 'DESCRIPTION', 'VALUE']]
    smoking_df_wide = pd.pivot(smoking_df, index='PATIENT', columns='DESCRIPTION', values='VALUE').fillna(0).reset_index()

    smoking_mapping = {'Never smoker': 0,
                       'Former smoker': 1,
                       'Current every day smoker': 1}

    smoking_df_wide['Tobacco smoking status NHIS'] = smoking_df_wide['Tobacco smoking status NHIS'].map(smoking_mapping)

    patients_df = pd.read_csv(os.path.join(synthea_path, 'patients.csv'))
    obs_df = pd.read_csv(os.path.join(synthea_path, 'observations.csv'))

    # uncomment for all observation types
    # set(pd.read_csv('synthea_data/observations.csv').DESCRIPTION.values)

    kidney_obs = obs_df[obs_df['DESCRIPTION'] == 'Glomerular filtration rate/1.73 sq M.predicted']
    kidney_obs = kidney_obs[['DATE', 'PATIENT', 'DESCRIPTION', 'VALUE', 'UNITS']].sort_values('DATE').drop_duplicates('PATIENT', keep='last')
    gfr_df = pd.pivot(kidney_obs, index='PATIENT', columns='DESCRIPTION', values='VALUE').reset_index()
    px_df = patients_df.merge(gfr_df, left_on='Id', right_on='PATIENT')

    sel_cols = ['Id',
     'BIRTHDATE',
     'RACE',
     'ETHNICITY',
     'GENDER',
     'ZIP',
     'Glomerular filtration rate/1.73 sq M.predicted']

    col_names = ['Id',
     'BIRTHDATE',
     'RACE',
     'ETHNICITY',
     'GENDER',
     'ZIP',
     'eGFR']

    px_df = px_df[sel_cols]
    px_df.columns = col_names
    px_df['eGFR'] = px_df.eGFR.astype(float)

    tmp = px_df.merge(cond_df_wide, how='left', left_on='Id', right_on='PATIENT').drop('Id', 1)
    # tmp = tmp.merge(obs_df_wide, how='left', on='PATIENT')
    tmp = tmp.merge(smoking_df_wide, how='left', on='PATIENT')

    diabetes_indicator = tmp[diabet_desc].max(axis=1)
    depression_indicator = tmp[depressions_desc].max(axis=1)
    bmi_indicator = tmp[bmi_desc].max(axis=1)
    ht_indicator = tmp[ht_desc].max(axis=1)
    smoking_indicator = tmp[smoking_desc].max(axis=1)
    # smoking_indicator = tmp[smoking_desc].max(axis=1)

    final_df = pd.concat([tmp.PATIENT,
                          diabetes_indicator,
                          depression_indicator,
                          bmi_indicator,
                          ht_indicator,
                          smoking_indicator], axis=1)
    final_df.columns = ['PATIENT',
                        'diabetes',
                        'depression',
                        'bmi',
                        'ht',
                        'smoking']

    final_df = final_df.merge(px_df, how='left', left_on='PATIENT', right_on='Id')
    final_df = final_df[[col for col in final_df.columns if col != 'Id']]
    final_df.columns = ['patient_id',
                        't2d',
                        'depression',
                        'bmi',
                        'hypertension',
                        'smoking',
                        'dob',
                        'race',
                        'ethnicity',
                        'gender',
                        'zip',
                        'eGFR']
    final_df['t2d'] = final_df['t2d'].astype(bool)
    final_df['depression'] = final_df['depression'].astype(bool)
    final_df['bmi'] = final_df['bmi'].astype(bool)
    final_df['hypertension'] = final_df['hypertension'].astype(bool)
    final_df['smoking'] = final_df['smoking'].astype(bool)
    
    return final_df