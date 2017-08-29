import numpy as np
import matplotlib.pyplot as plt


def main():
    """Basic machine learning example (k-nearest neighbor)."""

    #Training set and test point information.
    x_train = np.array([[1, 1], [2, 2.5], [3, 1.2], [5.5, 6.3], [6, 9], [7, 6]])
    y_train = ['green', 'green', 'green', 'black', 'black', 'black']
    x_test = np.array([3, 4])

    #Show training set points and test point on the plot with different color.
    plt.figure()
    plt.scatter(x_train[:, 0], x_train[:, 1], s=170, color=y_train[:])
    plt.scatter(x_test[0], x_test[1], s=170, color='red')
    plt.show()

    #Check distance for test point to every point in training set.
    num = len(x_train)
    distance = np.zeros(num)
    for i in range(num):
        distance[i] = dist(x_train[i], x_test)
    min_index = np.argmin(distance)

    #Print distance to everypoint and conclude color of test point.
    print(distance)
    print("test point should be {}".format(y_train[min_index]))


def dist(arg1, arg2):
    """Compute distance between given points."""
    return np.sqrt(np.sum((arg1-arg2)**2))


if __name__ == "__main__":
    main()
