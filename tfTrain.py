WORKSPACE_PATH = 'D:/GitHub/SLAIComputerVisionProject/Tensorflow/workspace'
SCRIPTS_PATH = 'D:/GitHub/SLAIComputerVisionProject/Tensorflow/scripts'
APIMODEL_PATH = 'D:/GitHub/SLAIComputerVisionProject/Tensorflow/models'
ANNOTATION_PATH = WORKSPACE_PATH+'/annotations'
IMAGE_PATH = WORKSPACE_PATH+'/images'
MODEL_PATH = WORKSPACE_PATH+'/models'
PRETRAINED_MODEL_PATH = WORKSPACE_PATH+'/pre-trained-models'
CONFIG_PATH = MODEL_PATH+'/my_ssd_mobnet/pipeline.config'
CHECKPOINT_PATH = MODEL_PATH+'/my_ssd_mobnet/'

# python D:/GitHub/SLAIComputerVisionProject/Tensorflow/scripts/generate_tfrecord.py -x D:/GitHub/SLAIComputerVisionProject/Tensorflow/workspace/images/train -l D:/GitHub/SLAIComputerVisionProject/Tensorflow/workspace/annotations/label_map.pbtxt -o D:/GitHub/SLAIComputerVisionProject/Tensorflow/workspace/annotations/train.record
# python D:/GitHub/SLAIComputerVisionProject/Tensorflow/scripts/generate_tfrecord.py -x D:/GitHub/SLAIComputerVisionProject/Tensorflow/workspace/images/test -l D:/GitHub/SLAIComputerVisionProject/Tensorflow/workspace/annotations/label_map.pbtxt -o D:/GitHub/SLAIComputerVisionProject/Tensorflow/workspace/annotations/test.record

labels = [{'name': 'Hand', 'id': 1}]
with open(ANNOTATION_PATH + '/label_map.pbtxt', 'w') as f:
    for label in labels:
        f.write('item{\n')
        f.write('\tname:\'{}\'\n'.format(label['name']))
        f.write('\tid:{}\n'.format(label['id']))
        f.write('}\n')


