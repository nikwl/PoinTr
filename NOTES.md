export PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python 

# train
./scripts/train.sh 1 --config cfgs/BrokenObjects/PoinTr.yaml --exp_name test2 --val_freq 1000
./scripts/test.sh 1 --config cfgs/BrokenObjects/PoinTr.yaml --exp_name test2 --ckpts experiments/PoinTr/BrokenObjects/test2/ckpt-epoch-200.pth