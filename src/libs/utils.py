import os, shutil, ctypes

class Utils:

    @staticmethod
    def is_admin() -> bool:
        """ Check if terminal is in adminstrator mode """
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    @staticmethod
    def flush_dns() -> bool:
        """ Flushes computers dns """
        os.system('ipconfig/flushdns')
        os.system('netsh winsock reset')
        return True

    @staticmethod
    def delete_dir(path, folder):
        """ Delete a directory quickly """
        os.rename(path+f"/{folder}", path+f"/{folder}2")
        os.mkdir(path+f"/{folder}")
        shutil.rmtree(path+f"/{folder}2")
