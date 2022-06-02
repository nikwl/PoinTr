export PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python 

# train
./scripts/train.sh 1 --config cfgs/BrokenObjects/PoinTr.yaml --exp_name test2 --val_freq 1000
./scripts/test.sh 1 --config cfgs/BrokenObjects/PoinTr.yaml --exp_name test2 --ckpts experiments/PoinTr/BrokenObjects/test2/ckpt-epoch-200.pth

./scripts/train.sh \
    1 \
    --config cfgs/BrokenObjects/a2-bottles.yaml \
    --exp_name exp \
    --val_freq 1000
./scripts/test.sh \
    1 \
    --config cfgs/BrokenObjects/a2-bottles.yaml \
    --exp_name exp \
    --ckpts experiments/a2-bottles/BrokenObjects/exp/ckpt-epoch-200.pth

./scripts/train.sh \
    2 \
    --config cfgs/BrokenObjects/a3-mugs.yaml \
    --exp_name exp \
    --val_freq 1000
./scripts/test.sh \
    2 \
    --config cfgs/BrokenObjects/a3-mugs.yaml \
    --exp_name exp \
    --ckpts experiments/a3-mugs/BrokenObjects/exp/ckpt-epoch-200.pth
