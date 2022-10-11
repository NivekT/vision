#!/bin/bash
#SBATCH --partition=train
#SBATCH --cpus-per-task=96 # 12 CPUs per GPU
#SBATCH --gpus-per-node=8
#SBATCH --nodes=1
#SBATCH --time=70:00:00


if [[ $1 = "tiny" ]]
then
    tiny="--tiny"
else
    tiny=""
fi


python bench_transforms.py $tiny
python bench_decoding.py $tiny

for fs in "ontap_isolated" "scratch" # "fsx_isolated"
do
    if [[ $fs = "scratch" ]]
    then 
        mkdir -p /scratch/nicolashug
        if [[ $1 = "tiny" ]]
        then
            cp /ontap_isolated/nicolashug/tinyimagenet /scratch/nicolashug/tinyimagenet -rv
        else
            cp /ontap_isolated/imagenet_full_size /scratch/nicolashug/imagenet_full_size -rv
        fi
    fi

    for script in "bench_e2e.py" "bench_data_reading_decoding.py" "bench_data_reading.py"
    do
        for num_workers in 0 12
        do
            # echo $script $fs $num_workers
            python $script --fs $fs --num-workers $num_workers $tiny --limit 12000
        done
    done
done