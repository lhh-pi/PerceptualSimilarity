import argparse
import os
import lpips

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-d0', '--dir0', type=str, default='./imgs/gt')
parser.add_argument('-d1', '--dir1', type=str, default='')
parser.add_argument('-o', '--out', type=str, default='')
parser.add_argument('-v', '--version', type=str, default='0.1')
parser.add_argument('--use_gpu', action='store_true', help='turn on flag to use GPU')

opt = parser.parse_args()

# Initializing the model
loss_fn = lpips.LPIPS(net='alex', version=opt.version)
if opt.use_gpu:
    loss_fn.cuda()

if opt.out == '':
    opt.out = 'results/' + opt.dir1.split('/')[1][5:] + '.txt'

# crawl directories
f = open(opt.out, 'w')
files = os.listdir(opt.dir0)
log_str = ""
for file in files:
    if os.path.exists(os.path.join(opt.dir1, file)):
        # Load images
        img0 = lpips.im2tensor(lpips.load_image(os.path.join(opt.dir0, file)))  # RGB image from [-1,1]
        img1 = lpips.im2tensor(lpips.load_image(os.path.join(opt.dir1, file)))

        if opt.use_gpu:
            img0 = img0.cuda()
            img1 = img1.cuda()

        # Compute distance
        dist01 = loss_fn.forward(img0, img1)
        print('%s:\t%.3f' % (file, dist01))
        f.writelines('%s:\t%.6f\n' % (file, dist01))

f.close()
