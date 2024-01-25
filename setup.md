# Follow these steps to reproduce the results on another server.

## Setup Conda Environment

```bash
conda create -n mtp2 python=3.10 pip pytorch torchvision pytorch-cuda=12.1 -c pytorch -c nvidia -y
conda activate mtp2
pip install -r requirements.txt
```
