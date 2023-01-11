from extractLips import *
import os
import env
from check_data_kind import check_kind

def main():
    root = env.ROOT
    save_root = env.SAVE_ROOT
    if save_root is None:
        save_root = root
    err_log = env.ERR_LOG
    path_file = env.PATH_FILE
    # You need change number of for process.
    not_use = env.NOT_USE
    if not_use is None:
        not_use = []
    for k1 in env.KIND1:
        path = os.path.join(root, k1, env.KIND2)
        save_path1 = os.path.join(save_root, k1, env.SAVE_TYPE)
        make_folder(save_path1)
        for k3 in os.listdir(path):
            if (k3 in not_use):
                continue
            target1 = os.path.join(path, k3)
            save_path2 = os.path.join(save_path1, k3)
            make_folder(save_path2)
            if not check_kind(target1):
                record_err_log(err_log, target1+' is not found.')
                continue
            for dk in os.listdir(target1):
                target2 = os.path.join(target1, dk)
                save_path3 = os.path.join(save_path2, dk)
                make_folder(save_path3)
                if not check_kind(target2):
                    record_err_log(err_log, target2+' is not found.')
                    continue
                print('Now: '+target2)
                extract(target2, save_path3)  # extract lips
                if not check_lips_length(target2, save_path3):  # check length of result.
                    record_err_log(err_log, save_path3+' is not equal frame length.')
                write_path(path_file, save_path3)
main()
