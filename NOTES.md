export PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python 

# train
./scripts/train.sh \
    1 \
    --config cfgs/BrokenObjects/a1-jars-a2.yaml \
    --exp_name exp \
    --val_freq 1000
./scripts/test.sh \
    1 \
    --config cfgs/BrokenObjects/a1-jars-a2.yaml \
    --exp_name exp \
    --ckpts experiments/a1-jars-a2/BrokenObjects/exp/ckpt-epoch-200.pth

./scripts/train.sh \
    2 \
    --config cfgs/BrokenObjects/a2-bottles-a2.yaml \
    --exp_name exp \
    --val_freq 1000
./scripts/test.sh \
    2 \
    --config cfgs/BrokenObjects/a2-bottles-a2.yaml \
    --exp_name exp \
    --ckpts experiments/a2-bottles-a2/BrokenObjects/exp/ckpt-epoch-200.pth

./scripts/train.sh \
    2 \
    --config cfgs/BrokenObjects/a3-mugs-a2.yaml \
    --exp_name exp \
    --val_freq 1000
./scripts/test.sh \
    2 \
    --config cfgs/BrokenObjects/a3-mugs-a2.yaml \
    --exp_name exp \
    --ckpts experiments/a3-mugs-a2/BrokenObjects/exp/ckpt-epoch-200.pth

./scripts/train.sh \
    1 \
    --config cfgs/BrokenObjects/a5-airplanes-a2.yaml \
    --exp_name exp \
    --val_freq 1000
./scripts/test.sh \
    1 \
    --config cfgs/BrokenObjects/a5-airplanes-a2.yaml \
    --exp_name exp \
    --ckpts experiments/a5-airplanes-a2/BrokenObjects/exp/ckpt-epoch-200.pth

./scripts/train.sh \
    1 \
    --config cfgs/BrokenObjects/a6-chairs-a2.yaml \
    --exp_name exp \
    --val_freq 1000
./scripts/test.sh \
    1 \
    --config cfgs/BrokenObjects/a6-chairs-a2.yaml \
    --exp_name exp \
    --ckpts experiments/a6-chairs-a2/BrokenObjects/exp/ckpt-epoch-200.pth

./scripts/train.sh \
    2 \
    --config cfgs/BrokenObjects/a7-cars-a2.yaml \
    --exp_name exp \
    --val_freq 1000
./scripts/test.sh \
    2 \
    --config cfgs/BrokenObjects/a7-cars-a2.yaml \
    --exp_name exp \
    --ckpts experiments/a7-cars-a2/BrokenObjects/exp/ckpt-epoch-200.pth
