import argparse
import datetime
from pathlib import Path
from time import time

import torch

from ffcv.loader import Loader as FFCVLoader
from torchvision.io import decode_jpeg, ImageReadMode


parser = argparse.ArgumentParser()
parser.add_argument("--fs", default="fsx_isolated")
parser.add_argument("--tiny", action="store_true")
args = parser.parse_args()

print(args)

path_to_dataset = "tinyimagenet/081318/" if args.tiny else "imagenet_full_size/061417"
COMMON_ROOT = Path("/") / args.fs / "nicolashug" / path_to_dataset
ARCHIVE_ROOT = COMMON_ROOT / "archives/train"
JPEG_FILES_ROOT = COMMON_ROOT / "train"

DATASET_SIZE = 100_000 if args.tiny else 1_281_167

# Deactivate OMP / MKL parallelism: in most cases we'll run the data-loading
# pipeline within a parallelized DataLoader which will call this as well anyway.
torch.set_num_threads(1)


def bench(f, inp, num_exp=3, warmup=1, unit="μ", num_images_per_call=DATASET_SIZE):
    # Computes PER IMAGE median times
    for _ in range(warmup):
        f(inp)

    times = []
    for _ in range(num_exp):
        start = time()
        f(inp)
        end = time()
        times.append((end - start))

    mul = {"μ": 1e6, "m": 1e3, "s": 1}[unit]
    times = torch.tensor(times) / num_images_per_call
    median_sec = torch.median(times)

    times_unit = times * mul
    median_unit = torch.median(times_unit)

    over_10_epochs = datetime.timedelta(seconds=int(median_sec * DATASET_SIZE * 10))

    s = f"{median_unit:.1f} {unit}{'s' if unit != 's' else ''}/img (std={torch.std(times_unit):.2f})"
    print(f"{s:30}   {int(1 / median_sec):15,}   {over_10_epochs}")
    print()
    return median_sec


def iterate_one_epoch(obj):
    if isinstance(obj, (torch.utils.data.datapipes.datapipe.IterDataPipe, FFCVLoader)):
        list(obj)
    else:
        # Need to reproduce "random" access
        indices = torch.randperm(len(obj))
        for i in indices:
            obj[i]


def decode(encoded_tensor):
    return decode_jpeg(encoded_tensor, mode=ImageReadMode.RGB)

def bytesio_to_tensor(bytesio):
    return torch.frombuffer(bytesio.getbuffer(), dtype=torch.uint8)

