import torch


# stack src se to tgt se
def stack_se(src_se, tgt_se):
    return torch.cat([src_se, tgt_se]).mean(0)
