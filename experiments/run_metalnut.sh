#!/bin/bash

# Run Metal Nut experiment for each individual dataset.
echo "Running Metal Nut"
for m in {0..2}
do
  echo "Manual Seed: $m"
  python train.py --dataset metal_nut \
                  --dataroot data/mvtec/metal_nut
                  --isize 32 \
                  --nc 3 \
                  --niter 15 \
                  --manualseed $m
done
exit 0
