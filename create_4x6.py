# -*- coding: utf-8 -*-

from PIL import Image
import numpy as np

import os
import argparse


def pil_image_2_array(img):
    return np.array(
        img.getdata(),
        np.uint8).reshape(
            img.size[1],
            img.size[0],
            3
        )


def process_main(args):
    imgfilename = args.imgfilename[0]
    assert os.path.exists(imgfilename)

    im_frame = Image.open(imgfilename)
    print(im_frame.size)
    np_frame = pil_image_2_array(im_frame)
    np_frame_repeated = np.tile(np_frame, (2, 3, 1))
    print(np_frame.shape)
    print(np_frame_repeated.shape)

    out_im_frame = Image.fromarray(np_frame_repeated)
    if args.outputfilename is None:
        args.outputfilename = "output.png"
    else:
        args.outputfilename = args.outputfilename[0]

    out_im_frame.save(args.outputfilename)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="create a 4x6 image for passport photos",
    )
    parser.add_argument("imgfilename", nargs=1, help="image filename")
    parser.add_argument("--outputfilename", nargs=1, help="output filename")

    args = parser.parse_args()

    process_main(args)

