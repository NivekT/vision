from dataset_helpers import make_dp, make_ffcv_dataloader

from bench_data_reading import pickle_bytesio_dp, torch_bytesio_dp
from common import bench, decode, iterate_one_epoch, ARCHIVE_ROOT, bytesio_to_tensor


ffcv_encoded = make_ffcv_dataloader(root=ARCHIVE_ROOT, transforms=False, encoded=True)
ffcv_decoded = make_ffcv_dataloader(root=ARCHIVE_ROOT, transforms=False, encoded=False)

pickle_decoded_dp = make_dp(root=ARCHIVE_ROOT, archive="pickle", archive_content="decoded")
torch_decoded_dp = make_dp(root=ARCHIVE_ROOT, archive="torch", archive_content="decoded")

if __name__ == "__main__":

    print("pickle bytesio->ToTensor()->decode_jpeg()")
    bench(iterate_one_epoch, inp=pickle_bytesio_dp.map(bytesio_to_tensor).map(decode))

    print("torch bytesio->ToTensor()->decode_jpeg()")
    bench(iterate_one_epoch, inp=torch_bytesio_dp.map(bytesio_to_tensor).map(decode))

    print("FFCV loading + decoding")
    bench(iterate_one_epoch, inp=ffcv_encoded)

    print("pickle pre-decoded")
    bench(iterate_one_epoch, inp=pickle_decoded_dp)

    print("torch pre-decoded")
    bench(iterate_one_epoch, inp=torch_decoded_dp)

    print("FFCV loading (pre-decoded)")
    bench(iterate_one_epoch, inp=ffcv_decoded)
    print()
