from weapon.detect import run
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--id', type=str, required=True)
parser.add_argument('--url', type=str, required=True)
args = parser.parse_args()

run(weights='weapon/sohas60hk.pt',conf_thres=0.6,source=args.url,nosave=True,idCamera=args.id)