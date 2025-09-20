import tensorflow as tf
import os
import time
from pathlib import Path
from reytools.file_system import create_directories


class CallBack:
    def __init__(self, call_back_dir):
        self.__create_log_dirs(call_back_dir)

    def __create_log_dirs(self, artifact_dir):
        self.root_dir = artifact_dir
        self.callback_dir = Path(os.path.join(artifact_dir, "callbacks"))
        self.tensorboard_log_dir = Path(os.path.join(self.callback_dir, "tensorboard_logs"))
        self.checkpoint_dir = Path(os.path.join(self.tensorboard_log_dir, "checkpoints"))
        self.checkpoint_path = Path(os.path.join(self.checkpoint_dir, "model.h5"))

        list_of_path = [self.callback_dir, self.tensorboard_log_dir, self.checkpoint_dir]
        create_directories(list_of_path)

    @property
    def _create_tb_callbacks(self):
        timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")
        tb_running_log_dir = os.path.join(
            self.tensorboard_log_dir,
            f"tb_logs_at_{timestamp}",
        )
        return tf.keras.callbacks.TensorBoard(log_dir=tb_running_log_dir)

    @property
    def _create_ckpt_callbacks(self):
        return tf.keras.callbacks.ModelCheckpoint(filepath=self.checkpoint_path, save_best_only=True)

    def get_tb_ckpt_callbacks(self):
        return [self._create_tb_callbacks, self._create_ckpt_callbacks]
