import tensorflow as tf
from object_detection.utils import config_util
from object_detection.protos import pipeline_pb2
from google.protobuf import text_format
import os
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as viz_utils
#from object_detection.builders import model_builder

WORKSPACE_PATH = 'D:/GitHub/SLAIComputerVisionProject/Tensorflow/workspace'
SCRIPTS_PATH = 'D:/GitHub/SLAIComputerVisionProject/Tensorflow/scripts'
APIMODEL_PATH = 'D:/GitHub/SLAIComputerVisionProject/Tensorflow/models'
ANNOTATION_PATH = WORKSPACE_PATH + '/annotations'
IMAGE_PATH = WORKSPACE_PATH + '/images'
MODEL_PATH = WORKSPACE_PATH + '/models'
PRETRAINED_MODEL_PATH = WORKSPACE_PATH + '/pre-trained-models'
CONFIG_PATH = MODEL_PATH + '/my_ssd_mobnet/pipeline.config'
CHECKPOINT_PATH = MODEL_PATH + '/my_ssd_mobnet/'
CUSTOM_MODEL_NAME = '/my_ssd_mobnet/'
#
# # python D:/GitHub/SLAIComputerVisionProject/Tensorflow/scripts/generate_tfrecord.py -x D:/GitHub/SLAIComputerVisionProject/Tensorflow/workspace/images/train -l D:/GitHub/SLAIComputerVisionProject/Tensorflow/workspace/annotations/label_map.pbtxt -o D:/GitHub/SLAIComputerVisionProject/Tensorflow/workspace/annotations/train.record
# # python D:/GitHub/SLAIComputerVisionProject/Tensorflow/scripts/generate_tfrecord.py -x D:/GitHub/SLAIComputerVisionProject/Tensorflow/workspace/images/test -l D:/GitHub/SLAIComputerVisionProject/Tensorflow/workspace/annotations/label_map.pbtxt -o D:/GitHub/SLAIComputerVisionProject/Tensorflow/workspace/annotations/test.record
# copy D:\GitHub\SLAIComputerVisionProject\Tensorflow\workspace\pre-trained-models\ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8\pipeline.config D:\GitHub\SLAIComputerVisionProject\Tensorflow\workspace\models\my_ssd_mobnet

# labels = [{'name': 'Hand', 'id': 1}]
# with open(ANNOTATION_PATH + '/label_map.pbtxt', 'w') as f:
#     for label in labels:
#         f.write('item{\n')
#         f.write('\tname:\'{}\'\n'.format(label['name']))
#         f.write('\tid:{}\n'.format(label['id']))
#         f.write('}\n')

config = config_util.get_configs_from_pipeline_file(CONFIG_PATH)
pipeline_config = pipeline_pb2.TrainEvalPipelineConfig()
with tf.io.gfile.GFile(CONFIG_PATH, "r") as f:
    proto_str = f.read()
    text_format.Merge(proto_str, pipeline_config)

pipeline_config.model.ssd.num_classes = 2
pipeline_config.train_config.batch_size = 4
pipeline_config.train_config.fine_tune_checkpoint = PRETRAINED_MODEL_PATH + '/ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8/checkpoint/ckpt-0'
pipeline_config.train_config.fine_tune_checkpoint_type = "detection"
pipeline_config.train_input_reader.label_map_path = ANNOTATION_PATH + '/label_map.pbtxt'
pipeline_config.train_input_reader.tf_record_input_reader.input_path[:] = [ANNOTATION_PATH + '/train.record']
pipeline_config.eval_input_reader[0].label_map_path = ANNOTATION_PATH + '/label_map.pbtxt'
pipeline_config.eval_input_reader[0].tf_record_input_reader.input_path[:] = [ANNOTATION_PATH + '/test.record']

config_text = text_format.MessageToString(pipeline_config)
with tf.io.gfile.GFile(CONFIG_PATH, "wb") as f:
    f.write(config_text)

# configs = config_util.get_configs_from_pipeline_file(CONFIG_PATH)
# detection_model = model_builder.build(model_config=configs['model'], is_training=False)


print("""python {}/research/object_detection/model_main_tf2.py --model_dir={}/{} --pipeline_config_path={}/{}/pipeline.config --num_train_steps=5000""".format(APIMODEL_PATH, MODEL_PATH, CUSTOM_MODEL_NAME, MODEL_PATH, CUSTOM_MODEL_NAME))


# Restore checkpoint
# ckpt = tf.compat.v2.train.Checkpoint(model=detection_model)
# ckpt.restore(os.path.join(CHECKPOINT_PATH, 'ckpt-6')).expect_partial()
#
#
# @tf.function
# def detect_fn(image):
#     image, shapes = detection_model.preprocess(image)
#     prediction_dict = detection_model.predict(image, shapes)
#     detections = detection_model.postprocess(prediction_dict, shapes)
#     return detections
