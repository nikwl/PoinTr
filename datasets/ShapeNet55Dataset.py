import os
import torch
import numpy as np
import torch.utils.data as data
from .io import IO
from .build import DATASETS
import logging

@DATASETS.register_module()
class ShapeNet(data.Dataset):
    def __init__(self, config):
        self.data_root = config.DATA_PATH
        # self.pc_path = config.PC_PATH
        self.subset = config.subset
        self.npoints = config.N_POINTS

        if self.subset == "train":
            suffix = "_train.npy"
        else:
            suffix = "_test.npy"

        self.file_list = IO.get(self.data_root + suffix)
        return
        # self.data_list_file = os.path.join(self.data_root, f'{self.subset}.txt')

        # print(f'[DATASET] Open file {self.data_list_file}')
        # with open(self.data_list_file, 'r') as f:
        #     lines = f.readlines()
        
        # self.file_list = []
        # for line in lines:
        #     line = line.strip()
        #     taxonomy_id = line.split('-')[0]
        #     model_id = line.split('-')[1].split('.')[0]
        #     self.file_list.append({
        #         'taxonomy_id': taxonomy_id,
        #         'model_id': model_id,
        #         'file_path': line
        #     })
        # print(f'[DATASET] {len(self.file_list)} instances were loaded')

    def pc_norm(self, pc, pc2):
        """ pc: NxC, return NxC """
        centroid = np.mean(pc, axis=0)
        pc = pc - centroid
        pc2 = pc2 - centroid
        m = np.max(np.sqrt(np.sum(pc**2, axis=1)))
        pc = pc / m
        pc2 = pc2 / m
        return pc, pc2, (centroid, m)

    def un_norm(self, pc, centroid, m):
        pc = pc * m
        pc = pc + centroid
        return pc

    def __getitem__(self, idx):
        # sample = self.file_list[idx]

        # data = IO.get(os.path.join(self.pc_path, sample['file_path'])).astype(np.float32)
        data = self.file_list[idx].astype(np.float32)
        partial, gt = data

        random_indices = np.random.choice(partial.shape[0], size=self.npoints, replace=False)
        partial = partial[random_indices, :]

        gt, partial, tf = self.pc_norm(gt, partial)
        # g = self.un_norm(gt, *tf)

        partial = torch.from_numpy(partial).float()
        gt = torch.from_numpy(gt).float()

        # return sample['taxonomy_id'], sample['model_id'], data
        return "None", "None", (partial, gt, tf)

    def __len__(self):
        return len(self.file_list)