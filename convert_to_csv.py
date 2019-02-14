
# The format of these is easy to understand:

# The first value is the "label", that is, the actual digit that the handwriting is supposed to represent, such as a "7" or a "9". It is the answer to which the neural network is aspiring to classify.
# The subsequent values, all comma separated, are the pixel values of the handwritten digit. The size of the pixel array is 28 by 28, so there are 784 values after the label.


def convert(imgf, labelf, outf, n):
    f = open(imgf, "rb")
    o = open(outf, "w")
    l = open(labelf, "rb")

    f.read(16)
    l.read(8)
    images = []

    for i in range(n):
        image = [ord(l.read(1))]
        for j in range(28*28):
            image.append(ord(f.read(1)))
        images.append(image)

    for image in images:
        o.write(",".join(str(pix) for pix in image)+"\n")
    f.close()
    o.close()
    l.close()

convert("MNIST_data/train-images-idx3-ubyte", "MNIST_data/train-labels-idx1-ubyte",
        "MNIST_data/mnist_train.csv", 60000)
convert("MNIST_data/t10k-images-idx3-ubyte", "MNIST_data/t10k-labels-idx1-ubyte",
        "MNIST_data/mnist_test.csv", 10000)


