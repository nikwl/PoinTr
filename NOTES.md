export PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python 

# train
./scripts/train.sh 1 --config cfgs/BrokenObjects/a1-jars-a3.yaml --exp_name exp --val_freq 1000
./scripts/test.sh 1 --config cfgs/BrokenObjects/a1-jars-a3.yaml --exp_name exp --ckpts experiments/a1-jars-a3/BrokenObjects/exp/ckpt-epoch-200.pth

./scripts/train.sh 2 --config cfgs/BrokenObjects/a2-bottles-a3.yaml --exp_name exp --val_freq 1000
./scripts/test.sh 2 --config cfgs/BrokenObjects/a2-bottles-a3.yaml --exp_name exp --ckpts experiments/a2-bottles-a3/BrokenObjects/exp/ckpt-epoch-200.pth

./scripts/train.sh 2 --config cfgs/BrokenObjects/a3-mugs-a3.yaml --exp_name exp --val_freq 1000
./scripts/test.sh 2 --config cfgs/BrokenObjects/a3-mugs-a3.yaml --exp_name exp --ckpts experiments/a3-mugs-a3/BrokenObjects/exp/ckpt-epoch-200.pth

./scripts/train.sh 1 --config cfgs/BrokenObjects/a5-airplanes-a3.yaml --exp_name exp --val_freq 1000
./scripts/test.sh 1 --config cfgs/BrokenObjects/a5-airplanes-a3.yaml --exp_name exp --ckpts experiments/a5-airplanes-a3/BrokenObjects/exp/ckpt-epoch-200.pth

./scripts/train.sh 1 --config cfgs/BrokenObjects/a6-chairs-a3.yaml --exp_name exp --val_freq 1000
./scripts/test.sh 1 --config cfgs/BrokenObjects/a6-chairs-a3.yaml --exp_name exp --ckpts experiments/a6-chairs-a3/BrokenObjects/exp/ckpt-epoch-200.pth

./scripts/train.sh 2 --config cfgs/BrokenObjects/a7-cars-a3.yaml --exp_name exp --val_freq 1000
./scripts/test.sh 2 --config cfgs/BrokenObjects/a7-cars-a3.yaml --exp_name exp --ckpts experiments/a7-cars-a3/BrokenObjects/exp/ckpt-epoch-200.pth

./scripts/train.sh 2 --config cfgs/BrokenObjects/a8-tables-a3.yaml --exp_name exp --val_freq 1000
./scripts/test.sh 2 --config cfgs/BrokenObjects/a8-tables-a3.yaml --exp_name exp --ckpts experiments/a8-tables-a3/BrokenObjects/exp/ckpt-epoch-200.pth

./scripts/train.sh 2 --config cfgs/BrokenObjects/a9-sofas-a3.yaml --exp_name exp --val_freq 1000
./scripts/test.sh 2 --config cfgs/BrokenObjects/a9-sofas-a3.yaml --exp_name exp --ckpts experiments/a9-sofas-a3/BrokenObjects/exp/ckpt-epoch-200.pth
