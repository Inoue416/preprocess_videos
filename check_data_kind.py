# This file is checking function of a data kind.
import env # You need to make env.py, env.py is setting file.
import os


def check_kind(path):
    return os.path.exists(path)


if __name__ == "__main__":
    root = env.root
    for k1 in env.kind1:
        path = os.path.join(root, k1, env.kind2)
        for k3 in os.listdir(path):
            if (k3 in env.not_target):
                continue
            target1 = os.path.join(path, k3)
            if not check_kind(target1):
                continue
            for dk in os.listdir(target1):
                target2 = os.path.join(target1, dk)
                if not check_kind(target2):
                    continue
                for data in os.listdir(target2):
                    data_path = os.path.join(target2, data)
                    if not check_kind(data_path):
                        continue
                    print(data_path)