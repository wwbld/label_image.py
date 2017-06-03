import os, sys

import tensorflow as tf

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# define function to check if a directory with 
# a particular name exists
def contains(existed, target):
    for name in existed:
        if target == name:
            return True
    return False

# change this as you see fit
image_path = sys.argv[1]
output_path = sys.argv[2]
existed = []
count = 0

if os.path.exists(output_path) == False:
    os.mkdir(output_path, 0755)

# Read in the image_data
for filename in os.listdir(image_path):
    fname = image_path+filename
    image_data = tf.gfile.FastGFile(fname, 'rb').read()

    # Loads label file, strips off carriage return
    label_lines = [line.rstrip() for line 
                       in tf.gfile.GFile("retrained_labels.txt")]

    # Unpersists graph from file
    with tf.gfile.FastGFile("retrained_graph.pb", 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        tf.import_graph_def(graph_def, name='')

    with tf.Session() as sess:
        # Feed the image_data as input to the graph and get first prediction
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
    
        predictions = sess.run(softmax_tensor, \
                 {'DecodeJpeg/contents:0': image_data})
    
        # Sort to show labels of first prediction in order of confidence
        top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
    
#        for node_id in top_k:
#            human_string = label_lines[node_id]
#            score = predictions[0][node_id]
#            print('%s (score = %.5f)' % (human_string, score))

        maxscore = 0;
        maxid = 0;
        target_name = ''
        for node_id in top_k:
            human_string = label_lines[node_id]
            score = predictions[0][node_id]
            if score > maxscore:
                maxscore = score
                maxid = node_id
                target_name = label_lines[maxid]
        count = count+1
        print('%d target is %s (score = %.5f)' % (count, target_name, maxscore))
        target_dir = output_path + '/' + target_name
        if contains(existed, target_name) == False:
            existed.append(target_name)
            if os.path.exists(target_dir) == False:
                os.mkdir(target_dir)
                print('create new directory %s' % (target_dir))
#                print('false')
        os.system('cp '+fname+' '+target_dir)









