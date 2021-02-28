import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import argparse
import os


class DownloadFromCSV(object):
    def __init__(self, csv_path, output_path):
        self.csv_path = csv_path
        self.output_path = output_path
        self.df = self.read_csv()

    def read_csv(self):
        return pd.read_csv(self.csv_path)

    def download(self, n_rows=3):
        for row in self.df.head(n_rows).iterrows():
            viz_patient_id, study_uid, series_uid = row[1]['viz_patient_id'], row[1]['study_uid'], row[1]['series_uid']
            cmd = self.dwnld_cmd(viz_patient_id, study_uid, series_uid)
            self.exec_cmd(cmd)

    def dwnld_cmd(self, viz_patient_id, study_uid, series_uid):
        cmd = f'aws s3 sync s3://viz-rnd-us-east-2-deidentification-results/production/{viz_patient_id}/{study_uid}/{series_uid}/' \
              f' {os.path.join(self.output_path, viz_patient_id, study_uid, series_uid)}'
        return cmd

    @staticmethod
    def exec_cmd(cmd):
        print(f'Executing: {cmd}')
        os.system(cmd)



def main():
    csv_path = '/Users/itamartsayag/workspace/tasks/jog_mode_enabelment/viz_etl.csv'
    output_path = '/Users/itamartsayag/workspace/data/ctp/dicoms'
    dwn = DownloadFromCSV(csv_path, output_path)
    dwn.download(7)

if __name__ == '__main__':
    main()
