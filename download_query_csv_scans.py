import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import argparse


class DownloadFromCSV(object):
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.df = pd.read_csv(self.csv_pth)

    def read_csv(self):
        pass

    def download(self):
        pass


def main():
    csv_path = '/Users/itamartsayag/workspace/tasks/jog_mode_enabelment/viz_etl.csv'
    dwn = DownloadFromCSV(csv_path)

if __name__ == '__main__':
    main()
